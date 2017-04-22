from django.test import TestCase
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect, render_to_response, RequestContext
from .models import *
from .forms import *
from django.http import HttpRequest
from medical_project.settings import *
from django.conf import settings
from django.utils.importlib import import_module


class ClientTest(TestCase):
    def create_user_object(self, username="me"):
        return User.objects.create(username=username)
