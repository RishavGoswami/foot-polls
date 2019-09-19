from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "FootPolls"
admin.site.site_title = "Admin"
admin.site.index_title = "FootPolls"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsSets = [(None, {'fields': ['question_text']}),
                  ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]

# Register the models to the admin panel
# admin.site.register(Question)
# admin.site.register(Choice)


admin.site.register(Question, QuestionAdmin)
