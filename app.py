# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 13:36:47 2023

@author: Dell
"""

import streamlit as st
import pickle


load = open('mod.pkl', 'rb')
model = pickle.load(load)



st.image("""https://rsigeeks.com/blog/wp-content/uploads/2022/10/Heatmap-Analysis-Customer-Churn-Rate2.jpg""")
st.title('Telecom Company Churn Predictor :running:')


def predict(voice_messages, intl_plan,
       day_mins,day_charge,  customer_calls):  
    pred = model.predict([[voice_messages, intl_plan,
           day_mins,day_charge,  customer_calls]])
    return pred

def start():
    voice_messages = st.number_input('Number of Voicemail Messages', min_value=0, max_value=43)
    intl_plan = st.selectbox('Do you have International :earth_asia: Plan?', ('Yes', 'No'))
    day_mins= st.number_input('Total minutes customer have used the service during daytime :mostly_sunny:',min_value=34.95, max_value=325.0)
    day_charge = st.number_input('Total charges for day time :mostly_sunny:', min_value=5.95, max_value=55.23)
    customer_calls= st.number_input('Total number of calls to customer care :phone:', min_value=0, max_value=4)
    
    
    if st.button('Predict'):
        result = predict(voice_messages, intl_plan,
               day_mins,day_charge,  customer_calls)
        st.success('Will customer Churn? : {} '.format(result) )
        
if __name__== '__main__':
    start()
        
    
    
    