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
def validate(request, format=None):
    if request.POST:
        try:
            model = Users.objects.get(
                email=request.POST.get('email'), is_active=1, is_delete=0)
            password = check_password(
                request.POST.get('password'), model.password)
        except Users.DoesNotExist:
            data = {'Status': '404',
                    'message': 'Username and password were incorrect'}
            return JSONResponse(data)
        if model and password:
            unique_id = get_random_string(length=32)
            Users.objects.filter(email=request.POST.get(
                'email')).update(login_token=unique_id)
            # data1=request.POST.get('email')
            user_details = Users.objects.get(email=request.POST.get('email'))
            serializer = UsersSerializer(user_details)
            # tmp=JSONResponse(serializer.data)
            data = {'Status': '200', 'message': 'Login successful',
                    'user_details': serializer.data}
            if request.POST.get('jobtypeId'):
                update_job_type(model.id, request.POST.get('jobtypeId'))
                data = {'Status': '200', 'message': 'Login successful',
                        'user_details': serializer.data, "jobtypeId": request.POST.get('jobtypeId')}
            return JSONResponse(data)
        else:
            data = {'Status': '404',
                    'message': 'Username and password were incorrect'}
            return JSONResponse(data)
    else:
        data = {'Status': 'fail', 'message': 'Invalid'}
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