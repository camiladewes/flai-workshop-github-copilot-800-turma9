import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [expandedTeams, setExpandedTeams] = useState({});

  const toggleTeamMembers = (teamId) => {
    setExpandedTeams(prev => ({
      ...prev,
      [teamId]: !prev[teamId]
    }));
  };

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;
    console.log('Teams API Endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Teams - Fetched Data:', data);
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results || data;
        setTeams(Array.isArray(teamsData) ? teamsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Teams - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return (
    <div className="container mt-4 loading-container">
      <div className="spinner-border text-primary" role="status">
        <span className="visually-hidden">Loading...</span>
      </div>
      <p className="mt-3">Loading teams...</p>
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
      <h2><i className="bi bi-people"></i> Teams</h2>
      <p className="text-muted mb-4">Join a team and compete together</p>
      
      {teams.length === 0 ? (
        <div className="alert alert-info" role="alert">
          <i className="bi bi-info-circle"></i> No teams found.
        </div>
      ) : (
        <div className="row">
          {teams.map((team, index) => {
            const isExpanded = expandedTeams[team._id || team.id];
            const members = Array.isArray(team.members) ? team.members : [];
            
            return (
              <div key={team._id || team.id || index} className="col-md-6 col-lg-4 mb-4">
                <div className="card h-100">
                  <div className="card-body d-flex flex-column">
                    <h5 className="card-title">
                      <i className="bi bi-shield-check"></i> {team.name}
                    </h5>
                    <p className="card-text flex-grow-1">
                      {team.description || 'No description available'}
                    </p>
                    <hr />
                    <div className="d-flex justify-content-between align-items-center mb-2">
                      <span className="badge bg-info text-dark">
                        <i className="bi bi-people-fill"></i> {members.length} Members
                      </span>
                      <button 
                        className="btn btn-sm btn-primary"
                        onClick={() => toggleTeamMembers(team._id || team.id)}
                      >
                        {isExpanded ? 'Hide' : 'View'} Members
                      </button>
                    </div>
                    {isExpanded && (
                      <div className="mt-2">
                        <hr />
                        <h6 className="text-muted mb-2">Team Members:</h6>
                        {members.length > 0 ? (
                          <ul className="list-unstyled mb-0">
                            {members.map((member, idx) => (
                              <li key={idx} className="mb-1">
                                <i className="bi bi-person-circle text-primary"></i> {member}
                              </li>
                            ))}
                          </ul>
                        ) : (
                          <p className="text-muted mb-0"><small>No members yet</small></p>
                        )}
                      </div>
                    )}
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}

export default Teams;
