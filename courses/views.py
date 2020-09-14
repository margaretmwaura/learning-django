from django.shortcuts import render, get_object_or_404, redirect

from django.views import View
# Create your views here.

from .models import Course

from .forms import CourseModelForm

class CourseObjectMixin(object):
    model = Course

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj

class CourseDeleteView(CourseObjectMixin, View):
    template_name = 'courses/course_delete.html'

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        print(obj)
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/')
        return render(request, self.template_name, context)

class CourseUpdateView(CourseObjectMixin, View):
    template_name = 'courses/course_update.html'

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if object is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)


class CourseCreateView(View):
    template_name = 'courses/course_create.html'
    # The fact that the id has been given a value of none .. it means that id is not a required parameter
    def get(self, request, *args, **kwargs):
        form = CourseModelForm()
        context = {"form" : form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {"form" : form}
        return render(request, self.template_name, context)

class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'object_list' : self.get_queryset()})

class CourseView(View):
    template_name = 'courses/course_detail.html'
    # The fact that the id has been given a value of none .. it means that id is not a required parameter
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)