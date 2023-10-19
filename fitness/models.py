import uuid
from django.db import models


class Equipment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    alternative_name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    link_to_image = models.URLField(max_length=255, null=True)
    link_to_thumbnail = models.URLField(max_length=255, null=True)


class Muscle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    alternative_name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    type = models.CharField(max_length=50)
    link_to_image = models.URLField(max_length=255, null=True)
    link_to_thumbnail = models.URLField(max_length=255, null=True)


class ExerciseType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=15)


class Exercise(models.Model):
    DIFFICULTY_EASY = 'Easy'
    DIFFICULTY_INTERMEDIATE = 'Intermediate'
    DIFFICULTY_ADVANCED = 'Advanced'

    DIFFICULTY_CHOICES = [
        (DIFFICULTY_EASY, DIFFICULTY_EASY),
        (DIFFICULTY_INTERMEDIATE, DIFFICULTY_INTERMEDIATE),
        (DIFFICULTY_ADVANCED, DIFFICULTY_ADVANCED),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    alternative_name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    difficulty = models.CharField(max_length=15, choices=DIFFICULTY_CHOICES, default=DIFFICULTY_INTERMEDIATE)
    compound_movement = models.BooleanField(default=False)
    link_to_image = models.URLField(max_length=255, null=True)
    link_to_thumbnail = models.URLField(max_length=255, null=True)
    link_to_video = models.URLField(max_length=255, null=True)
    # One-to-Many
    main_muscle = models.ForeignKey(to=Muscle, on_delete=models.PROTECT, related_name='main_exercises')
    # Many-to-Many
    types = models.ManyToManyField(to=ExerciseType, related_name='exercises')
    equipments = models.ManyToManyField(to=Equipment, related_name='exercises')
    secondary_muscles = models.ManyToManyField(to=Muscle, related_name='secondary_exercises')


class TrainingType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=15)


class Workout(models.Model):
    TARGET_FULL_BODY = 'Full Body'
    TARGET_UPPER_BODY = 'Upper Body'
    TARGET_LOWER_BODY = 'Lower Body'
    TARGET_ANTERIOR_MUSCLES = 'Anterior Muscles'
    TARGET_POSTERIOR_MUSCLES = 'Posterior Muscles'
    TARGET_MIXED = 'Mixed muscles'

    TARGET_CHOICES = [
        (TARGET_FULL_BODY, TARGET_FULL_BODY),
        (TARGET_UPPER_BODY, TARGET_UPPER_BODY),
        (TARGET_LOWER_BODY, TARGET_LOWER_BODY),
        (TARGET_ANTERIOR_MUSCLES, TARGET_ANTERIOR_MUSCLES),
        (TARGET_POSTERIOR_MUSCLES, TARGET_POSTERIOR_MUSCLES),
        (TARGET_MIXED, TARGET_MIXED),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    variant = models.CharField(max_length=5, null=True)
    type = models.ForeignKey(to=TrainingType, on_delete=models.SET_NULL, null=True)
    target = models.CharField(max_length=20, choices=TARGET_CHOICES, default=TARGET_MIXED, null=True)
    link_to_image = models.URLField(max_length=255, null=True)
    link_to_thumbnail = models.URLField(max_length=255, null=True)
    # Many-to-Many
    exercises = models.ManyToManyField(to=Exercise, related_name='workouts')


class Program(models.Model):
    SEQUENCE_WEEKLY = 'Weekly'
    SEQUENCE_CYCLE = 'Cycle'

    SEQUENCE_OPTIONS = [
        (SEQUENCE_WEEKLY, SEQUENCE_WEEKLY),
        (SEQUENCE_CYCLE, SEQUENCE_CYCLE),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    sequence = models.CharField(max_length=10, choices=SEQUENCE_OPTIONS, default=SEQUENCE_WEEKLY)
    duration = models.PositiveSmallIntegerField()
    link_to_image = models.URLField(max_length=255, null=True)
    link_to_thumbnail = models.URLField(max_length=255, null=True)
    # Many-to-Many
    types = models.ManyToManyField(to=TrainingType, related_name='programs', null=True)
    workouts = models.ManyToManyField(to=Workout, related_name='programs')
