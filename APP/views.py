from itertools import product
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect,StreamingHttpResponse,FileResponse,JsonResponse
from random import randint
from Project import *
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.core.serializers.json import DjangoJSONEncoder
from . models import *
from templates import *



def page(request):
    print("Кто то зашёл на страницу")
    return StreamingHttpResponse("Привет мир!")
def main (request):
    return HttpResponse("Это главная страница")
   
    
    

def pagewithrandom(request):
    a = randint(0,100)
    return HttpResponse(f"Случайное число : {a}")

def hello(request):
    a = "Зайцев Максим"
    b = 14
    c = randint(0,100)
    return HttpResponse(f"Привет!,Я {a} и мне {b} лет. Случайное число : {c}. Наименование : {pet_1.name}, категория : {pet_1.category}, цена : {pet_1.size}")

class Product:
    __max_id = 0

    def __init__(self, name: str,category: str,breed: str,price: int,nutrition):

        self.id = Product.__max_id
        self.name = name
        self.category = category
        self.breed = breed
        self.price = price
        self.nutrition = nutrition
        Product.__max_id +=1


    def __str__(self):
        return (
            f'ID: {self.id}<br>'
            + f'Name: {self.name}<br>'
            + f'Cstegory: {self.category}<br>'
            + f'Breed: {self.breed}<br>'
            + f'Price: {self.price}<br>'
            + f'carnivorous:{self.nutrition}'
        )

        




products = [Product( "Cat","Home","Siamese",3000,"carnivorous"),
            Product( "Dog","Home","Dachshund",3500,"carnivorous"),
            Product("fish","Home","Gold",500,"carnivorous"),
            Product("hamster","Home","Jungarik",700,"carnivorous"),
            Product('','','','','')]

def categorires(request, milkid):
    if int(milkid) > 10:
        if request.GET:
            print(request)
        raise Http404()
    return HttpResponse(f"<h1>Категория Кошки</h1> <p>Товар {milkid}</p>")
def TimePage(request):
    date = datetime.date.today()
    time = datetime.datetime.today().time()
    return HttpResponse(f"<h1>Дата {date} время {time}</h1>")
def user(request):
    login = request.GET.get("login")
    password = request.GET.get("password")
    return HttpResponse(f"Ваш логин {login} ваш пароль {password} ")

def index(request):
    return HttpResponse("<h2>Главная<h2>")

def user(request):
    age = request.GET.get("age")
    name = request.GET.get("name")
    return HttpResponse(f"<h2>Имя: {name} Возраст: {age} </h2>")
@csrf_exempt
def products_view(request: HttpResponse):
    if request.method == 'GET':
        category = request.GET.get('category', None)
        print(repr(category), repr(products[-1].category))
        return HttpResponse(',\n\n'.join(str(product) for product in products
                                         if category is None
                                         or category == product.category))



    if request.method == 'POST':
        body = [element.strip() for element in
                request.body.decode('UTF-8').split('\n')]

        products.append(Product(
            name=body[0],
            category=body[1],
            breed=body[2],
            price=int(body[3]),
            
        ))

        return HttpResponse(str(products[-1]), status=200)

    return HttpResponse(status = 405)  



@csrf_exempt
def product_view(request: HttpResponse, id: int):
    filtered = [product for product in products if product.id == id ] 

    if len(filtered) == 0:
        return HttpResponse(status = 404)

    product = filtered[0]

    if request.method == 'GET':
        if product.name == '':
            return HttpResponseRedirect(reverse('products'))

        return HttpResponse(str(product))

    return HttpResponse(status=405)


def file_show(request):
    file = "C:\Django\Store\images\RobloxScreenShot20220816_171412240.png"
    return FileResponse(open(file,'rb'), as_attachment= True,filename="aboba.jpeg")

def json_show(request):
    data = {'Price':50, 'Book':'Poem'}
    return JsonResponse(data)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class PersonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj,Person):
            return{"name": obj.name, "age": obj.age}
        return super().default(obj)
def p1(request):
    bob = Person("Bob", 50)
    return JsonResponse(bob, safe=False, encoder=PersonEncoder)

def p2(request):
    tim = Person("Tim", 16)
    return JsonResponse(tim, safe=False, encoder=PersonEncoder)

    
def index(request):
    bd = Question.objects.all()
    return render(request, 'index.html',{'bd':bd})





def index1(request):
    return render(request, 'index1.html')

def index2(request):
    return render(request, 'index2.html')


class Product:
    def __init__(self,id,name,category,breed,price,nutrition):
        self.id = (id)
        self.name = str(name)
        self.category = str(category)
        self.breed = breed
        self.price = price
        self.nutrition = nutrition

class ProductEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj,Product):
            return{"id": obj.id, "name": obj.name,"category": obj.category,"breed": obj.breed,"price": obj.price,"nutrition": obj.nutrition}
        return super().default(obj)
