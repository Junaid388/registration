from django.shortcuts import render

def post_list(request):
    return render(request, 'regis/post_list.html', {})
