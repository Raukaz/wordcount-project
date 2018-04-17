# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Below, the "name=" is for creating a name for links between pages, example in a page:
    # href="{% url 'homewebsite' %}" 
    path('',views.homepage, name='homewebsite'),
    # Below:
    # the "name='count'" is the reference for the code in the html file, in this case for
    # home.html: "<form action="{% url 'count' %}">"
    # This is very useful because I can change the "count/" path to any other name, and will
    # work with the changed name. Ex: path('countyes/', ...). You can verify in the html
    # souce code, that the new name will appear.
    path('count/', views.count, name='count'),
    # path('eggs/',views.eggs)
    # path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
]
