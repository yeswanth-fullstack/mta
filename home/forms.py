from django import forms


class PersonalInformation(forms.Form):
    title = forms.ChoiceField(
        choices=[("mr", "Mr."), ("ms", "Ms."), ("mrs", "Mrs.")], label="Title"
    )
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")
    email = forms.EmailField(label="Email Address")
    phone_number = forms.CharField(max_length=15, label="Phone Number", required=False)
