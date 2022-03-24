from django.shortcuts import render
from .forms import CsvModelForm
from .models import Csv
import csv
from dataitem.models import DataItem

# Create your views here.

def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0: # To get rid of header row
                    pass
                else:
                    a = row[0]
                    item_id = a.split(",")[0]
                    reference = a.split(",")[1]
                    name = a.split(",")[2]
                    owner = a.split(",")[3]
                    DataItem.objects.create(
                        item_id = item_id,
                        reference = reference,
                        name = name,
                        owner = owner
                    )

            obj.activated = True
            obj.save()
    dataitems = DataItem.objects.all()

    return render(request, 'csvs/upload.html', {
        'form':form,
        'dataitems':dataitems
    })


def view_d0010(request):
    mpan_cores_d0010 = ["J0003","J0004"]
    dataitems = DataItem.objects.all()
    
    return render(request, 'csvs/viewdata.html',{'dataitems':dataitems, 'mpans':mpan_cores_d0010})