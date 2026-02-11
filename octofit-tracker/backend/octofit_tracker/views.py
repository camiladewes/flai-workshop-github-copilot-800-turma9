from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import (
    UserSerializer,
    TeamSerializer,
    ActivitySerializer,
    LeaderboardSerializer,
    WorkoutSerializer
)


@api_view(['GET'])
def api_root(request, format=None):
    """
    API root endpoint that provides links to all available endpoints.
    """
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'teams': reverse('team-list', request=request, format=format),
        'activities': reverse('activity-list', request=request, format=format),
        'leaderboard': reverse('leaderboard-list', request=request, format=format),
        'workouts': reverse('workout-list', request=request, format=format),
    })


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing users.
    
    list: Get all users
    create: Create a new user
    retrieve: Get a specific user
    update: Update a user
    partial_update: Partially update a user
    destroy: Delete a user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing teams.
    
    list: Get all teams
    create: Create a new team
    retrieve: Get a specific team
    update: Update a team
    partial_update: Partially update a team
    destroy: Delete a team
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing activities.
    
    list: Get all activities
    create: Create a new activity
    retrieve: Get a specific activity
    update: Update an activity
    partial_update: Partially update an activity
    destroy: Delete an activity
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing the leaderboard.
    
    list: Get all leaderboard entries
    create: Create a new leaderboard entry
    retrieve: Get a specific leaderboard entry
    update: Update a leaderboard entry
    partial_update: Partially update a leaderboard entry
    destroy: Delete a leaderboard entry
    """
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing workout suggestions.
    
    list: Get all workout suggestions
    create: Create a new workout suggestion
    retrieve: Get a specific workout suggestion
    update: Update a workout suggestion
    partial_update: Partially update a workout suggestion
    destroy: Delete a workout suggestion
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
