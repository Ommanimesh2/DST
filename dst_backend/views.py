from django.shortcuts import render
from django.http import HttpResponse
import json
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from rest_framework.response import Response
from rest_framework import status, filters
from dst_backend.settings import SITE_ROOT
import os
from rest_framework.views import APIView
class thisView(APIView):
    def get(self , request, *args, **kwargs):
        data_file_path = os.path.join(SITE_ROOT, r'static', 'apple_data.json')
        District='Kolkata'
        Market='Mechua'
        Commodity='Apple'
        print("Data file path is",data_file_path)
        DATA= json.load(open(data_file_path))
        print(DATA)
        month={'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
        data=[]
        for dic in DATA:
        #     break
            if (dic['District Name'] == District) and (dic['Market Name'] == Market):
                Date=dic['Price Date']
                Date=Date[-4:]+'-'+month[Date[3:6]]+'-'+Date[0:2]
                data.append([Date,dic['Modal Price (Rs./Quintal)']])
        data=sorted(data)
        i=0
        time_data=[]
        while( i<len(data)):
            j=i
            modal=0
            while(j<len(data) and data[i][0]==data[j][0]):
                modal+=int(data[j][1])
                j+=1
                time_data.append({'Price_Date':pd.to_datetime(data[i][0]),'Modal_Price_per_Quintal':modal//(j-i)})
                i=j
        df=pd.DataFrame.from_dict(time_data[-30:])
        df = df.set_index('Price_Date')

        date=df.index[int(len(df)*0.7)]
        train = df[df.index <= date]
        test = df[df.index >= date]
        y = train['Modal_Price_per_Quintal']
        p,q,r=2,2,2
        Error= 10000000000
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    ARIMAmodel = ARIMA(y, order = (a+1,b+1,c+1))
                    ARIMAmodel = ARIMAmodel.fit()
                    y_pred = ARIMAmodel.get_forecast(len(test.index))
                    y_pred_df = y_pred.conf_int(alpha = 0.05) 
                    y_pred_df["Predictions"] = ARIMAmodel.predict(start = y_pred_df.index[0], end = y_pred_df.index[-1])
                    y_pred_df.index = test.index
                    y_pred_out = y_pred_df["Predictions"] 
                    error = np.sqrt(mean_squared_error(test["Modal_Price_per_Quintal"].values, y_pred_df["Predictions"]))
                    if abs(error)<Error:
                        Error=error
                    p,q,r=a+1,b+1,c+1

        ARIMAmodel = ARIMA(df['Modal_Price_per_Quintal'], order = (p,q,r))
        ARIMAmodel = ARIMAmodel.fit()
        y_pred = ARIMAmodel.get_forecast(7)
        y_pred_df = y_pred.conf_int(alpha = 0.05) 
        price = ARIMAmodel.predict(start = df.index[-1]+ pd.Timedelta(1, unit='D'), end = df.index[-1]+ pd.Timedelta(7, unit='D'))
        
        date_price=dict()
        for i in range(len(price)):
            date= str(price.index[i])[:10]
            date_price[date]=int(price.iloc[i])

        return Response(data=date_price, status=status.HTTP_201_CREATED)


