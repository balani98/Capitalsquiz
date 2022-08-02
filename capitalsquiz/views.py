from curses.ascii import HT
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
import random
import json
URL = 'https://countriesnow.space/api/v0.1/countries/capital'
def capitalsquiz(request):
    complete_data = requests.get(URL).json()
    countries_data = complete_data['data']
    countries_list = []
    for country in countries_data:
        countries_list.append(country['name'])
    # choosing the randome country
    country_name = random.choice(countries_list)
    return render(request,"capitalsquiz/quiz.html",{'country':country_name})

def validateCapital(request):
    try:
        context = {}
        country_name = request.GET.get('country')
        capital_input = request.GET.get('capital_input')
        complete_data = requests.get(URL).json()
        countries_data_dict = complete_data['data']
        # filtering the countires data 
        country_data_output_dict = [x for x in countries_data_dict if x['name'] == country_name]
        country_data = country_data_output_dict[0]
        if country_data['capital'].lower() == capital_input.lower() :
            context['message'] = 'Great !!! That is correct'
            context['correct'] = True  
            context['correct_answer'] = country_data['capital']
        else:
            context['message'] = 'Oops !!! That is incorrect'
            context['correct'] = False
            context['correct_answer'] = country_data['capital']
        return JsonResponse(context,status=200)
    except Exception as error:
        return JsonResponse(str(error),status=500)