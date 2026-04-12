def user_role(request):
    is_farmer = False
    if request.user.is_authenticated:
        try:
            is_farmer = request.user.farmer is not None
        except:
            is_farmer = False
    return {'is_farmer': is_farmer}