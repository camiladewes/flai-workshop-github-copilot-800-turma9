from djongo import models


class User(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hero_name = models.CharField(max_length=100)
    team_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    total_points = models.IntegerField(default=0)
    level = models.IntegerField(default=1)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username


class Team(models.Model):
    _id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.JSONField(default=list)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user_id = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    distance = models.FloatField()  # in km
    calories = models.IntegerField()
    points = models.IntegerField()
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f"{self.activity_type} - {self.user_id}"


class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    team_id = models.CharField(max_length=100)
    team_name = models.CharField(max_length=100, null=True, blank=True)
    total_points = models.IntegerField()
    rank = models.IntegerField()
    type = models.CharField(max_length=20, default='user')  # 'user' or 'team'
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leaderboard'

    def __str__(self):
        if self.type == 'team':
            return f"{self.team_name} - Rank {self.rank}"
        return f"{self.username} - Rank {self.rank}"


class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    exercises = models.JSONField(default=list)
    recommended_for = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.name
