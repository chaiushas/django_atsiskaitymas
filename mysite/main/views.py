from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .models import Project, Client
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

def index(request):
    count_projects = Project.objects.all().count()
    count_clients = Client.objects.all().count()

    context = {
        'count_projects': count_projects,
        'count_clients': count_clients,
    }
    return render(request, 'index.html', context=context)


class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser


class ProjectListView(SuperUserRequiredMixin, generic.ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'
    paginate_by = 6


class ProjectDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = Project
    template_name = 'project.html'
    context_object_name = 'project'

    def test_func(self):
        self.object = self.get_object()
        if self.request.user == self.object.in_charge or self.request.user.is_superuser:
            return True
        return False


class MyProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    template_name ='user_projects.html'
    context_object_name = 'projects'
    paginate_by = 10

    def get_queryset(self):
        return Project.objects.filter(in_charge=self.request.user).order_by('date_end')

# Registracija
@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'registration/register.html')