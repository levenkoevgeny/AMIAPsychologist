from django.contrib import admin
from .models import Rank, Subdivision, WorkDone, WorkKind, Request, PersonalWork


admin.site.register(Rank)
admin.site.register(Subdivision)
admin.site.register(WorkDone)
admin.site.register(WorkKind)
admin.site.register(Request)
admin.site.register(PersonalWork)