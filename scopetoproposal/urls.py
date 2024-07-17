from django.urls import path

from scopetoproposal import views

from scopetoproposal.views import FileUploadView


urlpatterns = [
    path('test/', views.test),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('upload-page/', views.upload_page, name='upload-page'),
]