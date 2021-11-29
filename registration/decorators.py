from django.http import HttpResponse, Http404
from django.shortcuts import redirect

# user kirmagan bo'lsagina signup va loginga ruxsat beradi, aks holda home ga 
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


# belgilangan rollarga ishlashga ruxsat beradi, masalan @allowed_users(allowed_roles=['admin']) ==> admin rolidagilarga 
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("Sizga bu sahifaga kirishga ruxsat yo'q !")
        return wrapper_func
    return decorator

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'foydalanuvchi':
			return redirect('user-page')

		if group == 'admin':
			return view_func(request, *args, **kwargs)

	return wrapper_function