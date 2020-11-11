from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static
import os
import qrcode as qr
import secrets


def home(request):
    return render(request, 'main/index.html')

def generate_qr(request):
    if request.is_ajax():
        user_link = request.POST.get('user_link')
        if user_link:
            img = qr.make(user_link)
            try:
                filename = ".".join([secrets.token_hex(25), 'png'])
                file_path = os.path.join(os.getcwd(), 'main', 'static', 'main', 'qr_codes')
                print(os.path.join(file_path, filename))
                with open(os.path.join(file_path, filename), 'wb') as file:
                    img.save(file)
            except Exception as e:
                print(e)
                return HttpResponse('Internal Error, not generated!', status=500)
            else:
                return HttpResponse(static('main/qr_codes/'+filename))
        else:
            return HttpResponse("Missing Link!", status=500)
