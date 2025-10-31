from django.shortcuts import render


# Create your views here.
def home(request):
    template_data = {}
    template_data["title"] = "LIRR Page"
    template_data["selected_page"] = "LIRR"
    return render(request, "home/index.html", {"template_data": template_data})


def mnr(request):
    template_data = {}
    template_data["title"] = "MNR Page"
    template_data["selected_page"] = "MNR"
    return render(request, "home/mnr.html", {"template_data": template_data})
