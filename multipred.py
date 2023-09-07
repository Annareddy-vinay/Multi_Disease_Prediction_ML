# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 11:14:56 2023

@author: annar
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
diabeties_model=pickle.load(open('C:/Users/annar/OneDrive/ML/multi_pred/saved_files/diabeties.sav','rb'))
heart_model=pickle.load(open('C:/Users/annar/OneDrive/ML/multi_pred/saved_files/heart disease.sav','rb'))
kidney_model=pickle.load(open('C:/Users/annar/OneDrive/ML/multi_pred/saved_files/kidney disease.sav','rb'))
parkisons_model=pickle.load(open('C:/Users/annar/OneDrive/ML/multi_pred/saved_files/parkisons.sav','rb'))
with st.sidebar:
    select=option_menu('MULTI-DISEAES-PREDICTION-SYSTEM',
                       ['HEART DISEASE','DIABETIES','KIDNEY','PARKISONS'],default_index=0)

        

if select=="HEART DISEASE":
    st.title("Heart disease prediction using ML")
    age=st.text_input("Enter age")
    Gender=st.radio("Gender",["male","female"])
    if Gender=="male":
        sex=1
    else:
        sex=0
    cp=st.radio("Chest pain",["Typical angina","Atypical angina","Non-anginal pain"
                              ,"Asymptomatic"])
    if cp=="Typical angina":
        cp=0
    elif cp=="Atypical angina":
        cp=1
    elif cp=="Non-anginal pain":
        cp=2
    else:
        cp=3
    trestbps=st.text_input("Enter Resting blood pressure(in mmHg)")
    chol=st.text_input("Enter Cholesterole")
    fbs=st.radio("Fasing blood sugar",[">120","<120"])
    if fbs==">120":
        fbs=1
    else:
        fbs=0
    restecg=st.radio("Resting electrocardiogram result",["Normal","Abnormal"])
    if restecg=="Normal":
        restecg=0
    else:
        restecg=1
    thalach=st.text_input("Enter Heart rate achieved")
    exang=st.radio("Exercise include angia",["Yes","No"])
    if exang=="Yes":
        exang=1
    else:
        exang=0
    oldpeak=st.text_input("Enter oldpeak")
    slope=st.radio("Slope",["Upsloping","Flat","Downsloping"])
    if slope=="Upsloping":
        slope=0
    elif slope=="Flat":
        slope=1
    else:
        slope=2
    ca=st.radio("Major vessels",["0","1","2"])
    thal=st.radio("Thallium level",["Normal","Fixed","Reversible defect"])
    if thal=="Normal":
        thal=1
    elif thal=="Fixed":
        thal=2
    else:
        thal=3
    Hrt_pred=''
    if st.button("Heart Disease Test Result:"):
        Hrt_pred=heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,
                                       thalach, exang,oldpeak,slope,ca,thal]])
    if Hrt_pred==1:
        Hrt_pred="You have Heart disease problem"
    elif Hrt_pred==0:
        Hrt_pred="You don't have any Heart problem"
        st.balloons()
    st.success(Hrt_pred)
if select =="DIABETIES":
    st.title("Diabeties prediction using ML")
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.text_input("Enter number of pregnancies")
    with col2:
        Glucose=st.text_input("Enter Glucose level")
    with col3:
        BloodPressure=st.text_input("Enter BloodPressure")
    with col1:
        Skin_Thickness=st.text_input("Enter Skin thickness")
    with col2:
        Insulin=st.text_input("Enter insulin")
    with col3:
        BMI=st.text_input("Enter BMI")
    with col1:
        DP=st.text_input("Enter DiabetiesPedigree function value")
    with col2:
        Age=st.text_input("Enter AGE")
    Diab_pred=''
    if st.button("Diabeties Test Result:"):
        Diab_pred=diabeties_model.predict([[Pregnancies,Glucose,BloodPressure,
                            Skin_Thickness,Insulin,BMI,DP,Age]])
    if Diab_pred==1:
        Diab_pred="You have Diabeties problem"
    elif Diab_pred==0:
        Diab_pred="You don't have any diabeties problem"
        st.balloons()
    st.success(Diab_pred)
