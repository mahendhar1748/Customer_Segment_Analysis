import numpy as np
import pandas as pd
import pickle
import streamlit as st

# Loading the saved model

loaded_model = pickle.load(open("M:/Customer_project/Trained_model.pkl","rb"))

# Creating a function for output Prediction

def customer_prediction(input_data):
    #Changing input Data to Numpy array
    input_data_np=np.asarray(input_data)
    # Re-shaping the array as we predicting for one instance
    input_data_reshaped = input_data_np.reshape(1,-1)
    # Predicting for loaded model
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    for i in range(0,5):
        if (prediction[0] == i):
            return "The Given Customer is Falling in {} Cluster Segment".format(i)
        else:
            return "Unable to predict Please Check the Given input parameters"

# Creating Function for input Parameters

def main():

    # Giving Title to Web page
    st.title("Customer Personality Analysis")
    html_temp = """
    <div style ="background-color:orange;padding:10px">
     <h3 style = "color:black;text-align:center;"> Customer Segment Analysis ML  Web App </h2>
    </div> """
    st.markdown(html_temp,unsafe_allow_html=True)

    #-------------------------------------------------------
    # ----------------   Giving Input Parameters  ----------
    #-------------------------------------------------------

    
    Year_Birth = st.text_input("Enter Year of Birth",max_chars=4,help="Please enter exactly 4 digits")

    # Dropdown menu for education levels
    col7,col8 = st.columns(2)
    education_level = col7.selectbox('Select your education level:',('2n_Cycle', 'Basic', 'Graduation', 'Master', 'PhD'))
    # Mapping education levels to their respective outputs
    education_mapping = {'2n_Cycle': 0,'Basic': 1,'Graduation': 2,'Master': 3,'PhD': 4}
    # Get the corresponding output based on the selected education level
    output = education_mapping.get(education_level)

    # Marriage Status
    Living_Status = col8.selectbox('Select your Living Status:',('Absurd', 'Alone', 'Divorced', 'Married', 'Single','Together','Widow','Yolo'))
    Live_mapping = {'Absurd': 0,'Alone': 1,'Divorced': 2,'Married': 3,'Single': 4,'Together': 5,'Widow': 6,'Yolo': 7}
    output_1 = Live_mapping.get(Living_Status)
    
    #Income
    col1,col2 = st.columns(2)
    col9,col10 = st.columns(2)
    Income = col9.text_input("Enter Income",max_chars=6,help="Please enter income below 10 Lakhs")
    # Kids at home
    Kids = col1.text_input("Enter Kids at home",max_chars=1,help="Please enter below 3 ")
    # Teen at home
    Teen = col2.text_input("Enter Teens at home",max_chars=1,help="Please enter below 3 ")

    # Deals Purchasing through differnet platform
    col11,col12 = st.columns(2)
    No_Purchase = col11.text_input("No of Deals Purchased",max_chars=2,help="Please enter below 15")
    col3,col4 = st.columns(2)
    col5,col6 = st.columns(2)
    No_web_Purchase = col3.text_input("Deals Purchased through wbsite",max_chars=2,help="Please enter below 30")
    No_Cat_Purchase = col4.text_input("Deals Purchased through catlogue",max_chars=2,help="Please enter below 30")
    No_Store_Purchase = col5.text_input("Deals Purchased through Sotre",max_chars=2,help="Please enter below 30")
    No_web_visits = col6.text_input("No of web visits ",max_chars=2,help="Please enter below 30")

    # Acceptance criteria of Discounts
    if 'discounts' not in st.session_state:
        st.session_state.discounts = {'AcceptedCmp3': 0, 'AcceptedCmp4': 0, 'AcceptedCmp5': 0, 'AcceptedCmp1': 0, 'AcceptedCmp2': 0, 'Response': 0}
    # Function to update discounts
    def update_discounts(season):
        for key in st.session_state.discounts.keys():
            st.session_state.discounts[key] = 1 if key == season else 0
    # User input: select a season from a selectbox
    selected_season = col12.selectbox("Choose a season to apply discount:", ('AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1', 'AcceptedCmp2', 'Response'))
    # Update the discounts based on the selection
    update_discounts(selected_season)

    season_3 = st.session_state.discounts['AcceptedCmp3']
    season_4 = st.session_state.discounts['AcceptedCmp4']
    season_5 = st.session_state.discounts['AcceptedCmp5']
    season_1 = st.session_state.discounts['AcceptedCmp1']
    season_2 = st.session_state.discounts['AcceptedCmp2']
    current_season = st.session_state.discounts['Response']

    # Amount Spending
    Amount_Spent = col10.text_input("Enter Amount Spending for All Purchases",max_chars=5,help="Please enter below 3000 ")

 #---------------------------------------------------------------------------------------------------------------
    Cluster = " "
     # Button for submission
    if st.button("Result"):
        Cluster = customer_prediction([Year_Birth,output,output_1,Income,Kids,Teen,No_Purchase,No_web_Purchase,
                                       No_Cat_Purchase,No_Store_Purchase,No_web_visits,season_3, season_4,season_5,season_1,season_2,current_season,Amount_Spent])
    st.success(Cluster)    

 #----------------------------------------------------------------------------------------------------------------
   
if __name__ == '__main__':
    main()




    