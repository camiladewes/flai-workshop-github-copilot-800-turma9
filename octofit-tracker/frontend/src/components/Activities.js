import React, { useState, useEffect } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const getActivityIcon = (activityType) => {
    const type = activityType?.toLowerCase() || '';
    if (type.includes('run')) return 'bi-person-walking';
    if (type.includes('bike') || type.includes('cycling')) return 'bi-bicycle';
    if (type.includes('swim')) return 'bi-water';
    if (type.includes('yoga')) return 'bi-hearts';
    if (type.includes('gym') || type.includes('strength')) return 'bi-trophy';
    if (type.includes('walk')) return 'bi-person-walking';
    return 'bi-activity';
  };

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;
    console.log('Activities API Endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Activities - Fetched Data:', data);
        // Handle both paginated (.results) and plain array responses
        const activitiesData = data.results || data;
        setActivities(Array.isArray(activitiesData) ? activitiesData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Activities - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return (
    <div className="container mt-4 loading-container">
      <div className="spinner-border text-primary" role="status">
        <span className="visually-hidden">Loading...</span>
      </div>
      <p className="mt-3">Loading activities...</p>
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
      <h2><i className="bi bi-activity"></i> Activities</h2>
      <p className="text-muted mb-4">Track and view all fitness activities</p>
      
      {activities.length === 0 ? (
        <div className="alert alert-info" role="alert">
          <i className="bi bi-info-circle"></i> No activities found.
        </div>
      ) : (
        <div className="row">
          {activities.map((activity, index) => (
            <div key={activity.id || index} className="col-md-6 col-lg-4 mb-4">
              <div className="card h-100">
                <div className="card-body">
                  <h5 className="card-title">
                    <i className={`bi ${getActivityIcon(activity.activity_type)}`}></i> {activity.activity_type || 'Activity'}
                  </h5>
                  <hr />
                  <div className="card-text">
                    <p className="mb-2">
                      <span className="badge bg-primary">Duration</span>
                      <strong className="ms-2">{activity.duration} min</strong>
                    </p>
                    <p className="mb-2">
                      <span className="badge bg-success">Distance</span>
                      <strong className="ms-2">{activity.distance} km</strong>
                    </p>
                    <p className="mb-2">
                      <span className="badge bg-danger">Calories</span>
                      <strong className="ms-2">{activity.calories || activity.calories_burned || 0}</strong>
                    </p>
                    <p className="mb-0">
                      <span className="badge bg-secondary">Date</span>
                      <strong className="ms-2">{new Date(activity.date).toLocaleDateString()}</strong>
                    </p>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Activities;
