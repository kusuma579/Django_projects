from django.shortcuts import render


def home(request):

    data = {

        'name': 'Kusuma Sravya',

        'role': 'Python Full Stack Developer',

        'college': 'VFSTR University',

        'email': 'sravya@gmail.com',

        'phone': '9876543210',

        'location': 'Guntur',

        'skills': [
            'Python',
            'Django',
            'HTML',
            'CSS',
            'JavaScript',
            'MySQL'
        ],

        'projects': [
            'Online Shopping Cart System',
            'Employee Management System',
            'Portfolio Website',
            'Book Management Application'
        ]
    }

    return render(request, 'home.html', data)


def contact(request):

    data = {}

    if request.method == "POST":

        data['name'] = request.POST.get('name')

        data['email'] = request.POST.get('email')

        data['message'] = request.POST.get('message')

    return render(request, 'contact.html', data)
