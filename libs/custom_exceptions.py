from rest_framework.exceptions import APIException


class AlreadyExistsException(APIException):
    status_code = 409
    default_detail = "Already Exists"


class InvalidInputDataException(APIException):
    status_code = 400
    default_detail = "Invalid Input Data"

    def __init__(self, message=None, *args, **kwargs):
        super(InvalidInputDataException, self).__init__(*args, **kwargs)


class VerificationException(APIException):
    status_code = 400
    default_detail = "User Not Active"


class InvalidCredentialsException(APIException):
    status_code = 401
    default_detail = "Invalid Credentials"


class UserNotAllowedException(APIException):
    status_code = 401
    default_detail = "User Not Allowed"


class UserExistsException(AlreadyExistsException):
    default_detail = "User Already Exists"


class UserDoesNotExistsException(APIException):
    status_code = 404
    default_detail = "User Does Not Exists"


class PasswordsDoNotMatchException(APIException):
    status_code = 400
    default_detail = "Passwords Don't Match"
