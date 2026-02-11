from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime


class UserModelTest(TestCase):
    """Test cases for User model"""
    
    def setUp(self):
        self.user = User.objects.create(
            username='test_hero',
            email='test@example.com',
            hero_name='Test Hero',
            team_id='team_test',
            total_points=100,
            level=1
        )
    
    def test_user_creation(self):
        """Test user model creation"""
        self.assertEqual(self.user.username, 'test_hero')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.total_points, 100)
        self.assertEqual(self.user.level, 1)
    
    def test_user_string_representation(self):
        """Test user string representation"""
        self.assertEqual(str(self.user), 'test_hero')


class TeamModelTest(TestCase):
    """Test cases for Team model"""
    
    def setUp(self):
        self.team = Team.objects.create(
            _id='team_test',
            name='Test Team',
            description='A test team',
            members=[]
        )
    
    def test_team_creation(self):
        """Test team model creation"""
        self.assertEqual(self.team._id, 'team_test')
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.description, 'A test team')
    
    def test_team_string_representation(self):
        """Test team string representation"""
        self.assertEqual(str(self.team), 'Test Team')


class ActivityModelTest(TestCase):
    """Test cases for Activity model"""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            user_id='user123',
            activity_type='Running',
            duration=30,
            distance=5.0,
            calories=300,
            points=50,
            date=datetime.now()
        )
    
    def test_activity_creation(self):
        """Test activity model creation"""
        self.assertEqual(self.activity.user_id, 'user123')
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.distance, 5.0)


class APIRootTest(APITestCase):
    """Test cases for API root endpoint"""
    
    def test_api_root(self):
        """Test API root endpoint returns all available endpoints"""
        url = reverse('api-root')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)


class UserAPITest(APITestCase):
    """Test cases for User API endpoints"""
    
    def setUp(self):
        self.user = User.objects.create(
            username='api_test_user',
            email='apitest@example.com',
            hero_name='API Test Hero',
            team_id='team_test',
            total_points=200,
            level=2
        )
    
    def test_get_users_list(self):
        """Test retrieving list of users"""
        url = reverse('user-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
    
    def test_get_user_detail(self):
        """Test retrieving a single user"""
        url = reverse('user-detail', kwargs={'pk': self.user._id})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'api_test_user')


class TeamAPITest(APITestCase):
    """Test cases for Team API endpoints"""
    
    def setUp(self):
        self.team = Team.objects.create(
            _id='api_team_test',
            name='API Test Team',
            description='Team for API testing',
            members=[]
        )
    
    def test_get_teams_list(self):
        """Test retrieving list of teams"""
        url = reverse('team-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
    
    def test_get_team_detail(self):
        """Test retrieving a single team"""
        url = reverse('team-detail', kwargs={'pk': self.team._id})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'API Test Team')


class ActivityAPITest(APITestCase):
    """Test cases for Activity API endpoints"""
    
    def test_get_activities_list(self):
        """Test retrieving list of activities"""
        url = reverse('activity-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LeaderboardAPITest(APITestCase):
    """Test cases for Leaderboard API endpoints"""
    
    def test_get_leaderboard_list(self):
        """Test retrieving leaderboard"""
        url = reverse('leaderboard-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITest(APITestCase):
    """Test cases for Workout API endpoints"""
    
    def test_get_workouts_list(self):
        """Test retrieving list of workouts"""
        url = reverse('workout-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

