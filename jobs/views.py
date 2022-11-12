from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db import transaction, IntegrityError

from .models import Job
from .forms import JobForm


class JobsListView(ListView):
    model = Job
    template_name = 'jobs/home.html'
    context_object_name = 'jobs'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        jobs = Job.objects.all().order_by("-date_added")

        context_data['jobs'] = jobs
        context_data['number_of_jobs'] = len(jobs)
        return context_data


class SearchView(JobsListView):
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        query = self.request.GET.get('search').lower()
        if query:
            jobs = Job.objects.all().order_by('-date_added')
            search_result = []
            for job in jobs:
                if query in job.title.lower() or query in job.company_name.lower() or query in job.description.lower():
                    search_result.append(job)
        else:
            search_result = []

        context_data['jobs'] = search_result
        context_data['number_of_jobs'] = len(search_result)
        return context_data


class EmployerJobsView(JobsListView):
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        user = self.request.user
        if user:
            search_result = Job.objects.filter(creator=user).order_by('-date_added')
        else:
            search_result = []

        context_data['jobs'] = search_result
        context_data['number_of_jobs'] = len(search_result)
        return context_data


class JobDetailView(DetailView):
    model = Job


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = JobForm

    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                super().post(request, *args, **kwargs)
        except IntegrityError:
            print("Integrity error in JobCreateView")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    fields = ['title', 'company_name', 'location', 'contact_info', 'description']

    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                super().post(request, *args, **kwargs)
        except IntegrityError:
            print("Integrity error in JobUpdateView")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        job = self.get_object()
        return self.request.user == job.creator


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job

    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                super().post(request, *args, **kwargs)
        except IntegrityError:
            print("Integrity error in JobDeleteView")

    def test_func(self):
        job = self.get_object()
        return self.request.user == job.creator

    def get_success_url(self):
        return reverse('home')
