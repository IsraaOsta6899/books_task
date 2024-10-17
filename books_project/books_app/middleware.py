# myapp/middleware.py
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden
from django.middleware.csrf import get_token

class CustomCsrfMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("")
        # if request.method in ['POST', 'PUT', 'DELETE']:
        #     # Check for the CSRF token in the headers
        #     csrf_token = request.META.get('X-CSRFToken')

        #     # Compare the CSRF token in the headers with the token stored in the session
        #     if not csrf_token:
        #         print("____________________________________________________")
        #         print(csrf_token)
        #         return HttpResponseForbidden("CSRF token missing or incorrect.")

        # return None  # Proceed to the next middleware or view

    # def process_response(self, request, response):
    #     # Optionally set a CSRF token in the response for clients
    #     response['X-CSRFToken'] = get_token(request)
    #     return response
