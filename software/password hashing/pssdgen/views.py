from django.shortcuts import render
import hashlib


hash_object = hashlib.md5()


def homepage(request):
    if request.method=='POST':
        password=request.POST['pass']
        hash_object.update(password.encode())
        hashed_psd = hash_object.hexdigest()
        context={'hashed_psd':hashed_psd}
        print(password)
        return render(request,"pssdgen\index.html",context)
    return render(request,"pssdgen\index.html")
