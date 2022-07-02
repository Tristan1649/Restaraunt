from django.contrib import admin
from .models import Table, BookTable, Response, Events, Food


admin.site.register(Table)
admin.site.register(BookTable)
admin.site.register(Response)
admin.site.register(Events)
admin.site.register(Food)

