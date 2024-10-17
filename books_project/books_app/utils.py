# books_app/exception.py

from rest_framework.exceptions import PermissionDenied, NotFound, ValidationError
from rest_framework import status
from rest_framework.response import Response  # Correctly importing Response


def exception_handler(exc, context):
    headers = None
    message_code = None
    print(f"Exception: {exc}, Context: {context}")  # Debug print


    if isinstance(exc, NotFound):
        message_detail = 'Not found.'
        status_code = status.HTTP_404_NOT_FOUND

    elif isinstance(exc, PermissionDenied):
        message_detail = 'Permission denied.'
        status_code = status.HTTP_403_FORBIDDEN
    elif isinstance(exc, ValidationError):
        message_detail = 'validation error.'
        status_code = status.HTTP_400_BAD_REQUEST
    else:
        message_detail = str(exc)
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    # Return the Response object correctly
    return Response(
        {
            "message_code": message_code,
            "message_detail": message_detail
        },
        status=status_code,
        headers=headers,
        exception=True
    )


def harri_exception_handler(exc, context):
    response = exception_handler(exc, context)
    return response


