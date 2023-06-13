from django.urls import path
from .views import (
    QuizListView,
    quiz_view,
    quiz_data_view,
    save_quiz_view,
    over,
    redirect,
    new_data,
    # get_image
    
)

app_name = 'quizes'

urlpatterns = [
    path('', QuizListView, name='main-view'),
    path(f'<int:id>/', quiz_view, name='quiz-view'),
    path(f'<int:id>/save/', save_quiz_view, name='save-view'),
    path(f'<int:id>/data/', quiz_data_view, name='quiz-data-view'),
    path(f'sign-up/',over,name='sign-up'),
    path(f'redirect/',redirect,name='redirect'),
    path(f'file_data/',new_data,name='file_data'),
    # path('image/',get_image,name='image')
    # path(f'quiz/',quiz_automate)
]
