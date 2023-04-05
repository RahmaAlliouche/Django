from django.contrib import admin


from .models import Medecine
from .models import Infermier
from .models import Abcense
from .models import Patient
from .models import Planing
from .models import Dossier_medecale
from .models import Rapport


admin.site.register(Medecine)
admin.site.register(Infermier)
admin.site.register(Patient)
admin.site.register(Planing)
admin.site.register(Dossier_medecale)
admin.site.register(Abcense)
admin.site.register(Rapport)

# Register your models here.
