from rest_framework.views import APIView
from django.shortcuts import render , HttpResponse
from rest_framework.response import Response
from bot.models import Subject ,Book
import json

def searchbook(request):
    if request.method == "POST":
        title = request.POST.get("Title").upper().strip()
        for book in Book.objects.all():
            if book.Title == title:
                return HttpResponse({"found"})
            
        return HttpResponse({"not found"})
    return render(request,'search.html')

def TitleStrip(request):
    for book in Book.objects.all():
        book.Title = book.Title.strip()
        book.save(force_update=True)
    return HttpResponse({"leading and trailing whitespaces are removed"})

def chatInterface(request):
    return render(request,'chatbot.html')

class WebHook(APIView):
    def post(self, request):

        print(json.dumps(request.data, indent=2))

        if request.data["queryResult"]["intent"]["displayName"] == "checkAvailability":
            textResponse = []
            title = request.data["queryResult"]["parameters"]["title"][0].split('\"')[1].upper().strip()
            for book in Book.objects.all():
                if book.Title == title:
                    return Response({"fulfillmentMessages": [{"text": {"text": [book.Title+" is available at the library"]}}]})
            return Response({"fulfillmentMessages": [{"text": {"text": ["book is not available at the library"]}}]})

        if request.data["queryResult"]["intent"]["displayName"] == "getListSubjects":
            textResponse = []

            for subject in Subject.objects.all():
                textResponse.append({"text": {"text": [subject.name]}})

            return Response({"fulfillmentMessages": textResponse})

        if request.data["queryResult"]["intent"]["displayName"] == "checkAvailability":
            textResponse = [{"text": {"text": "from the other side at checkavailability"}}]
            return Response({'fulfillmentMessages': textResponse})

        subjectCodes = request.data["queryResult"]["parameters"]["subject"]

        responseText = []

        for code in subjectCodes:
            try:
                subject = Subject.objects.get(name=code)
                if subject.documents:
                    for document in subject.documents.all():
                        responseText.append({"text": {"text": [document.url]}})
                else:
                    responseText.append({"text": {"text": ["not available on the other side"]}})
            except Exception as e:
                responseText.append({"text": {"text": [str(e)]}})

        return Response({"fulfillmentMessages": responseText})