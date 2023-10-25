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
router.register('equipments', EquipmentViewSet)
router.register('muscles', MuscleViewSet)
router.register('exercises', ExerciseSimpleViewSet)
router.register('exercises-detailed', ExerciseDetailedViewSet)
router.register('workouts', WorkoutViewSet)
router.register('workouts-routines', WorkoutWithRoutinesViewSet)
router.register('programs', ProgramViewSet)
router.register('programs-routines', ProgramWithRoutinesViewSet)

urlpatterns = router.urls
