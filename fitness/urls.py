from django.urls import path
from .views import equipments, muscles, exercises, workouts, programs

urlpatterns = [
    path('equipments/', equipments.equipment_list),
    path('equipments/<uuid:equipment_id>/', equipments.equipment_detail),
    path('muscles/', muscles.muscle_list),
    path('muscles/<uuid:muscle_id>/', muscles.muscle_detail),
    path('exercises/', exercises.exercise_list_simple),
    path('exercises/detail/', exercises.exercise_list_detail),
    path('exercises/<uuid:exercise_id>/', exercises.exercise_detail),
    path('workouts/', workouts.workout_list_simple),
    path('workouts/routines/', workouts.workout_list_with_routines),
    path('workouts/<uuid:workout_id>/', workouts.workout_detail),
    path('workouts/routines/<uuid:workout_id>/', workouts.workout_detail_with_routines),
    path('programs/', programs.program_list),
    path('programs/<uuid:program_id>/', programs.program_detail),
]
