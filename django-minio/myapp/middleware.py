from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.META['authorizationproxy'] = "123456"


def add_header_middleware(get_response):
    def middleware(request):
        request.META['authorizationproxy'] = '123456'
        response = get_response(request)
        response['world'] = 'hello'
        return response
    return middleware