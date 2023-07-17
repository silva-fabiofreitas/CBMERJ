from django.db.models import Count, F, OuterRef, Subquery, Window
# from django.contrib.postgres.aggregates import ArrayAgg 

from core.models import Occurrence

class Dashboard:
    
    qs = None

    @staticmethod
    def setFilteredOccurrence(queryset):
        Dashboard.qs = queryset

    @classmethod
    def get_statistc_piechart(cls):
        """
        Consolida as estatísticas de tipo de ocorrencia, tipo de acidente de transito,
          tipo de unidade de atendimento, risco.
          return dict  
        """    
        return dict(
            type_of_occurrence = cls.get_type_of_occurrence(),
            type_of_traffic_accident = cls.get_type_of_traffic_accident(),
            risk = cls.get_risk(),
            unit_type = cls.get_unit_type(),
            gender = cls.get_gender()
        )
    
    @staticmethod
    def get_type_of_occurrence():
        result = Dashboard.qs.exclude(type_of_occurrence__isnull=True) \
            .values('type_of_occurrence') \
            .annotate(name=F('type_of_occurrence__name'),value=Count('id'))

        return list(result)
    
    @staticmethod
    def get_type_of_traffic_accident():
        result = Dashboard.qs.exclude(type_of_traffic_accident__isnull=True) \
            .values('type_of_traffic_accident') \
            .annotate(name=F('type_of_traffic_accident__name'),value=Count('id'))

        return list(result)
    
    @staticmethod
    def get_risk():
        result = Dashboard.qs.exclude(risk__isnull=True) \
            .values('risk') \
            .annotate(name=F('risk__rating'),value=Count('id'))

        return list(result)
        
    @staticmethod
    def get_unit_type():
        result =Dashboard.qs.exclude(unit_type__isnull=True) \
            .values('unit_type') \
            .annotate(name=F('unit_type__name'),value=Count('id'))

        return list(result)
    
    @staticmethod
    def get_gender():
        result =Dashboard.qs.exclude(profile__gender__isnull=True) \
            .values('profile__gender') \
            .annotate(name=F('profile__gender__name'),value=Count('id'))

        return list(result)
        
    @staticmethod
    def get_age():
        result =Dashboard.qs.exclude(profile__age__isnull=True) \
            .exclude(profile__gender__isnull=True) \
            .values('profile__age', 'profile__gender__name') \
            .annotate(value=Count('id')).order_by("profile__age")

        return list(result)
    
    @staticmethod
    def get_distric_by_year():
        result =Dashboard.qs.exclude(address__district__isnull=True) \
            .values('date__year', 'address__district__name') \
            .annotate(value=Count('id')).order_by("date__year")
        
            
        import ipdb; ipdb.set_trace()
                     
        return list(result)

