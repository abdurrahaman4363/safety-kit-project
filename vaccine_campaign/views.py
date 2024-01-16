   
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,FormView
from .models import Review, Campaign, Vaccine, DoseBooking, AvailableTime
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import VaccineForm,DoseBookingForm,CampaignReviewForm
from django.views.generic import ListView,UpdateView, DeleteView,CreateView
from datetime import timedelta
from django.contrib import messages



class VaccineCreateView(CreateView):
    model = Vaccine
    form_class = VaccineForm
    template_name = 'vaccine_create.html'
    success_url = reverse_lazy('vaccine_list')
    

    def form_valid(self, form):
        messages.success(self.request, 'Successfully Successfully Added Vaccine.')
        form.instance.user_account = self.request.user.account
        return super().form_valid(form)

class VaccineListView(ListView):
    model = Vaccine
    template_name = 'vaccine_list.html'
    context_object_name = 'vaccine_list'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class VaccineUpdateView(UpdateView):
    model = Vaccine
    form_class = VaccineForm
    template_name = 'vaccine_update.html'
    success_url = reverse_lazy('vaccine_list')

    def form_valid(self, form):
        messages.success(self.request, 'Successfully Upadate Vaccine.')
        return super().form_valid(form)

class VaccineDeleteView(DeleteView):
    model = Vaccine
    template_name = 'vaccine_confirm_delete.html'
    success_url = reverse_lazy('vaccine_list')

    def form_valid(self, form):
        messages.success(self.request, 'Successfully Deleted Vaccine.')
        return super().form_valid(form)


class DoseBookingListView(LoginRequiredMixin, ListView):
    model = DoseBooking
    template_name = 'dosebooking_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return DoseBooking.objects.filter(patient=self.request.user)


class DoseBookingCreateView(LoginRequiredMixin, CreateView):
    model = DoseBooking
    form_class = DoseBookingForm
    template_name = 'dosebooking.html'
    success_url = reverse_lazy('dosebooking_list')

    def form_valid(self, form):
        messages.success(self.request, 'Booking Successful.')
        form.instance.patient = self.request.user
        form.instance.second_dose = form.instance.first_dose.date + timedelta(days=21)
        return super().form_valid(form)

class CampaignReviewView(LoginRequiredMixin, FormView):
    template_name = "campaign_review.html"
    form_class = CampaignReviewForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        campaign = Campaign.objects.get(pk=self.kwargs["pk"])
        reviewer = self.request.user
        new_comment = form.save(commit=False)
        new_comment.campaign = campaign
        new_comment.reviwer = reviewer
        new_comment.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        campaign = Campaign.objects.get(pk=self.kwargs["pk"])
        reviews = campaign.reviews.all()
        comment_form = kwargs.get("form", CampaignReviewForm())
        context["reviews"] = reviews
        context["comment_form"] = comment_form
        return context
        
            