from django.urls import path
from .views import (UserJobsListView,
                    JobCreateView,
                    JobUpdateView,
                    JobDetailView,
                    JobDeleteView,
                    SearchView,
                    EmployerJobsView)


urlpatterns = [
    path('', UserJobsListView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='job-search'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('job/new/', JobCreateView.as_view(), name='job-create'),
    path('job/<int:pk>/update/', JobUpdateView.as_view(), name='job-update'),
    path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='job-delete'),
    path('user-jobs/<int:creator>/', EmployerJobsView.as_view(), name='user-jobs'),
]
