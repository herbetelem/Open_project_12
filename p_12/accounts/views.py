from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserThemeForm
from .models import UserTheme, UserRole
from .serializers import UserRoleSerializer, UserThemeSerializer
from rest_framework import status, viewsets


from accounts.forms import RegistrationForm
from .permission import CheckRolePermission
from rest_framework.permissions import IsAuthenticated

# Create your views here.


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
            else:
                return render(request, 'registration/login.html', {})
        else:
            return render(request, 'registration/login.html', {})
    else:
        return redirect('home_page')

def logout_view(request):
    logout(request)
    return redirect('home_page')

def register_view(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect("login_view")
        else:
            return render(
                request, 'registration/register.html',
                {"user_form": user_form})
    else:
        user_form = RegistrationForm()
        return render(
            request, 'registration/register.html',
            {"user_form": user_form})

@login_required(login_url='/login/')
def profile_page(request, id: int):
    instance = get_object_or_404(UserTheme, user=request.user)
    if request.method == "POST":
        form = UserThemeForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('profile_page', request.user.id)
    form = UserThemeForm(instance=instance)
    user = get_object_or_404(User, id=id)
    context = {
        'user': user,
        'form': form,
    }
    if request.user.is_authenticated:
        context['theme'] = get_object_or_404(UserTheme, user=request.user)
    return render(request, 'profile_page.html', context)

def home_page(request):
    context = {}
    if request.user.is_authenticated:
        context['theme'] = get_object_or_404(UserTheme, user=request.user)
        return render(request, 'global/home.html', context)
    return render(request, 'global/home.html', context)

class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

    permission_classes = [IsAuthenticated, CheckRolePermission]

class UserThemeViewSet(viewsets.ModelViewSet):
    queryset = UserTheme.objects.all()
    serializer_class = UserThemeSerializer

    permission_classes = [IsAuthenticated, CheckRolePermission]
