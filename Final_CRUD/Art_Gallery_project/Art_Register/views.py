from django.shortcuts import render
from .models import ArtInformation

from django.views.generic import TemplateView
import shutil
import os
# Create your views here.

# Function Based Views

# def index(request):
#     return render(request, 'index.html')

# def buttons(request):
#     button = request.POST["b1"]
#     if button == "Insert":

#         id = request.POST["Art_Id"]
#         Art_Title = request.POST["Art_Title"]
#         Description = request.POST["Description"]
#         Artist = request.POST["Artist"]
#         Completion_Date = request.POST["Completion_Date"]
#         Category = request.POST["Category"]
        
#         try:
#             t1 = request.POST['t1']
#         except:
#             t1 = 0
#         try:
#             t2 = request.POST['t2']
#         except:
#             t2 = 0
#         try:
#             t3 = request.POST['t3']
#         except:
#             t3 = 0
#         try:
#             t4 = request.POST['t4']
#         except:
#             t4 = 0
#         try:
#             t5 = request.POST['t5']
#         except:
#             t5 = 0
#         try:
#             t6 = request.POST['t6']
#         except:
#             t6 = 0
#         try:
#             t7 = request.POST['t7']
#         except:
#             t7 = 0
#         try:
#             t8 = request.POST['t8']
#         except:
#             t8 = 0

#         Art_Price = request.POST["Art_Price"]
#         # pic = (request.FILES["picture"])

#         pic = request.POST["picture"]

#         #pathimage = os.path.join("C:\Users\SANDHYA CHETTIAR\Desktop\Final_CRUD\Art_Gallery_project\photos", str(pic))
#         pathimage ="C:/Users/SANDHYA CHETTIAR/Desktop/Final_CRUD/Art_Gallery_project/photos/" + str(pic) 

#         shutil.copy(pathimage,"C:/Users/SANDHYA CHETTIAR/Desktop/Final_CRUD/Art_Gallery_project/media/images")

#         obj = ArtInformation.objects.create(
#             Art_Id=id, Art_Title=Art_Title, Description=Description, Artist=Artist, Completion_Date=Completion_Date, Category=Category, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5, t6=t6, t7=t7, t8=t8, Art_Price=Art_Price, pic="images/"+pic)

#         msg = "Record Inserted"
#         return render(request, 'result.html', {'msg': msg})

#     elif button == "Select":
#         id = request.POST['Art_Id']
#         obj = ArtInformation.objects.get(pk=id)
#         return render(request, 'result.html', {'obj': obj})

#     elif button == "Update":

#         id = request.POST["Art_Id"]
#         Art_Title = request.POST["Art_Title"]
#         Description = request.POST["Description"]
#         Artist = request.POST["Artist"]
#         Completion_Date = request.POST["Completion_Date"]
#         Category = request.POST["Category"]
        
#         try:
#             t1 = request.POST['t1']
#         except:
#             t1 = 0
#         try:
#             t2 = request.POST['t2']
#         except:
#             t2 = 0
#         try:
#             t3 = request.POST['t3']
#         except:
#             t3 = 0
#         try:
#             t4 = request.POST['t4']
#         except:
#             t4 = 0
#         try:
#             t5 = request.POST['t5']
#         except:
#             t5 = 0
#         try:
#             t6 = request.POST['t6']
#         except:
#             t6 = 0
#         try:
#             t7 = request.POST['t7']
#         except:
#             t7 = 0
#         try:
#             t8 = request.POST['t8']
#         except:
#             t8 = 0

#         Art_Price = request.POST["Art_Price"]
#         pic = request.POST["picture"]


#         obj = ArtInformation.objects.get(pk=id)
#         obj.Art_Id = id
#         obj.Art_Title = Art_Title
#         obj.Description = Description
#         obj.Artist = Artist
#         obj.Completion_Date = Completion_Date
#         obj.Category = Category
#         obj.Art_Price = Art_Price
#         obj.pic = pic
        
#         obj.t1 = t1
#         obj.t2 = t2
#         obj.t3 = t3
#         obj.t4 = t4
#         obj.t5 = t5
#         obj.t6 = t6
#         obj.t7 = t7
#         obj.t8 = t8
#         obj.save()
#         msg = "Record Updated"
#         return render(request, 'result.html', {'msg': msg})

