import pandas as pd                 
from flask import Flask, request, Response
import requests
import pickle
from rossmann.Rossmann import Rossmann

# loading model
model = pickle.load(open('C:/Users/leogr/OneDrive/Documentos/Data Science Projects/Portfolio projects/store-sales-prediction/Model/store_sales_prediction_model.pkl', 'rb'))

# initialize API
app = Flask(__name__)

@app.route('/rossmann/predict', methods=['POST'])
def rossmann_predict():
    test_json = request.get_json()
    
    if test_json:
        if isinstance(test_json): # unique example
            test_raw = pd.DataFrame(test_json, index=[0])
        else: # multiple exemples
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())
        
        # instance rossmann class
        pipeline = Rossmann()
        
        # data cleaning
        df1 = pipeline.data_cleaning(test_raw)
        
        # feature engineering
        df2 = pipeline.feature_engineering(df1)
        
        # data preparation
        df3 = pipeline.data_preparation(df2)
        
        # prediction
        df_response = pipeline.get_prediciton(model, test_raw, df3)
        
        return df_response
        
    else:
        return Response('{}', status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run('0.0.0.0')                                                                                                                                       