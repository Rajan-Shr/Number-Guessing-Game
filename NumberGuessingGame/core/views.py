from django.shortcuts import render, redirect
from .models import Number
from .forms import NumberForm
import numpy as np
# Create your views here.
def index(request):
    message = ""
    if "random_number" not in request.session:
        random_number = np.random.randint(1,100,dtype=int)
        request.session["random_number"] = random_number
        request.session["count"] = 0
    if request.method == "POST":
        form = NumberForm(request.POST)
        if form.is_valid():
            user_number = int(request.POST.get("number"))
            computer_number =int(request.session.get("random_number"))
            request.session["count"] += 1
            count = request.session.get("count")

            if(computer_number > user_number):
                message = "Enter Greater number"
            elif(computer_number<user_number):
                message = "Enter Smaller number"
            else:
                message = f"Congratulations ! You won in {count} attempts"
                request.session.flush() 
        
        return render(request,"core/index.html",{
            'form':form,
            'message':message
        })
    else:
        form = NumberForm()

        return render(request,"core/index.html",{
            'form':form,
            'message':message
        })




    