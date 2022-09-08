#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import joblib
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from numpy import outer
from PIL import Image

model = joblib.load('customer.pkl')


def web_app():

    st.write("""
    # Customer Behaviour Analysis with Machine Learning
    ## This app predicts to which category a customer belongs too
   """)
    image = Image.open('customer_pic.png')

    st.image(image, caption='Customer Behaviour Analysis')
    st.header("User Details")
    st.subheader("Kindly Enter The following Details in order to make a prediction")

    Income = st.number_input("Income",1500,120000)
    Age = st.number_input("AGE",19,80)
    year = st.number_input("year",2005,2020)
    month = st.number_input("month",1,20)
    Month_Customer = st.number_input("Month_Customer",12,50)
    TotaSpendings = st.number_input("TotaSpendings",5,3000)
    Children = st.number_input("Children",0,3)
    
    if st.button("Press here to make Prediction"):
        
        result = model.predict([[Income,Age,year,month,Month_Customer,TotaSpendings,Children]])
        if result == 0:
            result = "CATEGORY_D"
        elif result == 1: 
            result = "CATEGORY_A"
        elif result == 2: 
            result = "CATEGORY_B"
        else : 
            result = "CATEGORY_C"
        
        
        st.text_area(label='Category belongs to:- ',value=result , height= 100)
         
    
    
run = web_app()







