from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, "home.html")

def about(request):
    return render (request, "about.html")

def projects(request):
    projects_show=[
        {
            "title": "Weather forecast",
            "path": "images/weather.jpeg",
           
        },
        {
            "title": "Job application",
            "path": "images/job.png",
          
        },
        
        {
            "title": "Calculator",
            "path": "images/calculator.png",    
        },
        
        {
            "title": "Student Management system",
            "path": "images/management.png  ", 
        },
        {
            "title": "Restaurant kitchen webapp",
            "path": "images/kitchen.jpeg  ",  
        },
        {
            "title": "Todo-list",
            "path": "images/todo.jpeg",
        },
    ]
    return render (request, "projects.html", {"projects_show": projects_show})