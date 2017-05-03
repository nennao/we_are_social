from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


@csrf_exempt
def paypal_return(request):
    args = {'post': request.POST, 'get': request.GET}
    return render(request, 'paypal/paypal_return.html', args)

# got a get thing
# GET
# <QueryDict: {u'auth': [u'AqDeYFehPsE3GkjQx9YntsnWM5P9gkndqNDr.rY0C5yw.Yj2DYk5xt-CEJ9oww1nr2RqVg.lLoP4tKKlv.2WcNA'], u'form_charset': [u'UTF-8']}>


def paypal_cancel(request):
    args = {'post': request.POST, 'get': request.GET}
    return render(request, 'paypal/paypal_cancel.html', args)