#     elif button == "Delete":
#         id = request.POST['Art_Id']
#         obj = ArtInformation.objects.get(pk=id)
#         obj.delete()
#         msg = "Record Deleted"
#         return render(request, 'result.html', {'msg': msg})




# Class Based Views

class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class ButtonView(TemplateView):

    def post(self, request, *args, **kwargs):
        button = request.POST["b1"]
        if button == "Insert":

            id = request.POST["Art_Id"]
            Art_Title = request.POST["Art_Title"]
            Description = request.POST["Description"]
            Artist = request.POST["Artist"]
            Completion_Date = request.POST["Completion_Date"]
            Category = request.POST["Category"]
            
            try:
                t1 = request.POST['t1']
            except:
                t1 = 0
            try:
                t2 = request.POST['t2']
            except:
                t2 = 0
            try:
                t3 = request.POST['t3']
            except:
                t3 = 0
            try:
                t4 = request.POST['t4']
            except:
                t4 = 0
            try:
                t5 = request.POST['t5']
            except:
                t5 = 0
            try:
                t6 = request.POST['t6']
            except:
                t6 = 0
            try:
                t7 = request.POST['t7']
            except:
                t7 = 0
            try:
                t8 = request.POST['t8']
            except:
                t8 = 0

            Art_Price = request.POST["Art_Price"]
            

            pic = request.POST["picture"]

            pathimage ="C:/Users/SANDHYA CHETTIAR/Documents/GitHub/CRUD_Capstone/Final_CRUD/Art_Gallery_project/photos/" + str(pic) 
            
            shutil.copy(pathimage,"C:/Users/SANDHYA CHETTIAR/Documents/GitHub/CRUD_Capstone/Final_CRUD/Art_Gallery_project/media/images")
            
            obj = ArtInformation.objects.create(
                Art_Id=id, Art_Title=Art_Title, Description=Description, Artist=Artist, Completion_Date=Completion_Date, Category=Category, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5, t6=t6, t7=t7, t8=t8, Art_Price=Art_Price, pic="images/"+pic)

            msg = "Record Inserted"
            return render(request, 'result.html', {'msg': msg})

        elif button == "Select":
            id = request.POST['Art_Id']
            obj = ArtInformation.objects.get(pk=id)
            return render(request, 'result.html', {'obj': obj})

        elif button == "Update":

            id = request.POST["Art_Id"]
            Art_Title = request.POST["Art_Title"]
            Description = request.POST["Description"]
            Artist = request.POST["Artist"]
            Completion_Date = request.POST["Completion_Date"]
            Category = request.POST["Category"]
            
            try:
                t1 = request.POST['t1']
            except:
                t1 = 0
            try:
                t2 = request.POST['t2']
            except:
                t2 = 0
            try:
                t3 = request.POST['t3']
            except:
                t3 = 0
            try:
                t4 = request.POST['t4']
            except:
                t4 = 0
            try:
                t5 = request.POST['t5']
            except:
                t5 = 0
            try:
                t6 = request.POST['t6']
            except:
                t6 = 0
            try:
                t7 = request.POST['t7']
            except:
                t7 = 0
            try:
                t8 = request.POST['t8']
            except:
                t8 = 0

            Art_Price = request.POST["Art_Price"]
            

            obj = ArtInformation.objects.get(pk=id)
            obj.Art_Id = id
            obj.Art_Title = Art_Title
            obj.Description = Description
            obj.Artist = Artist
            obj.Completion_Date = Completion_Date
            obj.Category = Category
            obj.Art_Price = Art_Price
            
            obj.t1 = t1
            obj.t2 = t2
            obj.t3 = t3
            obj.t4 = t4
            obj.t5 = t5
            obj.t6 = t6
            obj.t7 = t7
            obj.t8 = t8

            obj.save()
            msg = "Record Updated"
            return render(request, 'result.html', {'msg': msg})

        elif button == "Delete":
            id = request.POST['Art_Id']
            obj = ArtInformation.objects.get(pk=id)
            obj.delete()
            msg = "Record Deleted"
            return render(request, 'result.html', {'msg': msg})