from django.shortcuts import render
from .forms import PersonalInformation, RoutingInformation, QueryForm
from .models import TransactionSummary

JSON_data = [
    {
        "openclose": "Open",
        "dept": "CS",
        "users": "A. Lester",
        "totalrefund": 0,
        "totalclaim": 1,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "LIRR",
    },
    {
        "openclose": "Open",
        "dept": "CS",
        "users": "CC Approval Letters",
        "totalrefund": 121,
        "totalclaim": 19,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "LIRR",
    },
    {
        "openclose": "Open",
        "dept": "CS",
        "users": "CC Claim over $100",
        "totalrefund": 0,
        "totalclaim": 11,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "LIRR",
    },
    {
        "openclose": "Open",
        "dept": "CS",
        "users": "Online Claims",
        "totalrefund": 0,
        "totalclaim": 54,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "LIRR",
    },
    {
        "openclose": "Open",
        "dept": "CS",
        "users": "R. Cabrera ",
        "totalrefund": 89,
        "totalclaim": 65,
        "totalchargeback": 33,
        "totalpa61": 0,
        "page": "LIRR",
    },
    {
        "openclose": "Open",
        "dept": "CS",
        "users": "S. Stephens",
        "totalrefund": 1,
        "totalclaim": 6,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "LIRR",
    },
    {
        "openclose": "Open",
        "dept": "CS",
        "users": "V. Kravtsov",
        "totalrefund": 35,
        "totalclaim": 15,
        "totalchargeback": 2,
        "totalpa61": 0,
        "page": "LIRR",
    },
    {
        "openclose": "Closed",
        "dept": "CS",
        "users": "CC Approval Letters",
        "totalrefund": 27,
        "totalclaim": 1,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "LIRR",
    },
    {
        "openclose": "Closed",
        "dept": "CS",
        "users": "CC Claim over $100",
        "totalrefund": 0,
        "totalclaim": 2,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "LIRR",
    },
    {
        "openclose": "Closed",
        "dept": "CS",
        "users": "Online Claims",
        "totalrefund": 0,
        "totalclaim": 3,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "LIRR",
    },
    {
        "openclose": "Closed",
        "dept": "CS",
        "users": "R. Cabrera ",
        "totalrefund": 41,
        "totalclaim": 36,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "LIRR",
    },
    {
        "openclose": "Closed",
        "dept": "CS",
        "users": "S. Stephens",
        "totalrefund": 0,
        "totalclaim": 4,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "LIRR",
    },
    {
        "openclose": "Closed",
        "dept": "CS",
        "users": "V. Kravtsov",
        "totalrefund": 5,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "LIRR",
    },
    {
        "openclose": "Open",
        "dept": "CTP",
        "users": "CTP Paid Folder",
        "totalrefund": 0,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 2,
        "page": "MNR",
    },
    {
        "openclose": "Open",
        "dept": "CTP",
        "users": "CTP-System",
        "totalrefund": 0,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 1,
        "page": "MNR",
    },
    {
        "openclose": "Open",
        "dept": "CTP",
        "users": "Deadbeat",
        "totalrefund": 0,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 834,
        "page": "MNR",
    },
    {
        "openclose": "Open",
        "dept": "CTP",
        "users": "Fare Not Paid Folder",
        "totalrefund": 0,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 204925,
        "page": "MNR",
    },
    {
        "openclose": "Open",
        "dept": "CTP",
        "users": "Illegible",
        "totalrefund": 0,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 2859,
        "page": "MNR",
    },
    {
        "openclose": "Open",
        "dept": "CTP",
        "users": "Letters Folder",
        "totalrefund": 0,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 4165,
        "page": "MNR",
    },
    {
        "openclose": "Open",
        "dept": "CTP",
        "users": "Letters Ret Undeliverable",
        "totalrefund": 0,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 1,
        "page": "MNR",
    },
    {
        "openclose": "Open",
        "dept": "CTP",
        "users": "Waived Folder",
        "totalrefund": 0,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 26,
        "page": "MNR",
    },
    {
        "openclose": "Closed",
        "dept": "CTP",
        "users": "CTP Paid Folder",
        "totalrefund": 0,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 3718,
        "page": "MNR",
    },
    {
        "openclose": "Closed",
        "dept": "CTP",
        "users": "Deadbeat",
        "totalrefund": 0,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 7,
        "page": "MNR",
    },
    {
        "openclose": "Closed",
        "dept": "CTP",
        "users": "Illegible",
        "totalrefund": 0,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 647,
        "page": "MNR",
    },
    {
        "openclose": "Closed",
        "dept": "CTP",
        "users": "Letters Folder",
        "totalrefund": 0,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 3245,
        "page": "MNR",
    },
    {
        "openclose": "Closed",
        "dept": "CTP",
        "users": "Waived Folder",
        "totalrefund": 0,
        "totalclaim": 1,
        "totalchargeback": 0,
        "totalpa61": 68,
        "page": "MNR",
    },
    {
        "openclose": "Open",
        "dept": "Mail And Ride",
        "users": "M R Cash Refund For Proces",
        "totalrefund": 2,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "LIRR",
    },
    {
        "openclose": "Closed",
        "dept": "Mail And Ride",
        "users": "I. Jones",
        "totalrefund": 1,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "LIRR",
    },
    {
        "openclose": "Closed",
        "dept": "Mail And Ride",
        "users": "M R Cash Refund For Proces",
        "totalrefund": 8,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "LIRR",
    },
    {
        "openclose": "Closed",
        "dept": "Mail And Ride",
        "users": "M. Panetta",
        "totalrefund": 1,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "LIRR",
    },
    {
        "openclose": "Closed",
        "dept": "Mail And Ride",
        "users": "T. Odermatt",
        "totalrefund": 1,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "LIRR",
    },
    {
        "openclose": "Open",
        "dept": "PRA",
        "users": "A Brown",
        "totalrefund": 32,
        "totalclaim": 11,
        "totalchargeback": 5,
        "totalpa61": 0,
        "page": "MNR",
    },
    {
        "openclose": "Open",
        "dept": "PRA",
        "users": "C. Lambert",
        "totalrefund": 1,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "MNR",
    },
    {
        "openclose": "Open",
        "dept": "PRA",
        "users": "CC Refund for process",
        "totalrefund": 14,
        "totalclaim": 4,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "MNR",
    },
    {
        "openclose": "Open",
        "dept": "PRA",
        "users": "Cash Refund For Process",
        "totalrefund": 5,
        "totalclaim": 3,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "MNR",
    },
    {
        "openclose": "Open",
        "dept": "PRA",
        "users": "E. Vinculado",
        "totalrefund": 1,
        "totalclaim": 2,
        "totalchargeback": 4,
        "totalpa61": 0,
        "page": "MNR",
    },
    {
        "openclose": "Open",
        "dept": "PRA",
        "users": "G. Lobianco",
        "totalrefund": 51,
        "totalclaim": 41,
        "totalchargeback": 8,
        "totalpa61": 0,
        "page": "MNR",
    },
    {
        "openclose": "Open",
        "dept": "PRA",
        "users": "J. Jones",
        "totalrefund": 7,
        "totalclaim": 5,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "MNR",
    },
    {
        "openclose": "Open",
        "dept": "PRA",
        "users": "M. Balsome",
        "totalrefund": 8,
        "totalclaim": 0,
        "totalchargeback": 8,
        "totalpa61": 0,
        "page": "MNR",
    },
    {
        "openclose": "Open",
        "dept": "PRA",
        "users": "M. McDermott",
        "totalrefund": 40,
        "totalclaim": 4,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "MNR",
    },
    {
        "openclose": "Open",
        "dept": "PRA",
        "users": "R. Cabrera ",
        "totalrefund": 5,
        "totalclaim": 2,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "MNR",
    },
    {
        "openclose": "Open",
        "dept": "PRA",
        "users": "R. Cepeda",
        "totalrefund": 6,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "MNR",
    },
    {
        "openclose": "Open",
        "dept": "PRA",
        "users": "T Pong",
        "totalrefund": 2,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "MNR",
    },
    {
        "openclose": "Open",
        "dept": "PRA",
        "users": "Y. Walcott",
        "totalrefund": 20,
        "totalclaim": 1,
        "totalchargeback": 1,
        "totalpa61": 0,
        "page": "MNR",
    },
    {
        "openclose": "Closed",
        "dept": "PRA",
        "users": "A Brown",
        "totalrefund": 18,
        "totalclaim": 6,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "MNR",
    },
    {
        "openclose": "Closed",
        "dept": "PRA",
        "users": "CC Refund for process",
        "totalrefund": 3,
        "totalclaim": 2,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "MNR",
    },
    {
        "openclose": "Closed",
        "dept": "PRA",
        "users": "Cash Refund For Process",
        "totalrefund": 7,
        "totalclaim": 7,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "MNR",
    },
    {
        "openclose": "Closed",
        "dept": "PRA",
        "users": "G. Lobianco",
        "totalrefund": 16,
        "totalclaim": 6,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "MNR",
    },
    {
        "openclose": "Closed",
        "dept": "PRA",
        "users": "J. Jones",
        "totalrefund": 1,
        "totalclaim": 2,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "MNR",
    },
    {
        "openclose": "Closed",
        "dept": "PRA",
        "users": "M. Balsome",
        "totalrefund": 0,
        "totalclaim": 1,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "MNR",
    },
    {
        "openclose": "Closed",
        "dept": "PRA",
        "users": "M. Goulard",
        "totalrefund": 1,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "MNR",
    },
    {
        "openclose": "Closed",
        "dept": "PRA",
        "users": "R. Cabrera ",
        "totalrefund": 2,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "MNR",
    },
    {
        "openclose": "Closed",
        "dept": "PRA",
        "users": "Y. Walcott",
        "totalrefund": 2,
        "totalclaim": 0,
        "totalchargeback": 0,
        "totalpa61": 0,
        "page": "MNR",
    },
]


