from django import forms

class ContactForm(forms.Form):
	contact_name = forms.CharField(
		required=True,
		label='',
		max_length=50,
		widget=forms.TextInput(attrs={'placeholder':'Your name*',\
			"class":"form-control"}),
		)
	contact_email = forms.EmailField(
		required=True,
		label='',
		max_length=50,
		widget=forms.EmailInput(attrs={'placeholder':'Your email*',\
			"class":"form-control",}),
		)
	content = forms.CharField(
        required=False,
        label='',
        max_length=500,
        widget=forms.Textarea(attrs={'placeholder':'Message,Feedback,Comments',\
        	'rows':'8',"class":"form-control"}),
    )