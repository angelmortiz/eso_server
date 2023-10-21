from django.contrib import admin
from . import models

DISPLAY_LIST_PER_PAGE = 25


@admin.register(models.Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'alternative_name', 'type']
    list_filter = ['type']
    list_per_page = DISPLAY_LIST_PER_PAGE
    search_fields = ['name__istartswith']


@admin.register(models.Muscle)
class MuscleAdmin(admin.ModelAdmin):
    list_display = ['name', 'alternative_name', 'type']
    list_filter = ['type']
    list_per_page = DISPLAY_LIST_PER_PAGE
    search_fields = ['name__istartswith']


@admin.register(models.ExerciseType)
class ExerciseTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = DISPLAY_LIST_PER_PAGE
    search_fields = ['name__istartswith']


@admin.register(models.Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    autocomplete_fields = ['main_muscle']
    list_display = ['name', 'alternative_name', 'difficulty', 'compound_movement']
    list_editable = ['difficulty', 'compound_movement']
    list_filter = ['main_muscle', 'difficulty', 'compound_movement', 'types', 'equipments']
    list_select_related = ['main_muscle']
    list_per_page = DISPLAY_LIST_PER_PAGE
    search_fields = ['name__istartswith']


@admin.register(models.TrainingType)
class TrainingTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = DISPLAY_LIST_PER_PAGE
    search_fields = ['name__istartswith']


class WorkoutExerciseRoutineInline(admin.TabularInline):
    autocomplete_fields = ['workout', 'exercise', 'superset_exercise']
    model = models.WorkoutExerciseRoutine
    extra = 0


@admin.register(models.Workout)
class WorkoutAdmin(admin.ModelAdmin):
    inlines = [WorkoutExerciseRoutineInline]
    list_display = ['name', 'variant', 'target', 'type']
    list_editable = ['variant', 'target']
    list_filter = ['type', 'target']
    list_select_related = ['type']
    list_per_page = DISPLAY_LIST_PER_PAGE
    search_fields = ['name__istartswith', 'variant__istartswith']


@admin.register(models.WorkoutExerciseRoutine)
class WorkoutExerciseRoutineAdmin(admin.ModelAdmin):
    autocomplete_fields = ['workout', 'exercise', 'superset_exercise']
    list_display = ['id', 'workout', 'exercise', 'min_sets', 'max_sets', 'min_reps', 'max_reps', 'superset']
    list_editable = ['min_sets', 'max_sets', 'min_reps', 'max_reps', 'superset']
    list_select_related = ['workout', 'exercise', 'superset_exercise']
    list_per_page = DISPLAY_LIST_PER_PAGE


class ProgramWorkoutRoutineInline(admin.TabularInline):
    autocomplete_fields = ['program', 'workout']
    model = models.ProgramWorkoutRoutine
    extra = 0


@admin.register(models.Program)
class ProgramAdmin(admin.ModelAdmin):
    inlines = [ProgramWorkoutRoutineInline]
    list_display = ['name', 'sequence', 'duration']
    list_editable = ['sequence', 'duration']
    list_filter = ['sequence', 'duration', 'types']
    list_per_page = DISPLAY_LIST_PER_PAGE
    search_fields = ['name__istartswith']


@admin.register(models.ProgramWorkoutRoutine)
class ProgramWorkoutRoutineAdmin(admin.ModelAdmin):
    autocomplete_fields = ['program', 'workout']
    list_display = ['id', 'program', 'workout', 'sequence', 'day_number', 'day_of_the_week']
    list_editable = ['sequence', 'day_number', 'day_of_the_week']
    list_select_related = ['program', 'workout']
    list_per_page = DISPLAY_LIST_PER_PAGE
