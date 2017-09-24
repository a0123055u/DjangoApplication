import json,pdb

import datetime
from django.shortcuts import render, reverse, redirect, render_to_response
# Create your views here.
from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from rest_framework import status
from rest_framework.response import Response
from django.template import loader
from webapp.models import user,ProductOrders,ProductElectronics
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone


# from passlib.hash import md5_crypt as md5
# from passlib.hash import sha256_crypt as sha256
# from passlib.hash import sha512_crypt as sha512


def index(request):
    print('index')

    return render(request, 'webapp/login.html')

class ReLogIn(TemplateView):
    template_name='webapp/login.html'


class SignUp(TemplateView):
    print'content 3rd'
    template_name ='webapp/SignUp.html'

class popOut(TemplateView):
    print'pop Up'
    template_name = 'webapp/modalWindow.html'
    # return render_to_response('webapp/SignUp.html')

# class Content(TemplateView):
#     print'content 1st'
#     template_name = "webapp/SignUp.html"
#     def get(self,request):
#         print'content 2nd'
#         return render(request, 'webapp/SignUp.html')

class HomePage(TemplateView):
    print'Home page Redirected'
    template_name = 'webapp/Home.html'


def save(request):
    print('Test request')
    context = {'data': 'reached', 'response': 'Success'}
    print(context)
    post_body=json.loads(request.body)
    print('request', post_body['name'])
    if request.method == 'POST':
        checkDuplicationOfUsers=user.objects.filter(email=post_body['email'])
        if checkDuplicationOfUsers.exists():
            context = {'data': 'exisit', 'response': 'exisit'}
            return HttpResponse(json.dumps(context))
        encrypted_password_django_inbuilt=make_password(post_body['password'])
        userInstance = user(name=post_body['name'],password=encrypted_password_django_inbuilt,age =post_body['age'],
    nationality = post_body['nationality'],gender =post_body['gender1'],address=post_body['address'],email=post_body['email'],fin=post_body['fin'])
        userInstance.save()
        context = {'data': 'reached', 'response': 'Success'}
        print('entered post')

        return HttpResponseRedirect(reverse('relogin'))
        # return JsonResponse({'success': 'reached'}, status=200)
    else:
        context = {'data': 'reached', 'response': 'Success'}
        print('not post', request)
        return HttpResponseRedirect(reverse('relogin'))
            # JsonResponse({'error': 'not post'}, status=400)






def singin(request):
    print'request',request.POST
    # pdb.set_trace()
    if request.method=='POST':
        print request.body

        # post_body = json.loads(request.body)
        userName= request.POST.get('userName')
        passWord=request.POST.get('password')
        print'userName',userName,'Password',passWord,request.POST
        validUserName= user.objects.filter(name=userName)
        if validUserName.exists():
            password = validUserName.values()[0]['password']
            if check_password(passWord,password): #used to check hashed password under the given string in post.
                # template= loader.get_template('webapp/SignUp.html')
                # return HttpResponse(template.render(context=None))
                # url = reverse('content',permanent=True, kwargs={'classname': Content})
                # return render(request, "webapp/SignUp.html",context=None)
                # response = TemplateResponse(request, 'webapp/SignUp.html', {})
                request.session['username'] = userName
                request.session['email']=validUserName.values()[0]['email']
                return HttpResponseRedirect(reverse('home'))
                # import pdb
                # pdb.set_trace()
                # return render_to_response('webapp/SignUp.html',context=None, content_type=None, status=225)
                # return response
                # return redirect('/content',permanent=True,kwargs={'classname':Content})
                print 'after render'

            else:
                if password==passWord:
                    update_user_password=user.objects.filter(name=userName)
                    enrupted_password_using_inbuit_django=make_password(passWord)
                    update_user_password.update(password=enrupted_password_using_inbuit_django)
                    print'update_user_password',update_user_password,'encrypted password -',enrupted_password_using_inbuit_django
                    return HttpResponseRedirect(reverse('signup'))

                return JsonResponse({'error': 'WrongPassword'}, status=220)
        else:
            return JsonResponse({'error': 'Invalid UserName'}, status=230)




def checkOut(request):
    if request.method == 'POST':
        post_body = json.loads(request.body)
        postBody = post_body["postPayLoad"]
        model=postBody[0]["Model"]
        # model = [mod.encode('utf-8') for mod in model]
        price= postBody[0]["Price"]
        price = price.strip('$')
        price = int(price)
        userName = request.session['username']
        email = request.session['email']
        qty = 1
        salesCount = ProductOrders.objects.count()
        salesCount+=1
        print salesCount
        orderId = ('OID'+str(salesCount))
        print orderId
        my_datetime= datetime.datetime.now()
        product = ProductElectronics.objects.filter(modelName=model).first()
        print 'product>>>>>>>>>>>>>',product,product.modelName
        product.iventory= product.iventory-qty
        product.selledCount=product.selledCount+qty
        my_datetime=timezone.make_aware(my_datetime, timezone.get_current_timezone())
        order = ProductOrders(orderId=orderId,
                modelName =product,
                user = userName,
                email =email,
                quantity = qty,
                price =price,
                dateOfPurchase=my_datetime)
        print 'order',order,'  product',product
        product.save()
        order.save()
        print'Sucess......................'
        return JsonResponse({'Msg': 'Success'}, status=200)








