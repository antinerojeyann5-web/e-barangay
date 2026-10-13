from django.shortcuts import render, redirect, get_object_or_404
from .models import Resident, DocumentRequest, Announcement, Complaint, Guide
from .forms import ResidentRegisterForm, DocumentRequestForm, ComplaintForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# NEW: Welcome Page (shown first to visitors)
def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    query = request.GET.get('q')
    if query:
        residents_list = Resident.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
    else:
        residents_list = Resident.objects.all()
    announcements = Announcement.objects.all().order_by('-date_posted')[:3]
    return render(request, 'home.html', {'residents': residents_list, 'announcements': announcements, 'query': query})

def add_resident(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        contact_number = request.POST.get('contact_number')
        Resident.objects.create(first_name=first_name, last_name=last_name, age=age, address=address, contact_number=contact_number)
        return redirect('home')
    return render(request, 'add_resident.html')

def edit_resident(request, resident_id):
    resident = get_object_or_404(Resident, id=resident_id)
    if request.method == 'POST':
        resident.first_name = request.POST.get('first_name')
        resident.last_name = request.POST.get('last_name')
        resident.age = request.POST.get('age')
        resident.address = request.POST.get('address')
        resident.contact_number = request.POST.get('contact_number')
        resident.save()
        return redirect('home')
    return render(request, 'edit_resident.html', {'resident': resident})

def delete_resident(request, resident_id):
    resident = get_object_or_404(Resident, id=resident_id)
    resident.delete()
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = ResidentRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = ResidentRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def resident_dashboard(request):
    resident_profile = Resident.objects.filter(first_name__iexact=request.user.username).first()
    my_requests = DocumentRequest.objects.filter(user=request.user).order_by('-date_requested')
    my_complaints = Complaint.objects.filter(user=request.user).order_by('-date_submitted')
    context = {'my_requests': my_requests, 'my_complaints': my_complaints, 'resident_profile': resident_profile}
    return render(request, 'resident_dashboard.html', context)

@login_required
def request_document(request):
    if request.method == 'POST':
        form = DocumentRequestForm(request.POST)
        if form.is_valid():
            doc_request = form.save(commit=False)
            doc_request.user = request.user
            doc_request.save()
            return redirect('resident_dashboard')
    else:
        form = DocumentRequestForm()
    return render(request, 'request_document.html', {'form': form})

@login_required
def submit_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            return redirect('resident_dashboard')
    else:
        form = ComplaintForm()
    return render(request, 'submit_complaint.html', {'form': form})

def announcement_list(request):
    announcements = Announcement.objects.all().order_by('-date_posted')
    return render(request, 'announcements.html', {'announcements': announcements})

def guide_list(request):
    guides = Guide.objects.all().order_by('title')
    return render(request, 'guide.html', {'guides': guides})