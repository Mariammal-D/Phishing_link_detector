import streamlit as st
import machine_learning as ml
import feature_extraction as fe
from bs4 import BeautifulSoup
import requests as re
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score 

# col1, col2 = st.columns([1, 3])

st.title('Phishing link Detector')



    


model = ml.ab_model
    


url = st.text_input('Enter the URL')
# check the url is valid or not
if st.button('Check!'):
    try:
        response = re.get(url, verify=False, timeout=4)
        if response.status_code != 200:
            st.write(". HTTP connection was not successful for the URL: ", url)
        else:
            soup = BeautifulSoup(response.content, "html.parser")
            vector = [fe.create_vector(soup)]  # it should be 2d array, so I added []
            result = model.predict(vector)
            print(result)
           
            if result[0] == 0:
                st.success("Safe to use!!!!")
                
            else:
                st.warning("Phishing website ...!!")
                
    except re.exceptions.RequestException as e:
        st.warning("Phishing website ...!!")





