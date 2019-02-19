from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from milestones.forms import MilestoneFormModel
from milestones.models import Milestone


class HomeView(TemplateView):
    template_name = 'milestones/index.html'

    def get_context_data(self, **kwargs):
        milestones = Milestone.objects.all()

        return dict(milestones=milestones)


class MilestoneView(TemplateView):
    template_name = 'milestones/milestone.html'

    def get_context_data(self, **kwargs):
        milestone = get_object_or_404(Milestone, pk=kwargs['id'])

        return dict(milestone=milestone)


class NewMilestoneView(View):
    template_name = 'milestones/new.html'

    def post(self, request, *args, **kwargs):
        form = MilestoneFormModel(request.POST)

        if form.is_valid():
            form.save()
            return redirect('milestones:index')
        else:
            return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):
        form = MilestoneFormModel(request.POST or None)

        return render(request, self.template_name, {'form': form})
