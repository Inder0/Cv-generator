from django.shortcuts import render
from django.views.generic import CreateView,ListView
from .models import Profile
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
import io
# Create your views here.

class CreateProfileView(LoginRequiredMixin,CreateView):
    model=Profile
    fields = [
        'name', 'email', 'phone', 'degree',
        'school', 'university', 'summary',
        'previous_work', 'skills'
    ]
    template_name='myapp/accept.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)
    
class ProfileDashboardView(ListView):
    model=Profile
    template_name='myapp/dashboard.html'
    context_object_name='object_list'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Profile.objects.filter(user=self.request.user).order_by('-created_at')
        return Profile.objects.none()

@login_required
def delete_profile_redirect(request, pk):
    profile = get_object_or_404(Profile, pk=pk, user=request.user)
    profile.delete()
    return redirect('home')

@login_required
def resume(request, pk):
    profile = get_object_or_404(Profile, pk=pk, user=request.user)
    skills_list = []
    if profile.skills:
        skills_list = [skill.strip() for skill in profile.skills.split(',')]
    return render(request, 'myapp/resume.html', {
        'profile': profile,
        'skills_list': skills_list
    })

@login_required
def download_resume(request,pk):
    profile=get_object_or_404(Profile,pk=pk,user=request.user)
    template_path='myapp/download.html'
    context={'profile':profile}
    template=get_template(template_path)
    html=template.render(context)
    response=HttpResponse(content_type='applucation/pdf')
    response['Content-Disposition']=f'attachment; filename={profile.name}_CV.pdf'
    pisa_status=pisa.CreatePDF(io.BytesIO(html.encode('UTF-8')),dest=response,encoding='UTF-8')
    if pisa_status.err:
        return HttpResponse('Error generating PDF',status=500)
    return response