from rest_framework import serializers
from .models import (
    Equipment,
    Muscle,
    ExerciseType,
    Exercise,
    TrainingType,
    Workout,
    WorkoutExerciseRoutine,
    Program,
    ProgramWorkoutRoutine
)


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id', 'name', 'alternative_name', 'description', 'type', 'link_to_image', 'link_to_thumbnail']


class MuscleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscle
        fields = ['id', 'name', 'alternative_name', 'description', 'type', 'link_to_image', 'link_to_thumbnail']


class ExerciseMuscleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscle
        fields = ['id', 'name', 'alternative_name']


class ExerciseEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscle
        fields = ['id', 'name', 'alternative_name']


class ExerciseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseType
        fields = ['id', 'name']


class ExerciseSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'alternative_name', 'description', 'difficulty', 'compound_movement',
                  'link_to_image', 'link_to_thumbnail', 'link_to_video']


class ExerciseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'alternative_name', 'description', 'difficulty', 'compound_movement',
                  'link_to_image', 'link_to_thumbnail', 'link_to_video', 'main_muscle', 'secondary_muscles',
                  'equipments', 'types']

    main_muscle = ExerciseMuscleSerializer()
    secondary_muscles = ExerciseMuscleSerializer(many=True)
    equipments = ExerciseEquipmentSerializer(many=True)
    types = ExerciseTypeSerializer(many=True)


class TrainingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingType
        fields = ['name']


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'variant', 'type', 'target', 'link_to_image', 'link_to_thumbnail']


class WorkoutExerciseRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExerciseRoutine
        fields = ['id', 'workout', 'exercise', 'min_sets', 'max_sets', 'min_reps', 'max_reps', 'tempo_eccentric',
                  'tempo_pause_1', 'tempo_concentric', 'tempo_pause_2', 'min_rir', 'max_rir', 'superset',
                  'superset_exercise']


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['id', 'name', 'description', 'sequence', 'duration', 'link_to_image', 'link_to_thumbnail', 'types']


class ProgramWorkoutRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramWorkoutRoutine
        fields = ['id', 'program', 'workout', 'sequence', 'day_number', 'day_of_the_week']
