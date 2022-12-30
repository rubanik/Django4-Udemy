from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    TemplateView, 
    FormView, 
    CreateView, 
    ListView, 
    DetailView, 
    UpdateView,
    DeleteView
)

from classroom.forms import ContactForm
from classroom.models import Teacher


class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankYouView(TemplateView):
    template_name = 'classroom/thankyou.html'


class TeacherCreateView(CreateView):
    model = Teacher  # connect to a model
    fields = '__all__'  # decide what field need to show
    # decide what to do in case of succes
    success_url = reverse_lazy('classroom:thankyou')


class TeacherListView(ListView):
    # model_list.html
    model = Teacher
    queryset = Teacher.objects.order_by('first_name')
    content_object_name = 'teacher_list'


class TeacherDetailView(DetailView):
    # Return only one model entity
    # model_detail.html
    model = Teacher


class TeacherUpdateView(UpdateView):
    # SHARE create view model
    model = Teacher
    fields = ['last_name','first_name','subject'] # specify fields to update ('__all__' for all field updatinh)
    success_url = reverse_lazy('classroom:list_teacher')


class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('classroom:list_teacher')



class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # succes URL?
    # It's not a template! It's an URL!
    success_url = reverse_lazy('classroom:thankyou')

    # what to do with form
    def form_valid(self, form):
        print(form.cleaned_data)

        return super().form_valid(form)
