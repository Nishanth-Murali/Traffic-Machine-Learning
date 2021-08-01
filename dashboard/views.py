from django.shortcuts import render
from django.http import Http404, JsonResponse
from rest_framework import generics
from .serializers import DataSerializer
from .models import Data
import json
import copy

import dashboard.management.commands.load_traffic_data as dmcl


class DataView(generics.CreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

def index(request):
    return render(request, 'query/query.html')



def home(request):
    if request.method == 'POST':
        print("Good Morning")

        print(request.POST)
        vendors=request.POST.get("vendors")
        Intersection=request.POST.get("Intersection")
        trip_start=request.POST.get("trip-start")
        trip_end = request.POST.get("trip-end")
        appt_start=request.POST.get("appt-start")
        appt_end = request.POST.get("appt-end")
        check_box= request.POST.getlist("checkbox")

        print(vendors)
        print(Intersection)
        print(trip_start)
        print(trip_end)
        print(appt_start)
        print(appt_end)
        print(check_box)

        d=dmcl.Command()
        #d.handle()


        file = 'D:/Jobs/Full Time/EPICS Cause no JOB/Traffic Data Analysis/react_traffic_dashboard1/2021-01-31 00-00-00.json'

        f = open(file, )
        data = json.load(f)
        context = {
            'data': convert_data_to_dict(data),

        }


    # if a GET (or any other method) we'll create a blank form
    else:
        print("BYEEE")
        data = Data.objects.all()
        context={}


    return render(request, 'query/query.html',context)



def convert_data_to_dict(data):
    for hh in range(00, 24):
        for mm in range(00, 60):

            result = "{:02.0f}:{:02.0f}".format(hh, mm) + ":00"
            vehicles={'Light':0,'Bus':0,'ArticulatedTruck':0,'SingleUnitTruck':0,'Bicycle':0}

            directions={'EE':copy.deepcopy(vehicles),'EW':copy.deepcopy(vehicles),'EN':copy.deepcopy(vehicles),'ES':copy.deepcopy(vehicles),
                        'WE':copy.deepcopy(vehicles),'WW':copy.deepcopy(vehicles),'WN':copy.deepcopy(vehicles),'WS':copy.deepcopy(vehicles),
                        'NE':copy.deepcopy(vehicles),'NW':copy.deepcopy(vehicles),'NN':copy.deepcopy(vehicles),'NS':copy.deepcopy(vehicles),
                        'SE':copy.deepcopy(vehicles),'SW':copy.deepcopy(vehicles),'SN':copy.deepcopy(vehicles),'SS':copy.deepcopy(vehicles)}

            for row_data in data:
                if result not in row_data['timestamp']:
                    print(directions)
                    return directions
                directions[row_data['entrance']+row_data['exit']][row_data['class']]=row_data['qty']


# def data_detail(request, data_id):
#     try:
#         data = Data.objects.get(id=data_id)
#     except Data.DoesNotExist:
#         raise Http404('traffic_dashboard data not found')
#     return render(request, 'data_detail.html', {'data': data,})
