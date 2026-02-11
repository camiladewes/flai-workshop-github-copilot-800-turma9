import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function Home() {
  return (
    <div className="container mt-4">
      <div className="jumbotron text-center">
        <h1 className="display-3"><i className="bi bi-award"></i> Welcome to OctoFit Tracker!</h1>
        <p className="lead mt-3">Track your fitness activities, compete with teams, and achieve your fitness goals.</p>
        <hr className="my-4" />
        <p className="mb-4">Join thousands of users on their journey to better health and wellness.</p>
        <div className="d-flex justify-content-center gap-3 flex-wrap">
          <Link to="/activities" className="btn btn-light btn-lg">
            <i className="bi bi-bicycle"></i> View Activities
          </Link>
          <Link to="/teams" className="btn btn-light btn-lg">
            <i className="bi bi-people"></i> Join a Team
          </Link>
          <Link to="/workouts" className="btn btn-light btn-lg">
            <i className="bi bi-heart-pulse"></i> Start Workout
          </Link>
        </div>
      </div>
      
      <div className="row mt-5">
        <div className="col-md-4 mb-4">
          <div className="card text-center">
            <div className="card-body">
              <i className="bi bi-activity display-4 text-primary mb-3"></i>
              <h5 className="card-title">Track Activities</h5>
              <p className="card-text">Log your workouts, runs, cycling sessions, and more. Stay on top of your fitness journey.</p>
              <Link to="/activities" className="btn btn-outline-primary">View Activities</Link>
            </div>
          </div>
        </div>
        <div className="col-md-4 mb-4">
          <div className="card text-center">
            <div className="card-body">
              <i className="bi bi-trophy display-4 text-warning mb-3"></i>
              <h5 className="card-title">Compete</h5>
              <p className="card-text">Join the leaderboard, compete with friends, and earn points for your achievements.</p>
              <Link to="/leaderboard" className="btn btn-outline-primary">View Leaderboard</Link>
            </div>
          </div>
        </div>
        <div className="col-md-4 mb-4">
          <div className="card text-center">
            <div className="card-body">
              <i className="bi bi-people display-4 text-success mb-3"></i>
              <h5 className="card-title">Team Up</h5>
              <p className="card-text">Create or join teams, work together towards common goals, and motivate each other.</p>
              <Link to="/teams" className="btn btn-outline-primary">Browse Teams</Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary sticky-top">
          <div className="container-fluid">
            <Link className="navbar-brand d-flex align-items-center" to="/">
              <img src="/octofitapp-small.png" alt="OctoFit Logo" className="navbar-logo me-2" />
              <span>OctoFit Tracker</span>
            </Link>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav ms-auto">
                <li className="nav-item">
                  <Link className="nav-link" to="/">
                    <i className="bi bi-house-door"></i> Home
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/users">
                    <i className="bi bi-person-circle"></i> Users
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">
                    <i className="bi bi-activity"></i> Activities
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">
                    <i className="bi bi-people"></i> Teams
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">
                    <i className="bi bi-trophy"></i> Leaderboard
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">
                    <i className="bi bi-heart-pulse"></i> Workouts
                  </Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/users" element={<Users />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