# Create your views here.
def home(request):
    data = TransactionSummary.objects.all()
    template_data = {}
    template_data["title"] = "LIRR and MNR Page"
    template_data["selected_page"] = "Both"
    template_data["selected_sub"] = "All"
    template_data["data"] = data
    return render(request, "home/index.html", {"template_data": template_data})


def lirr(request):
    template_data = {}
    template_data["title"] = "LIRR Page"
    template_data["selected_page"] = "LIRR"
    template_data["selected_sub"] = "All"
    template_data["data"] = list(filter(lambda x: x["page"] == "LIRR", JSON_data))
    return render(request, "home/index.html", {"template_data": template_data})


def mnr(request):
    template_data = {}
    template_data["title"] = "MNR Page"
    template_data["selected_page"] = "MNR"
    template_data["selected_sub"] = "All"
    template_data["data"] = list(filter(lambda x: x["page"] == "MNR", JSON_data))
    return render(request, "home/index.html", {"template_data": template_data})


def show(request, id):
    template_data = {}
    template_data["title"] = "Show Page"
    template_data["selected_page"] = "Show"
    template_data["data"] = JSON_data[id]
    return render(request, "home/show.html", {"template_data": template_data})


def subpage(request, page, subpage):
    template_data = {}
    template_data["selected_page"] = page
    template_data["selected_sub"] = subpage
    template_data["title"] = "{} - {}".format(page, subpage)
    if page == "LIRR":
        filtered_data = list(filter(lambda x: x["page"] == "LIRR", JSON_data))
    elif page == "MNR":
        filtered_data = list(filter(lambda x: x["page"] == "MNR", JSON_data))
    else:
        filtered_data = JSON_data

    if subpage != "All":
        if subpage == "MailAndRide":
            filtered_data = list(
                filter(lambda x: x["dept"] == "Mail And Ride", filtered_data)
            )
        else:
            filtered_data = list(filter(lambda x: x["dept"] == subpage, filtered_data))

    template_data["data"] = filtered_data
    return render(request, "home/index.html", {"template_data": template_data})


