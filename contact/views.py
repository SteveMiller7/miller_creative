from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
				'first_name': form.cleaned_data['first_name'],
				'last_name': form.cleaned_data['last_name'],
				'email': form.cleaned_data['email_address'],
				'message': form.cleaned_data['message'],
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'info@millercreativedesign.com',
				          ['info@millercreativedesign.com'])
				messages.success(request,
								 'Thank you for your email. We will be in touch soon.')
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect(reverse('contact'))
      
	form = ContactForm()
	return render(request, "contact/contact.html", {'form': form})
