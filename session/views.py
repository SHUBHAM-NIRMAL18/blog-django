from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
# Simple Staic login for session demo
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'shubham' and password == 'pass123':
            request.session['username'] = username # Save shubham to session
            return redirect('dashboard')
        return render(request, 'login.html', {'error':'Incorrect password'})


