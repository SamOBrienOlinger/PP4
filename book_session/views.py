from django.shortcuts import render 

def get_book_session(request):
    return render(request, 'book_session/book_session.html')





