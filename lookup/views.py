from django.shortcuts import render
import json 
import requests

def home(request):
    if request.method=='POST':
        zipcode = request.POST['zipcode']
        zipcode = request.POST['zipcode']
        # return render(request, 'home.html', {'zipcode':zipcode})
        api_request=requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=25&API_KEY=82DF4B59-C1B8-4908-AEAA-45B25C356139")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api="Error....."
        return render(request, 'home.html',{'api':api})
    else:
        api_request=requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=82DF4B59-C1B8-4908-AEAA-45B25C356139")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api="Error....."
        return render(request, 'home.html',{'api':api})

def about(request):
    return render(request, 'about.html',{})
