from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from pymongo import MongoClient
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Clear existing data
        self.stdout.write('Clearing existing data...')
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create unique index on email field
        db.users.create_index([('email', 1)], unique=True)
        self.stdout.write(self.style.SUCCESS('Created unique index on email field'))

        # Superhero data
        marvel_heroes = [
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'hero_name': 'Peter Parker'},
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'hero_name': 'Tony Stark'},
            {'name': 'Captain America', 'email': 'captainamerica@marvel.com', 'hero_name': 'Steve Rogers'},
            {'name': 'Thor', 'email': 'thor@marvel.com', 'hero_name': 'Thor Odinson'},
            {'name': 'Black Widow', 'email': 'blackwidow@marvel.com', 'hero_name': 'Natasha Romanoff'},
            {'name': 'Hulk', 'email': 'hulk@marvel.com', 'hero_name': 'Bruce Banner'},
        ]

        dc_heroes = [
            {'name': 'Batman', 'email': 'batman@dc.com', 'hero_name': 'Bruce Wayne'},
            {'name': 'Superman', 'email': 'superman@dc.com', 'hero_name': 'Clark Kent'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'hero_name': 'Diana Prince'},
            {'name': 'Flash', 'email': 'flash@dc.com', 'hero_name': 'Barry Allen'},
            {'name': 'Aquaman', 'email': 'aquaman@dc.com', 'hero_name': 'Arthur Curry'},
            {'name': 'Green Lantern', 'email': 'greenlantern@dc.com', 'hero_name': 'Hal Jordan'},
        ]

        # Create teams
        self.stdout.write('Creating teams...')
        marvel_team = {
            '_id': 'team_marvel',
            'name': 'Team Marvel',
            'description': 'Avengers assemble!',
            'created_at': datetime.now(),
            'members': []
        }

        dc_team = {
            '_id': 'team_dc',
            'name': 'Team DC',
            'description': 'Justice League unite!',
            'created_at': datetime.now(),
            'members': []
        }

        # Insert users and populate teams
        self.stdout.write('Creating users...')
        marvel_user_ids = []
        dc_user_ids = []

        for hero in marvel_heroes:
            user_doc = {
                'username': hero['name'].lower().replace(' ', '_').replace('-', '_'),
                'email': hero['email'],
                'hero_name': hero['hero_name'],
                'team_id': 'team_marvel',
                'created_at': datetime.now(),
                'total_points': random.randint(500, 2000),
                'level': random.randint(1, 10)
            }
            result = db.users.insert_one(user_doc)
            marvel_user_ids.append(str(result.inserted_id))

        for hero in dc_heroes:
            user_doc = {
                'username': hero['name'].lower().replace(' ', '_').replace('-', '_'),
                'email': hero['email'],
                'hero_name': hero['hero_name'],
                'team_id': 'team_dc',
                'created_at': datetime.now(),
                'total_points': random.randint(500, 2000),
                'level': random.randint(1, 10)
            }
            result = db.users.insert_one(user_doc)
            dc_user_ids.append(str(result.inserted_id))

        # Update team members
        marvel_team['members'] = marvel_user_ids
        dc_team['members'] = dc_user_ids

        db.teams.insert_one(marvel_team)
        db.teams.insert_one(dc_team)
        self.stdout.write(self.style.SUCCESS(f'Created {len(marvel_heroes)} Marvel heroes'))
        self.stdout.write(self.style.SUCCESS(f'Created {len(dc_heroes)} DC heroes'))

        # Create activities
        self.stdout.write('Creating activities...')
        activity_types = ['Running', 'Cycling', 'Swimming', 'Weightlifting', 'Yoga', 'Boxing']
        all_user_ids = marvel_user_ids + dc_user_ids

        for _ in range(50):
            activity_doc = {
                'user_id': random.choice(all_user_ids),
                'activity_type': random.choice(activity_types),
                'duration': random.randint(15, 120),  # minutes
                'distance': round(random.uniform(1, 20), 2),  # km
                'calories': random.randint(100, 800),
                'points': random.randint(10, 100),
                'date': datetime.now() - timedelta(days=random.randint(0, 30)),
                'created_at': datetime.now()
            }
            db.activities.insert_one(activity_doc)

        self.stdout.write(self.style.SUCCESS('Created 50 activities'))

        # Create workouts
        self.stdout.write('Creating workout suggestions...')
        workouts = [
            {
                'name': 'Super Strength Training',
                'description': 'Build strength like the Hulk',
                'category': 'Strength',
                'difficulty': 'Advanced',
                'duration': 60,
                'exercises': ['Deadlifts', 'Bench Press', 'Squats', 'Pull-ups'],
                'recommended_for': ['team_marvel', 'team_dc']
            },
            {
                'name': 'Speed and Agility',
                'description': 'Move like the Flash',
                'category': 'Cardio',
                'difficulty': 'Intermediate',
                'duration': 45,
                'exercises': ['Sprints', 'Ladder Drills', 'Jump Rope', 'Burpees'],
                'recommended_for': ['team_dc']
            },
            {
                'name': 'Warrior Conditioning',
                'description': 'Train like Wonder Woman',
                'category': 'Mixed',
                'difficulty': 'Advanced',
                'duration': 90,
                'exercises': ['Combat Training', 'HIIT', 'Core Work', 'Flexibility'],
                'recommended_for': ['team_dc', 'team_marvel']
            },
            {
                'name': 'Web-Slinger Circuit',
                'description': 'Agility training for Spider-Man',
                'category': 'Agility',
                'difficulty': 'Intermediate',
                'duration': 45,
                'exercises': ['Climbing', 'Parkour', 'Plyometrics', 'Balance'],
                'recommended_for': ['team_marvel']
            },
            {
                'name': 'Asgardian Power',
                'description': 'Strength of the Gods',
                'category': 'Strength',
                'difficulty': 'Advanced',
                'duration': 75,
                'exercises': ['Olympic Lifts', 'Hammer Throws', 'Battle Ropes', 'Farmer Walks'],
                'recommended_for': ['team_marvel']
            }
        ]

        for workout in workouts:
            workout['created_at'] = datetime.now()
            db.workouts.insert_one(workout)

        self.stdout.write(self.style.SUCCESS(f'Created {len(workouts)} workout suggestions'))

        # Calculate and create leaderboard
        self.stdout.write('Creating leaderboard...')
        
        # Individual leaderboard
        users = list(db.users.find())
        for user in users:
            leaderboard_doc = {
                'user_id': str(user['_id']),
                'username': user['username'],
                'team_id': user['team_id'],
                'total_points': user['total_points'],
                'rank': 0,  # Will be calculated
                'updated_at': datetime.now()
            }
            db.leaderboard.insert_one(leaderboard_doc)

        # Update ranks
        sorted_users = sorted(users, key=lambda x: x['total_points'], reverse=True)
        for rank, user in enumerate(sorted_users, start=1):
            db.leaderboard.update_one(
                {'user_id': str(user['_id'])},
                {'$set': {'rank': rank}}
            )

        # Team leaderboard
        marvel_total = sum(u['total_points'] for u in users if u['team_id'] == 'team_marvel')
        dc_total = sum(u['total_points'] for u in users if u['team_id'] == 'team_dc')

        db.leaderboard.insert_one({
            'team_id': 'team_marvel',
            'team_name': 'Team Marvel',
            'total_points': marvel_total,
            'rank': 1 if marvel_total > dc_total else 2,
            'type': 'team',
            'updated_at': datetime.now()
        })

        db.leaderboard.insert_one({
            'team_id': 'team_dc',
            'team_name': 'Team DC',
            'total_points': dc_total,
            'rank': 1 if dc_total > marvel_total else 2,
            'type': 'team',
            'updated_at': datetime.now()
        })

        self.stdout.write(self.style.SUCCESS('Created leaderboard entries'))

        self.stdout.write(self.style.SUCCESS('Database population completed!'))
        self.stdout.write(f'Total users: {len(users)}')
        self.stdout.write(f'Total activities: 50')
        self.stdout.write(f'Total workouts: {len(workouts)}')
        self.stdout.write(f'Team Marvel points: {marvel_total}')
        self.stdout.write(f'Team DC points: {dc_total}')

        client.close()

