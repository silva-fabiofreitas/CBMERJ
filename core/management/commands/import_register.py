import time

import pandas as pd
import numpy as np

from django.core.management.base import BaseCommand

from core.models import Occurrence
from address.models import Address, District
from epidemiological.models import Profile, Gender
from event.models import (RiskRating,
                          TypeOfOccurrence,
                          TypeOfTrafficAccident,
                          UnitType)


class Command(BaseCommand):
    help = 'Importar registro de ocorrencia do bombeiros'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs=1, type=str)

    def handle(self, *args, **options):
        path = options['path'][0]
        if not path:
            path = 'data.xlsx'

        self.df = pd.read_excel(path)

        self.df['IDADE'] = self.df['IDADE'].replace({np.nan:None})
    
        self.import_district()
        start = time.time()
        self.import_register()      

        self.stdout.write(self.style.SUCCESS(f'Tempo:{time.time() - start}'))

    def import_register(self):
        CAMPOS_ID = 1
        RJ_ID = 1
        Occurrence.objects.all().delete()
        Address.objects.all().delete()
        Profile.objects.all().delete()
        



        gender_obj = Gender.objects.values('id', 'name')
        def get_gender(gender):
            relation = {'id': dic['id']
                        for dic in gender_obj if dic['name'] == gender}
            return relation.get('id')

        district_obj = District.objects.values('id', 'name')
        def get_district(district):
            relation = {'id': dic['id']
                        for dic in district_obj if dic['name'] == district}
            return relation.get('id')

        risk_obj = RiskRating.objects.values('id', 'rating')
        def get_risk(risk):
            relation = {'id': dic['id']
                        for dic in risk_obj if dic['rating'] == risk}
            return relation.get('id')

        unit_type_obj = UnitType.objects.values('id', 'name')
        def get_unit_type(unit_type):
            relation = {'id': dic['id']
                        for dic in unit_type_obj if dic['name'] == unit_type}
            return relation.get('id')
        
        type_of_occurrence_obj = TypeOfOccurrence.objects.values('id', 'name')
        def get_type_of_occurrence(type_of_occurrence):
            relation = {'id': dic['id']
                        for dic in type_of_occurrence_obj if dic['name'] == type_of_occurrence}
            return relation.get('id')
        
        type_of_traffic_accident_obj = TypeOfTrafficAccident.objects.values('id', 'name')
        def get_type_of_traffic_accident(type_of_traffic_accident):
            relation = {'id': dic['id']
                        for dic in type_of_traffic_accident_obj if dic['name'] == type_of_traffic_accident}
            return relation.get('id')


        ocorrunces = []
        for row in self.df.iterrows():
            address_obj = Address.objects.create(
                district_id=get_district(row[1].BAIRRO),
                city_id=CAMPOS_ID,
                state_id=RJ_ID,
            )

            profile_obj = Profile.objects.create(
                age=row[1].IDADE,
                gender_id = get_gender(row[1].GENERO)
            )

            obj = Occurrence(
                date=row[1].DATA,
                address=address_obj,
                profile=profile_obj,
                risk_id=get_risk(row[1]['ESTRAT RISCO SOC']),
                unit_type_id=get_unit_type(row[1]['CONF SOC']),
                type_of_occurrence_id=get_type_of_occurrence(row[1]["EV CARACT"]),
                type_of_traffic_accident_id=get_type_of_traffic_accident(row[1]["AC TRANSP"]),
            )

            ocorrunces.append(obj)

        Occurrence.objects.bulk_create(ocorrunces)

        self.stdout.write(self.style.SUCCESS('Importação dos registros concluida.'))

    def import_district(self):
        District.objects.all().delete()
        district = self.df['BAIRRO'].unique()

        obj = (District(name=name) for name in district)
        District.objects.bulk_create(obj, ignore_conflicts=True)

        self.stdout.write(self.style.SUCCESS('Importação dos Bairros concluida.'))    
