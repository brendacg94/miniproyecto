from django.contrib import admin
from users.models import *
from Bank_account.models import *
from Bank.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Bank_account)
admin.site.register(Bank)

