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


class QueryForm(BaseFormTemplate):
    bill_number = forms.CharField(max_length=20, label="BILL NO:", required=False)
    query_seq = forms.CharField(max_length=20, label="QUERY SEQ #:", required=False)
    form_no = forms.CharField(max_length=20, label="FORM NO #:", required=False)
    status = forms.ChoiceField(
        choices=[
            ("all", "All"),
            ("open", "Open"),
            ("closed", "Closed"),
        ],
        label="Status",
    )
    transaction_type = forms.ChoiceField(
        choices=[
            ("all", "All"),
            ("type1", "Type 1"),
            ("type2", "Type 2"),
        ],
        label="Transaction Type",
    )
    created_by_department = forms.ChoiceField(
        choices=[("dept1", "Department 1"), ("dept2", "Department 2")],
        label="Created by Department",
    )
    transaction_routed_to_department = forms.ChoiceField(
        choices=[("dept1", "Department 1"), ("dept2", "Department 2")],
        label="Transaction Routed to Department",
    )
    open_date_from = forms.DateField(
        label="Open Date From",
        widget=forms.DateInput(attrs={"type": "date"}),
        required=False,
    )
    open_date_to = forms.DateField(
        label="Open Date To",
        widget=forms.DateInput(attrs={"type": "date"}),
        required=False,
    )
    create_date = forms.DateField(
        label="Create Date",
        widget=forms.DateInput(attrs={"type": "date"}),
        required=False,
    )
    close_date = forms.DateField(
        label="Close Date",
        widget=forms.DateInput(attrs={"type": "date"}),
        required=False,
    )
    customer_order_number = forms.CharField(
        max_length=30, label="Customer Order Number", required=False
    )
    current_status = forms.ChoiceField(
        choices=[
            ("all", "All"),
            ("pending", "Pending"),
            ("approved", "Approved"),
            ("denied", "Denied"),
        ],
        label="Current Status",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            Row(
                Column("bill_number", css_class="me-2"),
                Column("query_seq", css_class="mx-2"),
                Column("form_no", css_class="ms-2"),
            ),
            Row(
                Column("status", css_class="me-2"),
                Column("transaction_type", css_class="mx-2"),
                Column("created_by_department", css_class="ms-2"),
                Column("transaction_routed_to_department", css_class="ms-2"),
            ),
            Row(
                Column("open_date_from", css_class="me-2"),
                Column("open_date_to", css_class="mx-2"),
                Column("create_date", css_class="ms-2"),
                Column("close_date", css_class="ms-2"),
            ),
            Row(
                Column("customer_order_number", css_class="me-2"),
                Column("current_status", css_class="ms-2"),
            ),
        )
