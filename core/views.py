from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from datastore.models import Dataset
from modelstore.models import DataModel

# ml imports
import io
import pickle
import csv
import pandas as pd
import numpy as np
import sklearn
from tools.col_maneged import col_reset
from tools.insurance_preprocessing import estimate


@api_view(['POST'])
def train(request):
    user=request.GET.get("user",None)
    target_column=request.GET.get("target_column",None)
    data_set=request.GET.get("data_set",None)
    if user and target_column and data_set:

        query=Dataset.objects.get(user=user,id=data_set)
        file_address = query.path.file
        data=[]
        with open(str(file_address), 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)

        df = pd.DataFrame(data=data)
        final_df = col_reset(df)
        train_model = estimate(final_df)
        filename='media/model/model.sav'
        # filename = 'model.sav'
        file=pickle.dump(train_model, open(filename, 'wb'))
        print(type(file))
        new_obj=DataModel.objects.create(
            dataset=query,
            name="data model",
            path='/model/model.sav'
        )
        new_obj.save()

        model_data=pickle.dumps(train_model)

        return Response('', status=status.HTTP_200_OK)




@api_view(['POST'])
def test(request):
    user=request.GET.get("user",None)
    data_model=request.GET.get("data_model",None)
    value=request.GET.get("value",None)
    if user and data_model and value:
        try:
            query=DataModel.objects.get(listing__user=user,id=data_model)
            csv_file_path=query.path
            # write logic
        except:
            return Response('fail', status_code=status.HTTP_400_BAD_REQUEST)

    else:
        return Response('fail', status_code=status.HTTP_400_BAD_REQUEST)
