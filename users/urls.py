from django.urls import path
from.import views
import uuid
import random
def generate_token():
    val=str(uuid.uuid4())
    token=random.sample(val,20)
    join_token=''.join(token)
    return join_token

urlpatterns=[
    path(f'login/',views.sign_in,name='login'),
    path('register/',views.sign_up,name='register'),
    # path('logout/',views.sign_out,name='logout'),
    # path('reset/',views.reset_account,name='reset'),
    # path('profile/',views.profile,name='profile'),
    path('update_user/',views.reset_account,name='update_user'),
]