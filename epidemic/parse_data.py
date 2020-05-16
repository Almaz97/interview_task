import csv
from epidemic.models import Country, DailyInfectionScan


with open('/home/almaz/test_project/inspection/epidemic/owid-covid-data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        iso_code = line[0]
        location = line[1]
        date = line[2]
        new_cases = int(line[4])
        new_death = int(line[6])

        country, created = Country.objects.get_or_create(name=location, iso_code=iso_code)
        daily_scan = DailyInfectionScan.objects.create(country=country, infected=new_cases, died=new_death, date=date)

print('finished')