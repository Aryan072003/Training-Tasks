from django.shortcuts import render

def home(request):
    name = 'Aryan'
    age = 21
    occupation = 'Engineer'
    return render(request, 'practice/index.html', {'name': name, 'age': age, 'occupation': occupation})
