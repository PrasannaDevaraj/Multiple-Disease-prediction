# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 22:01:57 2023

@author: PRASANNA
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved model

diabeticprediction_model = pickle.load(open('C:/Users/PRASANNA/OneDrive/Desktop/Multiple prediction system/Saved Models/diabeticprediction_model.sav','rb'))

heartdisease_model = pickle.load(open('C:/Users/PRASANNA/OneDrive/Desktop/Multiple prediction system/Saved Models/heartdisease_model.sav','rb'))

BreastCancerprediction_model = pickle.load(open('C:/Users/PRASANNA/OneDrive/Desktop/Multiple prediction system/Saved Models/BreastCancerprediction_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/PRASANNA/OneDrive/Desktop/Multiple prediction system/Saved Models/parkinsons_model.sav','rb'))


#sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Preamptive Model for Multiple Disease Prediction',
                           ['Diabetics Prediction',
                            'Chronic Heart Disease Prediction',
                            'Breast Cancer Prediction',
                            'Parkinsons Prediction'],
                           
                           icons = ['activity','heart','headset-vr','person'],
                          
                           default_index = 1)

#Diabetics Prediction
if(selected == 'Diabetics Prediction'):

    #page title
    st.title('Diabetics Prediction using Machine Learning')
    
    
    Pregnancies = st.text_input("Number of Pregnancies")
    Glucose = st.text_input("Glucose level")
    BloodPressure = st.text_input("Blood Pressure value")
    SkinThickness = st.text_input("Skin Thickness value")
    Insulin = st.text_input("Insulin level")
    BMI = st.text_input("BMI value")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")
    Age = st.text_input("Age of the person")
    
    #code for prediction
    diab_diagnosis = ''
    
    #creating a button for prediction
    
    if st.button("Diabetics test result"):
        diab_prediction = diabeticprediction_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if(diab_prediction[0]==1):
            diab_diagnosis = "The person is diabetic"
        else:
            diab_diagnosis = "The person is not Diabetic"
            
    st.success(diab_diagnosis)


