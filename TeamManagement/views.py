from django.shortcuts import render, redirect

from .models import TeamMember
from .forms import TeamMemberForm


def index(request):
    return render(request, 'TeamManagement/index.html',
                  {'team_members': TeamMember.objects.all()})


def add_member(request):
    # https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/#the-save-method
    if request.method == 'POST':
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        pass
    else:
        form = TeamMemberForm()
    return render(request, 'TeamManagement/add-member.html', {'form': form})


def edit_member(request, pk):
    team_member = TeamMember.objects.get(pk=pk)
    if request.method == 'POST':
        if 'delete' in request.POST:
            team_member.delete()
            return redirect('index')
        form = TeamMemberForm(request.POST, instance=team_member)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TeamMemberForm(instance=team_member)
    return render(request, 'TeamManagement/edit-member.html', {'form': form})
