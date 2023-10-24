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


class IdAndNameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'alternative_name']


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id', 'name', 'alternative_name', 'description', 'type', 'link_to_image', 'link_to_thumbnail']


class MuscleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscle
        fields = ['id', 'name', 'alternative_name', 'description', 'type', 'link_to_image', 'link_to_thumbnail']


class ExerciseMuscleSerializer(IdAndNameSerializer):
    class Meta(IdAndNameSerializer.Meta):
        model = Muscle


class ExerciseEquipmentSerializer(serializers.ModelSerializer):
    class Meta(IdAndNameSerializer.Meta):
        model = Equipment


class ExerciseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseType
        fields = ['id', 'name']


class ExerciseSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'alternative_name', 'description', 'difficulty', 'compound_movement',
                  'link_to_image', 'link_to_thumbnail', 'link_to_video']


class ExerciseDetailedSerializer(ExerciseSimpleSerializer):
    main_muscle = ExerciseMuscleSerializer()
    secondary_muscles = ExerciseMuscleSerializer(many=True)
    equipments = ExerciseEquipmentSerializer(many=True)
    types = ExerciseTypeSerializer(many=True)

    class Meta(ExerciseSimpleSerializer.Meta):
        fields = [*ExerciseSimpleSerializer.Meta.fields, 'main_muscle', 'secondary_muscles', 'equipments', 'types']


class TrainingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingType
        fields = ['id', 'name']


class ExerciseWorkoutSerializer(IdAndNameSerializer):
    class Meta(IdAndNameSerializer.Meta):
        model = Exercise


class WorkoutExerciseRoutineSerializer(serializers.ModelSerializer):
    exercise = ExerciseWorkoutSerializer()
    superset_exercise = ExerciseWorkoutSerializer()

    class Meta:
        model = WorkoutExerciseRoutine
        fields = ['id', 'exercise', 'min_sets', 'max_sets', 'min_reps', 'max_reps', 'tempo_eccentric',
                  'tempo_pause_1', 'tempo_concentric', 'tempo_pause_2', 'min_rir', 'max_rir', 'superset',
                  'superset_exercise']


class WorkoutSerializer(serializers.ModelSerializer):
    type = TrainingTypeSerializer()

    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'variant', 'type', 'target', 'link_to_image', 'link_to_thumbnail']


class WorkoutWithRoutinesSerializer(WorkoutSerializer):
    exercise_routines = WorkoutExerciseRoutineSerializer(many=True, source='workoutexerciseroutine_set')

    class Meta(WorkoutSerializer.Meta):
        fields = [*WorkoutSerializer.Meta.fields, 'exercise_routines']


class ProgramWorkoutNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'name']


class ProgramWorkoutRoutineSerializer(serializers.ModelSerializer):
    workout = ProgramWorkoutNameSerializer()

    class Meta:
        model = ProgramWorkoutRoutine
        fields = ['id', 'workout', 'sequence', 'day_number', 'day_of_the_week']


class ProgramSerializer(serializers.ModelSerializer):
    types = TrainingTypeSerializer(many=True)

    class Meta:
        model = Program
        fields = ['id', 'name', 'description', 'sequence', 'duration', 'link_to_image', 'link_to_thumbnail', 'types']


class ProgramWithRoutinesSerializer(ProgramSerializer):
    workout_routines = ProgramWorkoutRoutineSerializer(many=True, source='programworkoutroutine_set')

    class Meta(ProgramSerializer.Meta):
        fields = [*ProgramSerializer.Meta.fields, 'workout_routines']
