from django.http.response import BadHeaderError, HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template.loader import render_to_string
from school.forms import CareerForm, NewsAddForm

from school.models import News, Slides1, Slides2, Slides3, Slides4

# Create your views here.


def start(request):
    news = News.objects.all()
    image1 = Slides1.objects.get(id=2) 
    image2 = Slides2.objects.get(id=1) 
    image3 = Slides3.objects.get(id=1) 
    image4 = Slides4.objects.get(id=1) 
    context = { 'news' : news, 'image1' : image1, 'image2' : image2, 'image3' : image3, 'image4' : image4 }
    return render(request, 'index.html', context)

def aboutoverview(request):
    return render(request, 'about_overview.html')

def aboutinfrastructure(request):
    return render(request, 'about_infrastructure.html')

def aboutmanagement(request):
    return render(request, 'about_management.html')

def aboutcampuslife(request):
    return render(request, 'about_campuslife.html')

def aboutgallery(request):
    return render(request, 'gallery.html')

def academicsoverview(request):
    return render(request, 'academics_overview.html')

def academicsboard(request):
    return render(request, 'academics_boardaffiliation.html')

def academicssubjects(request):
    return render(request, 'academics_subjects.html')

def general(request):
    return render(request, 'general.html')

def laboratory(request):
    return render(request, 'laboratory.html')

def hostel(request):
    return render(request, 'hostel.html')

def sports(request):
    return render(request, 'sports.html')

def bus(request):
    return render(request, 'bus.html')

def admissionprocedure(request):
    return render(request, 'admission_procedure.html')

def requireddocumentation(request):
    return render(request, 'required_documentation.html')

def parentfeedback(request):
    return render(request, 'parent_feedback.html')

def FAQ(request):
    return render(request, 'FAQ.html')

def knowyourchild(request):
    return render(request, 'know_your_child.html')

def contact(request):
    if request.method == 'GET':
        return render(request, 'contact.html')
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        from_email = request.POST['email']
        phone = request.POST['phone']
        comments = request.POST['comments']
        body = {
           'fname' : fname,
           'lname' : lname,
           'from_email' : from_email,
           'phone' : phone,
           'comments' : comments,
       }
        message = '''
                Details: 
                    First Name: {}
                    Last Name: {}
                    Email: {}
                    Mobile Number: {}
                    Comments: {}

                From: {}
            '''.format(body['fname'],body['lname'],body['from_email'],body['phone'],body['comments'],body['from_email'])
        try:
            send_mail('Contact Details',message, '',['skrischool2020@gmail.com'])
            # messages(request, 'We have have received your mail. Thank you.')
            redirect('/contact')
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
    return render(request, "contact.html")

def news(request,pk):
    news = News.objects.get(pk=pk)
    context = { 'news':news }
    return render(request, 'news.html', context)

def home(request):
        events = News.objects.all()
        context = {'events':events}
        return render(request, 'home.html',context)

def upload(request):
    return render(request, 'upload.html')

def upload1(request):
    if request.method == 'GET':
        return render(request, 'upload.html')
    if request.method == 'POST':
            image1 = request.FILES['image1']
            event = Slides1.objects.get(id=2)
            event.image1 = image1
            event.save()
            return redirect('/upload')
    return render(request, 'upload.html')

def upload2(request):
    if request.method == 'GET':
        return render(request, 'upload.html')
    if request.method == 'POST':
            image2 = request.FILES['image2']
            event = Slides2.objects.get(id=1)
            event.image2 = image2
            event.save()
            return redirect('/upload')
    return render(request, 'upload.html')

def upload3(request):
    if request.method == 'GET':
        return render(request, 'upload.html')
    if request.method == 'POST':
            image3 = request.FILES['image3']
            event = Slides3.objects.get(id=1)
            event.image3 = image3
            event.save()
            return redirect('/upload')
    return render(request, 'upload.html')

def upload4(request):
    if request.method == 'GET':
        return render(request, 'upload.html')
    if request.method == 'POST':
            image4 = request.FILES['image4']
            event = Slides4.objects.get(id=1)
            event.image4 = image4
            event.save()
            return redirect('/upload')
    return render(request, 'upload.html')

def addevent(request):
    if request.method == 'GET':
        return render(request, 'addevent.html')
    if request.method == 'POST':
            title = request.POST['title']
            desc = request.POST['description']
            image1 = request.FILES['image1']
            image2 = request.FILES['image2']
            image3 = request.FILES['image3']
            image4 = request.FILES['image4']
            event = News(title=title,content=desc,image1=image1,image2=image2,image3=image3,image4=image4)
            event.save()
            return redirect('/home')
    return render(request, 'addevent.html')

def deleteevent(request,pk):
    event  = News.objects.filter(pk=pk)
    event.delete()
    return redirect('/home')


def admin_view(request,pk):
    news = News.objects.get(pk=pk)
    context = { 'news':news }
    return render(request, 'admin_event_view.html', context)


def loginPage(request):
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request,user)
				return redirect('/home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request,  "login.html", context)

def logoutPage(request):
        logout(request)
        return redirect('/')

def career_zone(request):
	if request.method == 'POST':
		form = CareerForm(request.POST)
		if form.is_valid():
			subject = "Career Application" 
			body = {
			'Name': form.cleaned_data['Name'], 
			'Email': form.cleaned_data['Email'], 
			'Mobile_Number': form.cleaned_data['Mobile_Number'], 
			'Place':form.cleaned_data['Place'],
            'Department':form.cleaned_data['Department'], 
            'Position_Applying_for':form.cleaned_data['Position_Applying_for'],  
			}
			message = '''
                Details: 
                    Name: {}
                    Email: {}
                    Mobile Number: {}
                    Place: {}
                    Department: {}
                    Position Applying for: {}

                From: {}
            '''.format(body['Name'],body['Email'],body['Mobile_Number'],body['Place'],body['Department'],body['Position_Applying_for'],body['Email'])

			try:
				send_mail(subject, message, '', ['skrischool2020@gmail.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("/career-zone")
      
	form = CareerForm()
	return render(request, "career_zone.html", {'form':form})
