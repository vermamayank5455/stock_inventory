from django.http import HttpResponseRedirect



def authorized_user(function = None):

    def wrap(request, *args, **kwargs):
        try:
            user_name = request.COOKIES['username']
            return function(request, *args, **kwargs)
        except:
            return HttpResponseRedirect("/admin-se/loginform/")


    return wrap