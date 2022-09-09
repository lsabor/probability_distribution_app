from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from distributions.models import NormalDist, ProbabilityDistribution
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

import json


def home(request):
    return redirect(reverse("home"))


def index(request):

    probdists = ProbabilityDistribution.objects.all()

    context = {
        "probdists": probdists,
    }

    return render(request, "index.html", context)


def probdist(request, id):
    # A lot of this work should be done by the front end to parse a distribution into something
    # that looks nice to display
    # for proof of concept, I'll parse some of the data here to show how I think about
    # how it will ultimately work
    dist = ProbabilityDistribution.objects.get(id=id)
    normdists = dist.normal_distributions.all()

    context = {
        "dist": dist,
        "data": json.dumps(dist.get_data()),
        "normdists": normdists,
    }

    return render(request, "display_probdist.html", context)


@require_POST
@csrf_exempt
def update_probdist(request, id):
    dist = ProbabilityDistribution.objects.get(id=id)

    dist.name = request.POST["name"]
    dist.xaxis_name = request.POST["xaxis_name"]
    dist.lower_bound = float(request.POST["lower_bound"])
    dist.upper_bound = float(request.POST["upper_bound"])

    dist.save()

    return redirect(reverse("home") + id)


@require_POST
@csrf_exempt
def delete_probdist(request, id):
    dist = ProbabilityDistribution.objects.get(id=id)
    dist.delete()

    return redirect(reverse("home"))


@require_POST
@csrf_exempt
def create_normdist(request, id):
    dist = ProbabilityDistribution.objects.get(id=id)

    data = request.POST.dict()
    data["mean"] = float(data["mean"])
    data["std"] = float(data["std"])
    data["weight"] = float(data["weight"])
    data["probabilitydistribution"] = dist

    new_normdist = NormalDist.objects.create(**data)

    return redirect(reverse("home") + id)


@require_POST
@csrf_exempt
def update_normdist(request, id, dist_id):

    normdist = NormalDist.objects.get(id=dist_id)

    data = request.POST
    normdist.mean = float(data["mean"])
    normdist.std = float(data["std"])
    normdist.weight = float(data["weight"])
    normdist.save()

    return redirect(reverse("home") + id)


@require_POST
@csrf_exempt
def delete_normdist(request, id, dist_id):

    normdist = NormalDist.objects.get(id=dist_id)
    normdist.delete()

    return redirect(reverse("home") + id)


def create_page(request):
    new_distribution = ProbabilityDistribution.objects.create(
        name="Distribution Name",
        xaxis_name="X Axis",
        lower_bound=0,
        upper_bound=1,
    )
    return redirect(reverse("home") + str(new_distribution.id))
