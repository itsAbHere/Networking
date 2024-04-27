from django.contrib import admin
from django.urls import path
from Sendit.views import upload_file, file_list, index, upload_success

urlpatterns = [
    # URL for the home view
    path('', index, name='index'), 
    # URL to handle file uploads
    path('upload_success/', upload_success, name='upload_success'),
    path('upload/', upload_file, name='upload_file'),
    # URL to display the list of uploaded files
    path('files/', file_list, name='file_list'),
    # Admin URL
    path('admin/', admin.site.urls),
]
