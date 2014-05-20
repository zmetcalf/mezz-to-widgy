from django.contrib import admin

from mezzanine.pages.admin import PageAdmin
from mezzanine.pages.models import RichTextPage

admin.site.register(RichTextPage, PageAdmin)
