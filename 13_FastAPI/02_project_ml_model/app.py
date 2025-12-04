from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd

# import the ml model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

tier_1_cities = ["Lahore", "Islamabad", "Peshawar", "Karachi"]
tier_2_cities = ["Mardan", "Quetta", "Faisalabad","Rawalpindi","Multan","Sialkot","Gujranwala","Hyderabad","Sukkur","Bahawalpur",
    "Sargodha","Abbottabad","Haripur","Swat","Kohat","Dera Ghazi Khan","Okara","Sheikhupura","Rahim Yar Khan","Chiniot"]


# pydantic model to validate incoming data
class UserInput(BaseModel):

    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the user")]
    height: Annotated[float, Field(..., gt=0, lt=2.5, description="Height of the user")]
    income_lpa: Annotated[float, Field(..., gt=0, description='Amount salary of the user in lpa')]
    smoker: Annotated[bool, Field(..., description='Is the user smoker')]
    city: Annotated[str, Field(..., description='The city that the user belongs to')]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'goverment_job', 'business_owner', 'unemployed', 'private_job'], Field(..., description='Occupation of the user')]


    @computed_field(return_type=float)
    @property
    def bmi(self):
        return self.weight/(self.height **2)
    
    @computed_field(return_type=str)
    @property
    def lifestyle_risk(self):
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker and self.bmi > 27:
            return "medium"
        else:
            return "low"
        
    @computed_field(return_type=str)
    @property
    def age_group(self):
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"
    
    @computed_field(return_type=int)
    @property
    def city_tier(self):
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
        

# /predict endpoint
@app.post('/predict')
def predict_premium(data: UserInput):

    input_df = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }])

    prediction = model.predict(input_df)[0]

    return JSONResponse(status_code=200, content={'predicted_category': prediction})