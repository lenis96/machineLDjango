from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import pickle
from sklearn.neural_network import MLPClassifier
# Create your views here.

class PredictionAPIView(APIView):
    def get(self,request,prediction):
        model = pickle.load(open('models/xor.sav','rb'))
        res = model.predict([[0,0],[0,1],[1,0],[1,1]])
        return Response({'message':'ok','res':res})