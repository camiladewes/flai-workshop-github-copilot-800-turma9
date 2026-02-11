import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
    console.log('Workouts API Endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts - Fetched Data:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Workouts - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return (
    <div className="container mt-4 loading-container">
      <div className="spinner-border text-primary" role="status">
        <span className="visually-hidden">Loading...</span>
      </div>
      <p className="mt-3">Loading workouts...</p>
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
      <h2><i className="bi bi-heart-pulse"></i> Workout Suggestions</h2>
      <p className="text-muted mb-4">Personalized workout plans to achieve your fitness goals</p>
      
      {workouts.length === 0 ? (
        <div className="alert alert-info" role="alert">
          <i className="bi bi-info-circle"></i> No workouts found.
        </div>
      ) : (
        <div className="row">
          {workouts.map((workout, index) => {
            const difficulty = workout.difficulty_level || workout.difficulty || 'medium';
            let difficultyColor = 'bg-warning';
            if (difficulty.toLowerCase() === 'easy' || difficulty.toLowerCase() === 'beginner') {
              difficultyColor = 'bg-success';
            } else if (difficulty.toLowerCase() === 'hard' || difficulty.toLowerCase() === 'advanced') {
              difficultyColor = 'bg-danger';
            }
            
            return (
              <div key={workout.id || index} className="col-md-6 col-lg-4 mb-4">
                <div className="card h-100">
                  <div className="card-body d-flex flex-column">
                    <h5 className="card-title">
                      <i className="bi bi-lightning"></i> {workout.name || workout.workout_type}
                    </h5>
                    <p className="card-text flex-grow-1">{workout.description}</p>
                    <hr />
                    <div className="d-flex justify-content-between align-items-center mb-3">
                      <span className="badge bg-primary">
                        <i className="bi bi-clock"></i> {workout.duration} min
                      </span>
                      <span className={`badge ${difficultyColor}`}>
                        <i className="bi bi-speedometer"></i> {difficulty}
                      </span>
                    </div>
                    <button className="btn btn-primary w-100">
                      <i className="bi bi-play-circle"></i> Start Workout
                    </button>
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

export default Workouts;
