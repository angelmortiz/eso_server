import uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Equipment(models.Model):
    TYPE_BILATERAL = 'Bilateral'
    TYPE_UNILATERAL = 'Unilateral'

    TYPE_CHOICES = [
        (TYPE_BILATERAL, TYPE_BILATERAL),
        (TYPE_UNILATERAL, TYPE_UNILATERAL),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    alternative_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, null=True, blank=True)
    link_to_image = models.URLField(max_length=255, null=True, blank=True)
    link_to_thumbnail = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]


class Muscle(models.Model):
    TYPE_BIG = 'Big'
    TYPE_SMALL = 'Small'

    TYPE_CHOICES = [
        (TYPE_BIG, TYPE_BIG),
        (TYPE_SMALL, TYPE_SMALL),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    alternative_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=TYPE_BIG, null=True, blank=True)
    link_to_image = models.URLField(max_length=255, null=True, blank=True)
    link_to_thumbnail = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]


class ExerciseType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]


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
    alternative_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    difficulty = models.CharField(max_length=15, choices=DIFFICULTY_CHOICES, default=DIFFICULTY_INTERMEDIATE)
    compound_movement = models.BooleanField(default=False)
    link_to_image = models.URLField(max_length=255, null=True, blank=True)
    link_to_thumbnail = models.URLField(max_length=255, null=True, blank=True)
    link_to_video = models.URLField(max_length=255, null=True, blank=True)
    # Related muscle
    main_muscle = models.ForeignKey(to=Muscle, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='main_exercise_set')
    # Many-to-Many
    secondary_muscles = models.ManyToManyField(to=Muscle, related_name='secondary_exercise_set')
    types = models.ManyToManyField(to=ExerciseType)
    equipments = models.ManyToManyField(to=Equipment)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]


class TrainingType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]


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
    description = models.TextField(null=True, blank=True)
    variant = models.CharField(max_length=5, null=True, blank=True)
    # Related type
    type = models.ForeignKey(to=TrainingType, on_delete=models.SET_NULL, null=True, blank=True)
    target = models.CharField(max_length=20, choices=TARGET_CHOICES, default=TARGET_MIXED, null=True, blank=True)
    link_to_image = models.URLField(max_length=255, null=True, blank=True)
    link_to_thumbnail = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]


class WorkoutExerciseRoutine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Related workout
    workout = models.ForeignKey(to=Workout, on_delete=models.CASCADE, null=True, blank=True)
    # Related exercise
    exercise = models.ForeignKey(to=Exercise, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='exercise_workoutexerciseroutine_set')
    min_sets = models.PositiveSmallIntegerField(default=3)
    max_sets = models.PositiveSmallIntegerField(default=4)
    min_reps = models.PositiveSmallIntegerField(default=8)
    max_reps = models.PositiveSmallIntegerField(default=15)
    tempo_eccentric = models.PositiveSmallIntegerField(default=1)
    tempo_pause_1 = models.PositiveSmallIntegerField(default=1)
    tempo_concentric = models.PositiveSmallIntegerField(default=1)
    tempo_pause_2 = models.PositiveSmallIntegerField(default=1)
    min_rir = models.PositiveSmallIntegerField(default=0)
    max_rir = models.PositiveSmallIntegerField(default=3)
    # Superset
    superset = models.BooleanField(default=False)
    superset_exercise = models.ForeignKey(to=Exercise, on_delete=models.SET_NULL, default=None, null=True, blank=True,
                                          related_name='superset_workoutexerciseroutine_set')


class Program(models.Model):
    SEQUENCE_WEEKLY = 'Weekly'
    SEQUENCE_CYCLE = 'Cycle'

    SEQUENCE_OPTIONS = [
        (SEQUENCE_WEEKLY, SEQUENCE_WEEKLY),
        (SEQUENCE_CYCLE, SEQUENCE_CYCLE),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    sequence = models.CharField(max_length=10, choices=SEQUENCE_OPTIONS, default=SEQUENCE_WEEKLY)
    duration = models.PositiveSmallIntegerField()
    link_to_image = models.URLField(max_length=255, null=True, blank=True)
    link_to_thumbnail = models.URLField(max_length=255, null=True, blank=True)
    # Many-to-Many
    types = models.ManyToManyField(to=TrainingType)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]


class ProgramWorkoutRoutine(models.Model):
    DAY_MONDAY = 'Monday'
    DAY_TUESDAY = 'Tuesday'
    DAY_WEDNESDAY = 'Wednesday'
    DAY_THURSDAY = 'Thursday'
    DAY_FRIDAY = 'Friday'
    DAY_SATURDAY = 'Saturday'
    DAY_SUNDAY = 'Sunday'

    DAY_CHOICES = [
        (DAY_MONDAY, DAY_MONDAY),
        (DAY_TUESDAY, DAY_TUESDAY),
        (DAY_WEDNESDAY, DAY_WEDNESDAY),
        (DAY_THURSDAY, DAY_THURSDAY),
        (DAY_FRIDAY, DAY_FRIDAY),
        (DAY_SATURDAY, DAY_SATURDAY),
        (DAY_SUNDAY, DAY_SUNDAY),
    ]

    SEQUENCE_WEEKLY = 'Weekly'
    SEQUENCE_CYCLE = 'Cycle'

    SEQUENCE_OPTIONS = [
        (SEQUENCE_WEEKLY, SEQUENCE_WEEKLY),
        (SEQUENCE_CYCLE, SEQUENCE_CYCLE),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Related program
    program = models.ForeignKey(to=Program, on_delete=models.CASCADE, null=True, blank=True)
    # Related workout
    workout = models.ForeignKey(to=Workout, on_delete=models.SET_NULL, null=True, blank=True)
    sequence = models.CharField(max_length=10, choices=SEQUENCE_OPTIONS, default=SEQUENCE_WEEKLY)
    day_number = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)], null=True,
                                                  blank=True)
    day_of_the_week = models.CharField(max_length=10, choices=DAY_CHOICES, null=True, blank=True)
