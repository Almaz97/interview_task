from django.shortcuts import render
from .models import Country, DailyInfectionScan
from datetime import timedelta, datetime


def home_view(request):
    countries = Country.objects.all()

    start_date = datetime.strptime('2020-04-08', "%Y-%m-%d").date()

    weeks = []
    for i in range(1, 6):
        weeks.append([i, str(start_date) + ' / ' + str(start_date + timedelta(days=7))])
        start_date += timedelta(days=7)

    dataset = []
    for country in countries:
        total_infected_list = []
        total_died_list = []
        start_date = datetime.strptime('2020-04-08', "%Y-%m-%d").date()

        for i in range(6):
            weekly_condition = DailyInfectionScan.objects.filter(country=country,
                                                                 date__range=[start_date,
                                                                              start_date + timedelta(days=6)])
            if weekly_condition:
                total_infected = [week.infected for week in weekly_condition]
                total_died = [week.died for week in weekly_condition]
                total_infected_list.append(sum(total_infected))
                total_died_list.append(sum(total_died))
                start_date += timedelta(days=7)

        dataset.append({
            'country': country,
            'total_infected': total_infected_list,
            'total_died': total_died_list
        })

    context = {
        'weeks': weeks,
        'dataset': dataset
    }

    return render(request, 'home.html', context=context)