def refund(request):
    template_data = {}
    template_data["title"] = "Refund Form"
    if request.method == "GET":
        routing_form = RoutingInformation(prefix="routing")
        personal_form = PersonalInformation(prefix="personal")
        template_data["forms"] = [
            {"title": "Routing Information", "form": routing_form},
            {"title": "Personal Information", "form": personal_form},
        ]
        return render(
            request,
            "home/refund.html",
            {"template_data": template_data},
        )
    elif request.method == "POST":
        form = PersonalInformation(request.POST)
        if form.is_valid():
            # Process the form data here
            cleaned_data = form.cleaned_data
            return render(
                request,
                "home/refund_success.html",
                {"data": cleaned_data},
            )
        else:
            return render(request, "home/refund.html", {"template_data": template_data})


def query(request):
    template_data = {}
    template_data["title"] = "Query Form"
    template_data["filter"] = True
    if request.method == "GET":
        query_form = QueryForm(prefix="query")
        template_data["forms"] = query_form
        return render(request, "home/filter.html", {"template_data": template_data})
    return render(request, "home/filter.html", {"template_data": template_data})


def batches(request):
    template_data = {}
    template_data["title"] = "Batches Page"
    template_data["selected_page"] = "Batches"
    return render(request, "home/batches.html", {"template_data": template_data})


def deadbeat(request):
    template_data = {}
    template_data["title"] = "Deadbeat Page"
    template_data["selected_page"] = "Deadbeat"
    return render(request, "home/deadbeat.html", {"template_data": template_data})


def list_deadbeats(request):
    template_data = {}
    template_data["title"] = "List of Deadbeats"
    template_data["selected_page"] = "List Deadbeats"
    return render(request, "home/list_deadbeats.html", {"template_data": template_data})
