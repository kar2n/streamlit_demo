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




# success
st.success("Success")

# success
st.info("Information")

# success
st.warning("Warning")

# success
st.error("Error")

# Exception - This has been added later
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

# Write text
st.write("Text with write")

# Writing python inbuilt function range()
st.write(range(10))

# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
if st.checkbox("Show/Hide"):

    # display the text if the checkbox returns True value
    st.text("Showing the widget")

# radio button
# first argument is the title of the radio button
# second argument is the options for the radio button
status = st.radio("Select Gender: ", ('Male', 'Female'))

# conditional statement to print 
# Male if male is selected else print female
# show the result using the success function
if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")


# Selection box

# first argument takes the titleof the selectionbox
# second argument takes options
hobby = st.selectbox("Hobbies: ",
                     ['Dancing', 'Reading', 'Sports'])

# print the selected hobby
st.write("Your hobby is: ", hobby)


# Create a simple button that does nothing
st.button("Click me for no reason")

# Create a button, that when clicked, shows a text
if(st.button("About")):
    st.text("Welcome To GeeksForGeeks!!!")

# Text Input

# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input("Enter Your name", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
    result = name.title()
    st.success(result)
