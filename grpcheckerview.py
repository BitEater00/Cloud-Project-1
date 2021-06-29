from django.contrib.auth.decorators import user_passes_test

def group_required(*group_name):
    def in_groups(u):
        if u.is_authenticated:
            if u.groups.filter(name__in = group_name).exists() | u.is_superuser:
                return True
        return False

    return user_passes_test(in_groups , login_url="/")

def group_not_required(*group_name):
    def in_groups(u):
        if u.is_authenticated:
            if u.groups.filter(name__in = group_name).exists():
                return False
        return True

    return user_passes_test(in_groups , login_url="/")