"""Store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from APP.views import *
from django.urls import include, path
from Project import *
from APP import views
from templates import *







urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/',page),
    path('', osn),
    path('random/',pagewithrandom),
    path('hello',hello),
    path ('products/',include('APP.urls')),
    path('time/', TimePage),
    path('login/', user),
    path('products/', products_view, name= 'products'),
    path('products/<int:id>', product_view, name= 'product' ),
    path('', views.index),
    path('user/', views.user),
    path('img/',file_show),
    path('json/',json_show ),
    path('p1/', p1),
    path('p2/', p2),
    path('welcome/', index),
    path('food/', include('APP.urls2')),
    path('cat/', cat),
    path('dog/', dog),
    path('fish/', fish),
    path('hamster/', hamster),
    path('Street' , Street),
    path('School', Scholl),
    path('Index', Index),
    path('bayak-anatoliy-adamovich',Bayak),
    path('belyaev-aleksey-nikolaevich',Belyaev),
    path('blinov-vyacheslav-alekseevich', Blinov),
    path('volkov-nikolai-viktorovich', Volkov),
    path('galkina-lyubov-vladimirovna', Galkina),
    path('glazov-mikhail-dmitrievich', Glazov),
    path('gorodetskiy-dmitriy-igorevich', Gorodetskiy),
    path('gulko-david-mikhaylovich', Gulko),
    path('eromasov-vladimir-pavlovich', Eromasov),
    path('kamenshchik-dmitriy-vladimirovich', Kamenshchik),
    path('kovalevskiy_leonid_pavlovich', Kovalevskiy),
    path('kuznetsov-oleg-stepanovich', Kuzhetsov),
    path('maksimova-zoya-ivanovna', Maksimova),
    path('morozov-ivan-sergeevich', Morozov),
    path('nikolaichev-lev-grigorevich',Nikolaichev),
    path('novichkov-evgeniy-mikhaylovich', Novichkov),
    path('panchenko-aleksey-sidorovich',Panchenko ),
    path('ragimov_alizaman_sabir_ogly', Ragimov),
    path('ratkin-vladimir-gustavovich', Ratkin),
    path('romanova-tamara-tikhonovna',Romanova),
    path('safin-valeriy-vazykhovich',Safin),
    path('timofeeva-lidiya-vasilevna',Timofeeva),
    path('fedosov-yuriy-lazarevich',Fedosov),
    path('shalaev_vyacheslav_aleksandrovich',Shalaev),
    path('shevakina-nina-nikolaevna', Shevakina),
    path('shokurov_vladimir_viktorovich',Shokurov),
    path('shutov-vladislav-dmitrievich',Shutov),
    path('yarunin-aleksandr-vasilevich',Yarunin),
    path('Avenarius',Avenarius),
    path('Batirev', Batirev),
    path('Belov', Belov),
    path('Vostrakov',Vostrakov),
    path('Gagarin',Gagarin),
    path('Gogol',Gogol),
    path('Gorkiy', Gorkiy),
    path('Dzerjinski', Dzerjinski),
    path('Jukov',Jukov),
    path('Izmailov',Izmailov),
    path('Ilyushin',Ilyushin),
    path('Kolomica',Kolomica),
    path('Korneev', Korneev),
    path('Kurizhov',Kurizhov),
    path('Levanevsky',Levanevsky),
    path('Michurin',Michurin),
    path('Nevskiy',Nevskiy),
    path('Przhevalskiy',Przhevalskiy),
    path('Talalihin',Talalihin),
    path('Timiryazev',Timiryazev),
    path('Tolstoy',Tolstoy),
    path('Tupolev',Tupolev),
    path('Frunze',Frunze),
    path('Chehov',Chehov),
    path('Shevchenko', Shevchenko),
    path('Domodedovskiy_Licey_№3', Maksimov),
    path('Domodedovskaya_School_№2', School2),
    path('Domodedovskaya_School_№9', School9),
    path('Domodedovskaya_School_№12',School12),
    path('Ilyinskay_School', School3),
    path('Konstantinovskaya_School', School4),
    path('People',Popa)



    
   



]
