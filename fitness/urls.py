from rest_framework.routers import DefaultRouter
from .views import (
    EquipmentViewSet,
    MuscleViewSet,
    ExerciseSimpleViewSet,
    ExerciseDetailedViewSet,
    WorkoutViewSet,
    WorkoutWithRoutinesViewSet,
    ProgramViewSet,
    ProgramWithRoutinesViewSet)

router = DefaultRouter()
router.register(r'equipments', EquipmentViewSet)
router.register(r'muscles', MuscleViewSet)
router.register(r'exercises', ExerciseSimpleViewSet)
router.register(r'exercises-detailed', ExerciseDetailedViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'workouts-routines', WorkoutWithRoutinesViewSet)
router.register(r'programs', ProgramViewSet)
router.register(r'programs-routines', ProgramWithRoutinesViewSet)

urlpatterns = router.urls
