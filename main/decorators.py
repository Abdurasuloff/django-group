from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def allowed_groups(allowed_groups = []):
    def decorator(view_func):
        @login_required()
        def wrapper_func(request, *args, **kwargs):
            groups = request.user.groups.all()
            for group in groups:
                if group.name in allowed_groups:
                    return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("Access  Denied!")
        return wrapper_func
    return decorator        