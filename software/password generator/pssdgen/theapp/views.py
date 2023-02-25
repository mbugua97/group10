from django.shortcuts import render

# Create your views here.
def generate(request):
    password=""
    if request.method=='POST':
        number=request.POST['number']
        characters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        for i in number:
            rand=rand.randint(0,25)
            password[i]=characters[rand]
        context={'password':password}
        return render(request,'theapp\index.html',context)
    return render(request,'theapp\index.html')