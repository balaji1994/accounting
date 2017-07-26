from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# from childcare.models import (
#     Users, JobType, JobAddress, JobTime_Budget, JobRequirements, Postal_code, Cities)
# from childcare.serializers import UsersSerializer, JobtypeSerializer, JobAddressSerializer, JobTime_BudgetSerializer, JobRequirementsSerializer
from accounting.models import (Users)
from accounting.serializers import (UsersSerializer) 
from django.shortcuts import render
from templated_email import send_templated_mail
from templated_email import InlineImage
# from hrmsv2.settings import FRONT_URL
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.core.signing import Signer
from django.core.mail import send_mail
# from rest_framework.test import APIRequestFactory
from django.core.files import uploadedfile
from django.core.files import uploadhandler
from rest_framework import generics
from datetime import datetime
from django.db.models import Q
from django.db.models import Sum
import dateutil.parser
import os
# import datetime
import json
import base64

from django.utils.crypto import get_random_string
