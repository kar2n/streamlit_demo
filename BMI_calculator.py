# import module
import streamlit as st

# Title
st.title('BMI calculator')

# Input weight
weight = st.number_input("Enter your weight (in kgs)") 

# Input height
# radio button to choose format
status = st.radio('Select your height format: ',
                  ('cms', 'meters', 'feet'))

# compare status
if(status == 'cms'):
  height = st.number_input('Centimeters')

  try:
    bmi = weight / ((height/100)** 2)
  except:
    st.text("Enter some value of height")

elif(status == 'meters'):
  height = st.number_input('Meters')

  try:
    bmi = weight / (height ** 2)
  except:
    st.text("Enter some value of height") 

else:
  heigh = st.number_input('Feet')

# 1 meter = 3.28
  try:
    bmi = weight / (((height/3.28))** 2)
  except:
    st.text("Enter some value of height")

# check if the button is pressed or not
if(st.button('Calculate BMI')):

# print the BMI INDEX
st.text("Your BMI Index is {}.".format(bmi))
