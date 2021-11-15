from django import forms
from django.contrib import admin


# from .models import Question, Option, Result, User
from .models import Question, Option, Result
from django.contrib.auth.admin import UserAdmin


class OptionInline(admin.TabularInline):
    model = Option
    extra = 1
class ResultInline(admin.TabularInline):
    model = Result
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    #fieldsets are what we see when we click on the Question to see it's details
    fieldsets = [
        (None,{'fields': ['question', 'description', 'code']}),
        # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    #inlines help us to add related fields. Options and results are related by a FOriegnKey
    inlines = [OptionInline, ResultInline]
    # This is the view when we see all of the questions together in one list...
    list_display = ('question','description','code', 'id')
    search_fields = ['question', 'code']

class ResultAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "order",)

# class CustomUserAdmin(UserAdmin):
#     fieldsets = (
#         *UserAdmin.fieldsets,  # original form fieldsets, expanded
#         (                      # new fieldset added on to the bottom
#             'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
#             {
#                 'fields': (
#                     'is_bot_flag',
#                 ),
#             },
#         ),
#     )


# admin.site.register(User, CustomUserAdmin)


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Result, ResultAdmin)
# admin.site.register(User)
# admin.site.register(User, UserAdmin)