#Chronic Heart Disease Prediction
if(selected == 'Chronic Heart Disease Prediction'):

    #page title
    st.title('Chronic Heart Disease Prediction using Machine Learning')
    
    
    Age = st.number_input("Age of the person")
    Sex = st.number_input("Gender of the person")
    cp = st.number_input("Chest pain from 1-4")
    trestbps = st.number_input("Resting blood pressure value")
    chol = st.number_input("Serum cholestoral in mg/dl")
    fbs = st.number_input("Fasting blood sugar level")
    restecg = st.number_input("resting electrocardiographic results")
    thalach = st.number_input("Maximum heart rate achieved")
    exang = st.number_input("Exercise induced angina")
    oldpeak = st.number_input("Old peak value")
    slope = st.number_input("The slope of the peak value")
    ca = st.number_input("Number of major blood vessels")
    thal = st.number_input("Heart rate")  
    
    #code for prediction
    heart_diagnosis = ''
    
    #creating a button for prediction
    
    if st.button("Heart test result"):
        heart_prediction = heartdisease_model.predict([[Age, Sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if(heart_prediction[0]==1):
            heart_diagnosis = "The person sufers from heart disease"
        else:
            heart_diagnosis = "The person is healthy"
    st.success(heart_diagnosis)    
    
    
#Breast Cancer Prediction
if(selected == 'Breast Cancer Prediction'):

    #page title
    st.title('Breast Cancer Prediction using Machine Learning')
    
    meanradius = st.number_input("Mean radius") 
    meantexture = st.number_input("Mean texture")
    meanperimeter = st.number_input("Mean perimeter")
    meanarea = st.number("Mean area")
    meansmoothness = st.number_input("Mean smoothness")
    meancompactness = st.number_input("Mean compactness")
    meanconcavity = st.number_input("Mean concavity")
    meanconcavepoints = st.number_input("Mean concave points")
    meansymmetry = st.number_input("Mean symmetry")
    meanfractaldimension = st.number_input("Mean fractal dimension")
    radiuserror = st.number_input("Radius error")
    textureerror = st.number_input("Texture error")
    perimetererror =st.number_input("Perimeter error")
    areaerror = st.number_input("area error")
    smoothnesserror = st.number_input("Smoothness error")
    compactnesserror = st.number_input("Compactness error")
    concavityerror = st.number_input("Concavity error")
    concavepointserror = st.number_input("Concave points error")
    symmetryerror = st.number_input("Symmetry error")
    fractaldimensionerror = st.number_input("Fractal dimension error")
    worstradius = st.number_input("Worst radius")
    worsttexture = st.number_input("Worst texture")
    worstperimeter = st.number_input("Worst perimeter")
    worstarea = st.number_input("Worst area")
    worstsmoothness = st.number_input("Worst smoothness")
    worstcompactness = st.number_input("Worst compactness")
    worstconcavity = st.number_input("Worst concavity")
    worstconcavepoints = st.number_input("Worst concave points")
    worstsymmetry = st.number_input("Worst symmetry")
    worstfractaldimension = st.number_input("Worst fractal dimensions")
    
    #code for prediction
    BC_diagnosis = ''
    
    #creating a button for prediction
    
    if st.button("Breast Cancer test result"):
        BC_prediction = BreastCancerprediction_model.predict([[meanradius, meantexture, meanperimeter, meanarea,
                                                                 meansmoothness, meancompactness, meanconcavity, meanconcavepoints,
                                                                 meansymmetry,meanfractaldimension, radiuserror, textureerror, perimetererror, 
                                                                 areaerror, smoothnesserror, compactnesserror, concavityerror, 
                                                                 concavepointserror, symmetryerror, fractaldimensionerror, 
                                                                 worstradius, worsttexture, worstperimeter, worstarea, worstsmoothness, 
                                                                 worstcompactness, worstconcavity, worstconcavepoints, worstsymmetry,
                                                                 worstfractaldimension]])
        
        if(BC_prediction[0]==1):
            BC_diagnosis = "The person sufers from Breast Cancer"
        else:
            BC_diagnosis = "The person is healthy"
    st.success(BC_diagnosis)   
    
      
#Parkinsons Prediction
if(selected == 'Parkinsons Prediction'):

    #page title
    st.title('Parkinsons Prediction using Machine Learning')
    
    MDVPFoHz = st.text_input("MDVPFo(Hz)")
    MDVPFhiHz = st.text_input("MDVPFhi(Hz)")
    MDVPFloHz = st.text_input("MDVPFlo(Hz)")
    MDVPJitter = st.text_input("MDVPJitter(%)")
    MDVPJitterAbs = st.text_input("MDVPJitter(Abs)")
    MDVPRAP = st.text_input("MDVPRAP")
    MDVPPPQ = st.text_input("MDVPPPQ")
    JitterDDP = st.text_input("MDVPDDP")
    MDVPShimmer = st.text_input("MDVPShimmer")
    MDVPShimmerdB = st.text_input("MDVPShimmer(dB)")
    ShimmerAPQ3 = st.text_input("ShimmerAPQ3")
    ShimmerAPQ5 = st.text_input("ShimmerAPQ5")
    MDVPAPQ = st.text_input("MDVPAPQ")
    ShimmerDDA = st.text_input("ShimmerDDA") 
    NHR = st.text_input("NHR")
    HNR = st.text_input("HNR")
    RPDE = st.text_input("RPDE")
    DFA = st.text_input("DFA")
    spread1 = st.text_input("spread1")
    spread2 = st.text_input("spread2")
    D2 = st.text_input("D2")
    PPE = st.text_input("PPE") 
    
    #code for prediction
    park_diagnosis = ''
    
    #creating a button for prediction
    
    if st.button("Parkinson Disease test result"):
        park_prediction = parkinsons_model.predict([[MDVPFoHz, MDVPFhiHz, MDVPFloHz, MDVPJitter, MDVPJitterAbs, 
                                                     MDVPRAP, MDVPPPQ, JitterDDP, MDVPShimmer, MDVPShimmerdB, ShimmerAPQ3,ShimmerAPQ5, 
                                                     MDVPAPQ, ShimmerDDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        
        if(park_prediction[0]==1):
            park_diagnosis = "The person sufers from Parkinsons Disease"
        else:
            park_diagnosis = "The person is healthy"
    st.success(park_diagnosis)   
        


    