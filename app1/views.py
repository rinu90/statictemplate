from django.shortcuts import render ,redirect
from app1.forms import ContactForm
# Create your views here.
def index(request):
    return render(request, 'index.html')
'''def register(request):
    return render(request, 'registration/register.html')'''

def register(request):
    #con = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Process form data (save to database, send email, etc.)
            # Redirect to a success page after processing
            return redirect('submit')  # 'submit' is the URL name for submit.html
    else:
        form = ContactForm()
    return render(request, 'registration/register.html', {'form':form})

def aboutme(request):
    return render(request, 'aboutme.html')

def submit_page(request):
    return render(request, 'submit.html')