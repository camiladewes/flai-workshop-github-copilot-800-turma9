import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
    console.log('Leaderboard API Endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Leaderboard - Fetched Data:', data);
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Leaderboard - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return (
    <div className="container mt-4 loading-container">
      <div className="spinner-border text-primary" role="status">
        <span className="visually-hidden">Loading...</span>
      </div>
      <p className="mt-3">Loading leaderboard...</p>
    </div>
  );
  
  if (error) return (
    <div className="container mt-4 error-container">
      <div className="alert alert-danger" role="alert">
        <h4 className="alert-heading">Error!</h4>
        <p>{error}</p>
      </div>
    </div>
  );

  return (
    <div className="container mt-4">
      <h2><i className="bi bi-trophy"></i> Leaderboard</h2>
      <p className="text-muted mb-4">Top performers and their achievements</p>
      
      {leaderboard.length === 0 ? (
        <div className="alert alert-info" role="alert">
          <i className="bi bi-info-circle"></i> No leaderboard data found.
        </div>
      ) : (
        <div className="table-responsive">
          <table className="table table-hover table-striped align-middle">
            <thead>
              <tr>
                <th scope="col" className="text-center"><i className="bi bi-hash"></i> Rank</th>
                <th scope="col"><i className="bi bi-person"></i> User</th>
                <th scope="col" className="text-center"><i className="bi bi-star"></i> Total Points</th>
              </tr>
            </thead>
            <tbody>
              {leaderboard.map((entry, index) => {
                const rank = entry.rank || index + 1;
                let rankBadge = 'bg-secondary';
                if (rank === 1) rankBadge = 'bg-warning';
                else if (rank === 2) rankBadge = 'bg-secondary';
                else if (rank === 3) rankBadge = 'bg-danger';
                
                return (
                  <tr key={entry.id || index}>
                    <td className="text-center">
                      <span className={`badge ${rankBadge} fs-6`}>{rank}</span>
                    </td>
                    <td><strong>{entry.username || entry.user_name || entry.user || 'Unknown'}</strong></td>
                    <td className="text-center">
                      <span className="badge bg-primary fs-6">{entry.total_points || entry.points || 0}</span>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default Leaderboard;
