from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView
from .models import Profile
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
import io
from .utils import get_skills_and_strengths,parse_text
from .forms import ProfileForm
# Create your views here.

class CreateProfileView(LoginRequiredMixin,CreateView):
    model=Profile
    form_class=ProfileForm
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
            qs = Profile.objects.filter(user=self.request.user).order_by('-created_at')
        else:
            return Profile.objects.none()
        query = self.request.GET.get('q') 
        if query:
            qs = qs.filter(name__icontains=query)
        return qs

class UpdateProfileView(LoginRequiredMixin,UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'myapp/accept.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        obj = get_object_or_404(Profile, id=self.kwargs['pk'])
        if obj.user != self.request.user:
            raise PermissionError("Not allowed")
        return obj
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
@login_required
def delete_profile_redirect(request, pk):
    profile = get_object_or_404(Profile, pk=pk, user=request.user)
    if request.method == "POST":
        profile.delete()
        return redirect('home')

    return render(request, 'myapp/delete_confirm.html', {'profile': profile})

@login_required
def resume(request, pk):
    profile = get_object_or_404(Profile, pk=pk, user=request.user)
    skills_list,strengths=get_skills_and_strengths(profile.skills)

    return render(request, 'myapp/resume.html', {
        'profile': profile,
        'skills_list': skills_list,
        'strengths':strengths
    })

@login_required
def download_resume(request,pk):
    profile=get_object_or_404(Profile,pk=pk,user=request.user)
    template_path='myapp/download.html'
    skills_list,strengths=get_skills_and_strengths(profile.skills)
    experience = parse_text(profile.previous_work)
    context={'profile':profile,'skills_list':skills_list,'strengths':strengths,'experience':experience,}
    template=get_template(template_path)
    html=template.render(context)
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']=f'attachment; filename={profile.name}_CV.pdf'
    pisa_status=pisa.CreatePDF(io.BytesIO(html.encode('UTF-8')),dest=response,encoding='UTF-8')
    if pisa_status.err:
        return HttpResponse('Error generating PDF',status=500)
    return response