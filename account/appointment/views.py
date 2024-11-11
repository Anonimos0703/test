# appointment/views.py
from django.contrib import messages
from .forms import AppointmentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Appointment

def appointment_view(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user  # Associate the logged-in user with the appointment
            appointment.save()
            messages.success(request, 'Appointment booked successfully!')
            # Redirect to the appointment list in the other app
            return redirect('appointment_list')  # Make sure 'appointment_list' is the correct URL name

    context = {
        'form': form
    }
    return render(request, 'appointment.html', context)
 


# Helper function to check if user is admin
def is_admin(user):
    return user.is_staff

# View for admin to see all appointments
@login_required
@user_passes_test(is_admin)
def admin_appointment_list(request):
    appointments = Appointment.objects.all()  # Fetch all appointments
    return render(request, 'admin_appointment_list.html', {'appointments': appointments})

# View for admin to update a specific appointment
@login_required
@user_passes_test(is_admin)
def admin_appointment_update(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('admin_appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    
    return render(request, 'appointment/admin_appointment_update.html', {'form': form, 'appointment': appointment})
