def get_ip(request):
    address=request.META.get('HTTP_X_FORWARDED_FOR')
    if address:
        ip=address.split(',')[0].strip()
    else:
        ip=request.META.get('REMOTE_ADDR')
    return ip