if select =="KIDNEY":
    st.title("Kidney prediction using ML")
    col1,col2,col3=st.columns(3)
    with col1:
        Age=st.text_input("Enter AGE")
    with col2:
        bp=st.text_input("Enter Blood pressure(BP)")
    with col3:
        sg=st.text_input("Enter specific gravity(SG)")
    with col1:
        al=st.text_input("Enter Albumin(AL)")
    with col2:
        su=st.text_input("Enter Sugar(SU)")
    with col3:
        rbc=st.radio("Red blood cells(RBC)",["Normal","AbNormal"])
        if rbc=="Normal":
            rbc=1
        else:
            rbc=0
    with col1:       
        pc=st.radio("Pus cell(PC)",["Normal","AbNormal"])
        if pc=="Normal":
            pc=1
        else:
            pc=0
    with col2:
        pcc=st.radio("Pus cell Clumps(PCC)",["present","Notpresent"])
        if pcc=="present":
            pcc=1
        else:
            pcc=0
    with col3:
        ba=st.radio("Bacteria(BA)",["present","Notpresent"])
        if ba=="present":
            ba=1
        else:
            ba=0
    with col1:
        bgr=st.text_input("Enter Blood glucose random(BGR)")
    with col2:
        bu=st.text_input("Enter Blood urea(BU)")
    with col3:
        sc=st.text_input("Enter Serum creatinine(SC)")
    with col1:
        sod=st.text_input("Enter Sodium")
    with col2:
        pot=st.text_input("Enter Potassium")
    with col3:
        hemo=st.text_input("Enter Hemoglobin")
    with col1:
        pcv=st.text_input("Enter Packed cell volume(PCV)")
    with col2:
        wc=st.text_input("Enter White blood cell count(WC)")
    with col3:
        rc=st.text_input("Enter Red blood cell count(RC)")
    with col1:
        htn=st.radio("Hypertension",["Yes","No"])
        if htn=="Yes":
            htn=1
        else:
            htn=0
    with col2:
        dm=st.radio("Diabeties mellitus(DM)",["Yes","No"])
        if dm=="Yes":
            dm=1
        else:
            dm=0
    with col3:
        cad=st.radio("Coronary artery diseas(CAD)e",["Yes","No"])
        if cad=="Yes":
            cad=1
        else:
            cad=0
    with col1:
        appet=st.radio("Appetite",["Good","Poor"])
        if appet=="Good":
            appet=1
        else:
            appet=0
    with col2:
        pe=st.radio("Pedal edema(PE)",["Yes","No"])
        if pe=="Yes":
            pe=1
        else:
            pe=0
    with col3:
        ane=st.radio("Anemia",["Yes","No"])
        if ane=="Yes":
            ane=1
        else:
            ane=0
    kid_pred=''
    if st.button("Kidney Disease Test result:"):
        kid_pred=kidney_model.predict([[Age,bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,
                        sc,sod,pot,hemo,pcv,wc,htn,dm,cad,appet,pe,ane]])
    if kid_pred==1:
        kid_pred="You have Kidney disease problem"
    elif kid_pred==0:
        kid_pred="You don't have any Kidney disease problem"
        st.balloons()
    st.success(kid_pred)
if select =="PARKISONS":
    st.title("parkisons prediction using ML")
    col1,col2,col3=st.columns(3)
    with col1:
        fo=st.text_input("Enter Average Vocal fundamental frequency(HZ)(FO)")
    with col2:
        fhi=st.text_input("Enter Maximum Vocal fundamental frequency(HZ)(FHI)")
    with col3:
        flo=st.text_input("Enter Minimum Vocal fundamental frequency(HZ)(FLO)")
    with col1:
        jitter1=st.text_input("Enter Jitter(in %)")
    with col2:
        jitter2=st.text_input("Enter Absolute Jitter")
    with col3:
        rap=st.text_input("Enter Relative amplitude penatration(RAP)")
    with col1: 
        ppq=st.text_input("Enter Period perturbation quotient(PPQ")
    with col2:
        ddp=st.text_input("Enter Difference B/W jitters(DDP)")
    with col3:
        shimmer1=st.text_input("Enter Local shimmer")
    with col1:
        shimmer2=st.text_input("Enter Local shimmer(in dB")
    with col2:
        shimmer3=st.text_input("Enter 3-point APQ")
    with col3:
        shimmer4=st.text_input("Enter 5-point APQ")
    with col1:
        apq11=st.text_input("Enter 11-point Amplitude petrurbation quotient(APQ)")
    with col2:
        shimmer5=st.text_input("Enter Difference B/W amplitudes(DDA)")
    with col3:
        nhr=st.text_input("Enter Noise/Hormonic(ratio)(NHR)")
    with col1:
        hnr=st.text_input("Enter Hormonic/Noise(ratio)(HNR)")
    with col2:
        rpde=st.text_input("Enter Period density entropy(RPDE)")
    with col3:
        d2=st.text_input("Enter correlation dimension(D2)")
    with col1:
        dfa=st.text_input("Enter Detrended fluctuation analysis(DFA)")
    with col2:
        sp1=st.text_input("Enter Nonlinear measures(Spread1)")
    with col3:
        sp2=st.text_input("Enter Frequency variation(Spread2)")
    with col1:
        ppe=st.text_input("Enter Pitch period entropy(PPE)")
    park_pred=''
    if st.button("parkisons Disease Test result:"):
        park_pred=parkisons_model.predict([[fo,fhi,flo,jitter1,jitter2,rap,ppq,
                            ddp,shimmer1,shimmer2,shimmer3,shimmer4,apq11,
                            shimmer5,nhr,hnr,rpde,d2,dfa,sp1,sp2,ppe]])
    if park_pred==1:
        park_pred="You have Parkisons problem"
    elif park_pred==0:
        park_pred="You don't have any parkisons problem"
        st.balloons()
    st.success(park_pred)
    
    