def cat(request):
    cat= Product("68737", "Cat","pet","Siamese","3000p","carnivorous")
    return JsonResponse(cat, safe = False,encoder=ProductEncoder)
def dog(request):
    dog= Product("68738", "Dog","pet","Dachshund","3500p","carnivorous")
    return JsonResponse(dog, safe = False,encoder=ProductEncoder)
def fish(request):
    fish= Product("68739", "fish","pet","Gold","500p","herbivorus")
    return JsonResponse(fish, safe = False,encoder=ProductEncoder)
def hamster(request):
    hamster= Product("68740", "hamster","pet","Jungarik","700p","herbivorus")
    return JsonResponse(hamster, safe = False,encoder=ProductEncoder)



    
    

def osn(request):
    return render(request, 'MainMenu.html')  
def Street(request):
    return render(request, 'hz.html')
def Scholl(request):
    return render(request, 'school.html')
def Index(request):
    return render(request, 'index1.html')
def Bayak(request):
    return render(request, 'Bayak.html')
def Belyaev(request):
    return render(request, 'belyaev.html')
def Blinov(request):
    return render(request, 'blinov.html')
def Volkov(request):
    return render(request, 'volkov.html')
def Galkina(request):
    return render(request, 'galkina.html')
def Glazov(request):
    return render(request, 'glazov.html')
def Gorodetskiy(request):
    return render(request, 'gorodetskiy.html')
def Gulko(request):
    return render(request, 'gulko.html')
def Eromasov(request):
    return render(request, 'eromasov.html')
def Kamenshchik(request):
    return render(request, 'kamenshchik.html')
def Kovalevskiy(request):
    return render(request, 'kovalevskiy.html')
def Kuzhetsov(request):
    return render(request, 'kuznetsov.html')
def Maksimova(request):
    return render(request, 'maksimova.html')
def Morozov(request):
    return render(request, 'morozov.html')
def Nikolaichev(request):
    return render(request, 'nikolaichev.html')
def Novichkov(request):
    return render(request, 'novichkov.html')
def Panchenko(request):
    return render(request, 'panchenko.html')
def Ragimov(request):
    return render(request, 'ragimov.html')
def Ratkin(request):
    return render(request, 'ratkin.html')
def Romanova(request):
    return render(request, 'romanova.html')
def Safin(request):
    return render(request, 'safin.html')
def Timofeeva(request):
    return render(request, 'timofeeva.html')
def Fedosov(request):
    return render(request, 'fedosov.html')
def Shalaev(request):
    return render(request, 'shalaev.html')
def Shevakina(request):
    return render(request, 'shevakina.html')
def Shokurov(request):
    return render(request, 'shokurov.html')
def Shutov(request):
    return render(request, 'shutov.html')
def Yarunin(request):
    return render(request, 'yarunin.html')
def Avenarius(request):
    return render(request, 'Avenarius.html')
def Batirev(request):
    return render(request, 'Batirev.html')
def Belov(request):
    return render(request, 'Belov.html')
def Vostrakov(request):
    return render(request, 'Vostrakov.html')
def Gagarin(request):
    return render(request, 'Gagarin.html')
def Gogol(request):
    return render(request,'Gogol.html')
def Gorkiy(request):
    return render(request, 'Gorkiy.html')
def Dzerjinski(request):
    return render(request,'Dzerjinski.html')
def Jukov(request):
    return render(request,'Jukov.html')
def Izmailov(request):
    return render(request, 'Izmailov.html')
def Ilyushin(request):
    return render(request,'Ilyushin.html')
def Kolomica(request):
    return render(request,'Kolomica.html')
def Korneev(request):
    return render(request,'Korneev.html')
def Kurizhov(request):
    return render(request,'Kurijov.html')
def Levanevsky(request):
    return render(request,'Levanevsky.html')
def Michurin(request):
    return render(request,'Michurin.html')
def Nevskiy(request):
    return render(request, 'Nevskiy.html')
def Przhevalskiy(request):
    return render(request, 'Przhevalskiy.html')
def Talalihin(request):
    return render(request,'Talalihin.html')
def Timiryazev(request):
    return render(request,'Timiryazeva.html')
def Tolstoy(request):
    return render(request,'Tolstogo.html')
def Tupolev(request):
    return render(request,'Tupolev.html')
def Frunze(request):
    return render(request, 'Frunze.html')
def Chehov(request):
    return render(request,'Chehov.html')
def Shevchenko(request):
    return render(request, 'Shevchenko.html')
def Maksimov(request):
    return render(request,'DomLiceyN3.html')
def School2(request):
    return render(request,'DomSchool№2.html')
def School9(request):
    return render(request,'DomSchool№9.html')
def School12(request):
    return render(request, 'DomSchool№12.html')
def School3(request):
    return render(request,'IlyinskaySchool.html')
def School4(request):
    return render(request,'Konstantinovskaya_School.html')
def Popa(request):
    return render(request,'osn.html')