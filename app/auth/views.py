from flask import render_template, url_for, flash, redirect, request, abort
from . import auth
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db
from flask_login import login_user, current_user, logout_user