from django.contrib import admin
from app.models import AddDoctor, Appointment,doclogin,Feedback,files

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'date', 'happy',)

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(AddDoctor)
admin.site.register(Appointment)
admin.site.register(doclogin)
admin.site.register(files)
