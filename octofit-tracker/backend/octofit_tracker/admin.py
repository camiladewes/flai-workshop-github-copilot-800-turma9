from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'hero_name', 'team_id', 'total_points', 'level', 'created_at']
    list_filter = ['team_id', 'level', 'created_at']
    search_fields = ['username', 'email', 'hero_name']
    ordering = ['-total_points']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['_id', 'name', 'description', 'created_at']
    search_fields = ['name', 'description']
    ordering = ['name']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'activity_type', 'duration', 'distance', 'calories', 'points', 'date', 'created_at']
    list_filter = ['activity_type', 'date', 'created_at']
    search_fields = ['user_id', 'activity_type']
    ordering = ['-date']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['rank', 'username', 'team_name', 'total_points', 'type', 'updated_at']
    list_filter = ['type', 'team_id', 'updated_at']
    search_fields = ['username', 'team_name']
    ordering = ['rank']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'difficulty', 'duration', 'created_at']
    list_filter = ['category', 'difficulty', 'created_at']
    search_fields = ['name', 'description', 'category']
    ordering = ['name']
