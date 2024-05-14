from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import Project,Issue  # Import your Project model
from django.apps import apps
from django.core import serializers
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm
        if request.method =='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Hello {user}, Registration successful. Please log in.')
                return redirect('login')  # Redirect to the login page
        context = {'form': form}    
        return render(request, 'users/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request,'Username or Password is incorrect')
        context = {}
        return render(request, 'users/login.html', context)

def logoutView(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request,'users/home.html')

def get_user_list(request):
    users = User.objects.all()  # Fetch all users from the database
    user_data = [{'username': user.username,'id':user.id} for user in users]  # Extract username from each user object
    return JsonResponse(user_data, safe=False)

@csrf_exempt  # Disable CSRF protection (for demonstration, use appropriate protection in production)
def add_project(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')

        # Create a new project object and save it to the database
        project = Project.objects.create(name=project_name)

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
    
@csrf_exempt
def get_project_list(request):
    if request.method == 'GET':
        projects = Project.objects.all()  # Assuming you have a Project model
        project_list = list(projects.values('id', 'name'))  # Replace 'id', 'name' with actual fields of your Project model
        return JsonResponse(project_list, safe=False)
    else:
        return JsonResponse({"error": "Only GET method is allowed"}, status=400)

@csrf_exempt
def get_issue_list(request):
    if request.method == 'GET':
        issues = Issue.objects.all()

        # Serialize queryset to list of dictionaries
        data = [
            {
                'project': issue.project.name,  # Access related project's name
                'module': issue.module,
                'issue_type': issue.issue_type,
                'problem': issue.problem,
                'assigned_to': issue.assigned_to.username,  # Access related user's username
                'created_at': issue.created_at
            }
            for issue in issues
        ]

        # Return JsonResponse with the serialized data
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({"error": "Only GET method is allowed"}, status=400)
@csrf_exempt    
def add_issue(request):
    if request.method == 'POST':
        # Retrieve form data from AJAX POST request
        project_id = request.POST.get('project_id')
        issue_type = request.POST.get('issue_type')
        module = request.POST.get('module')
        problem = request.POST.get('problem')
        assigned_to_id = request.POST.get('assigned_to')

        # Retrieve Project instance based on project_id
        project = get_object_or_404(Project, pk=project_id)

        # Retrieve User instance based on assigned_to_id
        assigned_to = get_object_or_404(User, pk=assigned_to_id)

        # Create the Issue instance with validated data
        issue = Issue.objects.create(
            project=project,
            issue_type=issue_type,
            module=module,
            problem=problem,
            assigned_to=assigned_to
        )

        # Return a success response
        return JsonResponse({'status': 'success', 'message': 'Issue added successfully'})
    
    # Handle other HTTP methods or invalid requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)