from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_numder = request.GET.get('page', 1)
    paginator = Paginator(csv_data, 10)
    page = paginator.get_page(page_numder)

    context = {
        'page': page,
        'bus_stations': page,
    }
    return  render(request, 'stations/index.html', context)

def get_csv(csv_file):
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

csv_data = get_csv('data-398-2018-08-30.csv')

