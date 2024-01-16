from django.shortcuts import render
from vaccine_campaign.models import Campaign
from vaccine_campaign.models import Review, Campaign
from vaccine_campaign.forms import CampaignReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View



class HomeView(View):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        campaigns = Campaign.objects.all()
        reviews = Review.objects.all()
        comment_form = CampaignReviewForm()

        context = {
            "campaigns": campaigns,
            "reviews": reviews,
            "comment_form": comment_form,
        }

        return render(request, self.template_name, context)