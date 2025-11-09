from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column


class BaseFormTemplate(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.label_class = "form-label"
        self.helper.form_class = "form-horizontal"


class RoutingInformation(BaseFormTemplate):
    status = forms.ChoiceField(
        choices=[
            ("open", "Open"),
            ("closed", "Closed"),
        ],
        widget=forms.RadioSelect,
        label="Status",
    )
    open_date_time = forms.DateTimeField(
        label="Open Date and Time",
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
    )
    from_department = forms.ChoiceField(
        choices=[("dept1", "Department 1"), ("dept2", "Department 2")],
        label="From Department",
    )
    from_user = forms.ChoiceField(
        choices=[("user1", "User 1"), ("user2", "User 2")], label="From User"
    )
    to_department = forms.ChoiceField(
        choices=[("dept1", "Department 1"), ("dept2", "Department 2")],
        label="To Department",
    )
    to_user = forms.ChoiceField(
        choices=[("user1", "User 1"), ("user2", "User 2")], label="To User"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            Row(
                Column(
                    "status",
                ),
                Column(
                    "open_date_time",
                ),
            ),
            Row(
                Column(
                    Row(
                        "from_department",
                    ),
                    Row(
                        "from_user",
                    ),
                ),
                Column(
                    Row(
                        "to_department",
                    ),
                    Row(
                        "to_user",
                    ),
                ),
            ),
        )


class PersonalInformation(BaseFormTemplate):
    title = forms.ChoiceField(
        choices=[("mr", "Mr."), ("ms", "Ms."), ("mrs", "Mrs.")], label="Title "
    )
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")
    address1 = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3}), label="Address"
    )
    address2 = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3}),
        label="Address (Line 2)",
        required=False,
    )
    zip_code = forms.CharField(max_length=10, label="ZIP Code")
    city = forms.CharField(max_length=50, label="City")
    state = forms.CharField(max_length=50, label="State")
    country = forms.CharField(max_length=50, label="Country")
    international_zip = forms.CharField(
        max_length=20, label="International ZIP", required=False
    )
    day_phone = forms.CharField(max_length=15, label="Day Phone", required=False)
    evening_phone = forms.CharField(
        max_length=15, label="Evening Phone", required=False
    )
    extension = forms.CharField(max_length=10, label="Extension", required=False)
    email = forms.EmailField(label="Email Address")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            Row(
                Column("title", css_class="me-2"),
                Column("first_name", css_class="mx-2"),
                Column("last_name", css_class="ms-2"),
            ),
            Row(
                Column("address1", css_class="me-2"),
                Column("address2", css_class="ms-2"),
            ),
            Row(
                Column("zip_code", css_class="me-2"),
                Column("city", css_class="mx-2"),
                Column("state", css_class="ms-2"),
            ),
            Row(
                Column("country", css_class="me-2"),
                Column("international_zip", css_class="ms-2"),
            ),
            Row(
                Column("day_phone", css_class="me-2"),
                Column("evening_phone", css_class="mx-2"),
                Column("extension", css_class="ms-2"),
            ),
            "email",
        )


class ReasonStatusInformation(BaseFormTemplate):
    status = forms.ChoiceField(
        choices=[
            ("pending", "Pending"),
            ("approved", "Approved"),
            ("denied", "Denied"),
        ],
        widget=forms.RadioSelect,
        label="Status",
    )
    reason = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4}), label="Reason for Refund"
    )
    status_update = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4}), label="Status Update"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            "reason",
            "status_update",
        )
