from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response


class CorsCustomMiddleware(MiddlewareMixin):
    # def process_response(self, request, response):
    #     if response is not None:
    #         print("got here")
    #         response['Access-Control-Allow-Origin'] = '*'
    #         print(response)
    #         return response

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # response['Access-Control-Allow-Origin'] = "http://localhost:3000"
        print(response.status_code)
        return response
        # return Response(response.data,status= response.status_code, headers={'Access-Control-Allow-Origin': 'http://localhost:3000'})
