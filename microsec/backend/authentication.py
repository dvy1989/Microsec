from rest_framework.authentication import BasicAuthentication


class NoPopupAuthentication(BasicAuthentication):
    def authenticate_header(self, request):
        return super(NoPopupAuthentication, self).authenticate_header(request).replace('Basic', 'xBasic')
