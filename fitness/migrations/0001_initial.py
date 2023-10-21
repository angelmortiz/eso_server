# Generated by Django 4.2.6 on 2023-10-21 18:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('alternative_name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, choices=[('Bilateral', 'Bilateral'), ('Unilateral', 'Unilateral')], max_length=15, null=True)),
                ('link_to_image', models.URLField(blank=True, max_length=255, null=True)),
                ('link_to_thumbnail', models.URLField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('alternative_name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('difficulty', models.CharField(choices=[('Easy', 'Easy'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='Intermediate', max_length=15)),
                ('compound_movement', models.BooleanField(default=False)),
                ('link_to_image', models.URLField(blank=True, max_length=255, null=True)),
                ('link_to_thumbnail', models.URLField(blank=True, max_length=255, null=True)),
                ('link_to_video', models.URLField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ExerciseType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Muscle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('alternative_name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, choices=[('Big', 'Big'), ('Small', 'Small')], default='Big', max_length=10, null=True)),
                ('link_to_image', models.URLField(blank=True, max_length=255, null=True)),
                ('link_to_thumbnail', models.URLField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('sequence', models.CharField(choices=[('Weekly', 'Weekly'), ('Cycle', 'Cycle')], default='Weekly', max_length=10)),
                ('duration', models.PositiveSmallIntegerField()),
                ('link_to_image', models.URLField(blank=True, max_length=255, null=True)),
                ('link_to_thumbnail', models.URLField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProgramWorkoutRoutine',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sequence', models.CharField(choices=[('Weekly', 'Weekly'), ('Cycle', 'Cycle')], default='Weekly', max_length=10)),
                ('day_number', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)])),
                ('day_of_the_week', models.CharField(blank=True, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('variant', models.CharField(blank=True, max_length=5, null=True)),
                ('target', models.CharField(blank=True, choices=[('Full Body', 'Full Body'), ('Upper Body', 'Upper Body'), ('Lower Body', 'Lower Body'), ('Anterior Muscles', 'Anterior Muscles'), ('Posterior Muscles', 'Posterior Muscles'), ('Mixed muscles', 'Mixed muscles')], default='Mixed muscles', max_length=20, null=True)),
                ('link_to_image', models.URLField(blank=True, max_length=255, null=True)),
                ('link_to_thumbnail', models.URLField(blank=True, max_length=255, null=True)),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fitness.trainingtype')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='WorkoutExerciseRoutine',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('min_sets', models.PositiveSmallIntegerField(default=3)),
                ('max_sets', models.PositiveSmallIntegerField(default=4)),
                ('min_reps', models.PositiveSmallIntegerField(default=8)),
                ('max_reps', models.PositiveSmallIntegerField(default=15)),
                ('tempo_eccentric', models.PositiveSmallIntegerField(default=1)),
                ('tempo_pause_1', models.PositiveSmallIntegerField(default=1)),
                ('tempo_concentric', models.PositiveSmallIntegerField(default=1)),
                ('tempo_pause_2', models.PositiveSmallIntegerField(default=1)),
                ('min_rir', models.PositiveSmallIntegerField(default=0)),
                ('max_rir', models.PositiveSmallIntegerField(default=3)),
                ('superset', models.BooleanField(default=False)),
                ('exercise', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exercise_workoutexerciseroutine_set', to='fitness.exercise')),
                ('superset_exercise', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='superset_workoutexerciseroutine_set', to='fitness.exercise')),
                ('workout', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fitness.workout')),
            ],
        ),
        migrations.AddIndex(
            model_name='trainingtype',
            index=models.Index(fields=['name'], name='fitness_tra_name_c62927_idx'),
        ),
        migrations.AddField(
            model_name='programworkoutroutine',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fitness.program'),
        ),
        migrations.AddField(
            model_name='programworkoutroutine',
            name='workout',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fitness.workout'),
        ),
        migrations.AddField(
            model_name='program',
            name='types',
            field=models.ManyToManyField(to='fitness.trainingtype'),
        ),
        migrations.AddIndex(
            model_name='muscle',
            index=models.Index(fields=['name'], name='fitness_mus_name_79e341_idx'),
        ),
        migrations.AddIndex(
            model_name='exercisetype',
            index=models.Index(fields=['name'], name='fitness_exe_name_2b9093_idx'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='equipments',
            field=models.ManyToManyField(to='fitness.equipment'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='main_muscle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_exercise_set', to='fitness.muscle'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='secondary_muscles',
            field=models.ManyToManyField(related_name='secondary_exercise_set', to='fitness.muscle'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='types',
            field=models.ManyToManyField(to='fitness.exercisetype'),
        ),
        migrations.AddIndex(
            model_name='equipment',
            index=models.Index(fields=['name'], name='fitness_equ_name_ef264f_idx'),
        ),
        migrations.AddIndex(
            model_name='workout',
            index=models.Index(fields=['name'], name='fitness_wor_name_bd6075_idx'),
        ),
        migrations.AddIndex(
            model_name='program',
            index=models.Index(fields=['name'], name='fitness_pro_name_61b691_idx'),
        ),
        migrations.AddIndex(
            model_name='exercise',
            index=models.Index(fields=['name'], name='fitness_exe_name_91210a_idx'),
        ),
    ]
