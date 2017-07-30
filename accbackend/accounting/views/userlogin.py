from .imports import *


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def authenticate(usrid, login_token):
    try:
        Users.objects.get(id=usrid, login_token=login_token)
        return True
    except Users.DoesNotExist:
        return False


@csrf_exempt
def validate(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        try:
            model = Users.objects.get(
                Q(email=data['username']) | Q(phonenumber=data['username']), is_active=0, is_delete=0)
            print(data['password'])
            password = check_password(
                data['password'], model.password)
        except Users.DoesNotExist:
            data = {'Status': '404',
                    'message': 'Username and password were incorrect'}
            return JSONResponse(data)
        if model and password:
            unique_id = get_random_string(length=32)
            # Users.objects.filter(email=request.POST.get(
            #     'email')).update()
            model.login_token = unique_id
            model.save()
            # data1=request.POST.get('email')
            serializer = UsersSerializer(model)
            # tmp=JSONResponse(serializer.data)
            data = {'Status': '200', 'message': 'Login successful',
                    'user_details': serializer.data}
            # if request.POST.get('jobtypeId'):
            #     update_job_type(model.id, request.POST.get('jobtypeId'))
            #     data = {'Status': '200', 'message': 'Login successful',
            #             'user_details': serializer.data, "jobtypeId": request.POST.get('jobtypeId')}
            return JSONResponse(data)
        else:
            data = {'Status': '404',
                    'message': 'Username and password were incorrect'}
            return JSONResponse(data)
    else:
        data = {'Status': '500', 'message': 'Method should be POST'}
        return JSONResponse(data)

# To Check whether mobilenumber or email exists in the table


@csrf_exempt
def check_user(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        model = Users.objects.filter(
            Q(phonenumber=data['username']) | Q(email=data['username'])).exists()
        if model:
            result = {'Status': '200', 'message': 'User exists'}
            return JSONResponse(result)
        else:
            result = {'Status': '404', 'message': 'User not exists'}
            return JSONResponse(result)


@csrf_exempt
def signup(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = Signup(data=data,many=False)
        if serializer.is_valid():
            serializer.save()
            result = {"Status":"200","message":"Signup successful!!","data":serializer.data}
        else:
            result = {"Status":"500","errors":serializer.errors}
        return JSONResponse(result)


@csrf_exempt
def check_accountno(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        if 'account_no' in data:
            try:
                Users.objects.get(account_no=data['account_no'])
            except Users.DoesNotExist:
                result = {"Status":"200","message":"Account number is unique"}
                return JSONResponse(result)
            result = {"Status":"500","message":"Account number is not unique"}
            return JSONResponse(result)
        else:
            result = {"Status":"500","message":"Need Account number to check!!"}
            return JSONResponse(result)


@csrf_exempt
def sendemail(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        sendemail = 'info@exotigo.in'
        # sendemail = "ksathickali124045@gmail.com"
        from_email = 'ksathickali124045@gmail.com'
        name = data['name']
        surname = data['surname']
        city = data['city']
        country = data['country']
        email =data['email']
        phonenumber = data['phonenumber']
        message = data['message']
        # return HttpResponse(act_link)
        send_templated_mail(
            template_name='welcome',
            from_email=from_email,
            recipient_list=[sendemail],
            context={
                'name': name,
                'surname': surname,
                'city': city,
                'country': country,
                'email': email,
                'phone': phonenumber,
                'message': message
            },
        )
        print("mail sent")
    return HttpResponse('Success')