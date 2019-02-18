# Main App URL Config

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

API_TITLE = "Morgantown Codes Demo API"
API_DESCRIPTION = "We really hope this works."
schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include("rest_framework.urls")),
    path('demo/', include("demo_app.urls")),

    path('schema/', schema_view),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
]
