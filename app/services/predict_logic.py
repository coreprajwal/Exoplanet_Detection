import pickle
import numpy as np

with open("scalerpickle.pkl","rb") as f:
              scaler=pickle.load(f)

with open("forestpickle.pkl","rb") as m:
              forestmodel=pickle.load(m)



def predict_service(data):
       data=data.dict()
       input_data=np.array([[data[keys] for keys in data]])
       scaleddata=scaler.transform(input_data)
       result=forestmodel.predict(scaleddata)[0]
       probability=forestmodel.predict_proba(scaleddata)[0]
       
       if result==0:
              label="Not A Planet"
              confidence=float(probability[0])
       elif result==1:
              label="Confirmed Exoplanet"
              confidence=float(probability[-1])
       else:
              label="Error in Confirmation"
              confidence=0.0000
              
       
       finalresult={"label":label,"confidence":confidence}
       return finalresult