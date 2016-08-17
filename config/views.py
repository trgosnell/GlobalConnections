from django.http import HttpResponse

def default(request):
    return(HttpResponse('<h1>This is a default page.</h1>'))
