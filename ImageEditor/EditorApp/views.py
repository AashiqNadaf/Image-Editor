from django.shortcuts import render
from EditorApp.forms import ImageForm
from EditorApp.models import ImageModel
from django.http import HttpResponseRedirect


# Create your views here.
def deleteImg():
    count = ImageModel.objects.all().count()
    for i in range(count):
        imgs = ImageModel.objects.last()
        imgs.delete()

def index(request):
    form = ImageForm()

    if request.method == 'POST':
        deleteImg()
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect("/editing/")
        else:
            print("Error")
    

    return render(request, "EditorApp/index.html", {'form': form})

def imageEditingPage(request):
    img = ImageModel.objects.first().image
    print(img)
    return render(request, "EditorApp/imageEdit.html", {'orgImg': img})