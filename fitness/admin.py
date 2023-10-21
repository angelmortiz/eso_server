from django.contrib import admin
from . import models

DISPLAY_LIST_PER_PAGE = 25


@admin.register(models.Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'alternative_name', 'type']
    list_per_page = DISPLAY_LIST_PER_PAGE


@admin.register(models.Muscle)
class MuscleAdmin(admin.ModelAdmin):
    list_display = ['name', 'alternative_name', 'type']
    list_per_page = DISPLAY_LIST_PER_PAGE


@admin.register(models.ExerciseType)
class ExerciseTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = DISPLAY_LIST_PER_PAGE


@admin.register(models.Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'alternative_name', 'difficulty', 'compound_movement']
    list_editable = ['difficulty', 'compound_movement']
    list_per_page = DISPLAY_LIST_PER_PAGE


@admin.register(models.TrainingType)
class TrainingTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = DISPLAY_LIST_PER_PAGE


@admin.register(models.ExercisePlan)
class ExercisePlanAdmin(admin.ModelAdmin):
    list_display = ['exercise', 'min_sets', 'max_sets', 'min_reps', 'max_reps', 'superset']
    list_editable = ['min_sets', 'max_sets', 'min_reps', 'max_reps', 'superset']
    list_per_page = DISPLAY_LIST_PER_PAGE


@admin.register(models.Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'variant', 'type', 'target']
    list_editable = ['variant', 'type', 'target']
    list_per_page = DISPLAY_LIST_PER_PAGE


@admin.register(models.WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ['workout', 'day_number', 'day_of_the_week']
    list_editable = ['day_number', 'day_of_the_week']
    list_per_page = DISPLAY_LIST_PER_PAGE


@admin.register(models.Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'sequence', 'duration']
    list_editable = ['sequence', 'duration']
    list_per_page = DISPLAY_LIST_PER_PAGE
