from rest_framework.views import APIView
from rest_framework.response import Response

class SystemView(APIView):
    def post (self, request ,services ,format = None):
        print("----------------------")
        if services == 'pdftoinvoice':
            print("----------------------")
            files = request.FILES
            print("----------------------")
            print(files)
            print("----------------------")
        return Response(status = 200)
