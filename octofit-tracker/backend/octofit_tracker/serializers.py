from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['_id', 'username', 'email', 'hero_name', 'team_id', 'created_at', 'total_points', 'level']
        read_only_fields = ['_id', 'created_at']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['_id', 'name', 'description', 'created_at', 'members']
        read_only_fields = ['created_at']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['_id', 'user_id', 'activity_type', 'duration', 'distance', 'calories', 'points', 'date', 'created_at']
        read_only_fields = ['_id', 'created_at']


class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ['_id', 'user_id', 'username', 'team_id', 'team_name', 'total_points', 'rank', 'type', 'updated_at']
        read_only_fields = ['_id', 'updated_at']


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description', 'category', 'difficulty', 'duration', 'exercises', 'recommended_for', 'created_at']
        read_only_fields = ['_id', 'created_at']
