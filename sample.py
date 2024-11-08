# import module
import streamlit as st

# Title
st.title("Hello GeeksForGeeks !!!")

# Header
st.header("This is a header") 

# Subheader
st.subheader("This is a subheader")

# Text
st.text("Hello GeeksForGeeks !!!")

# Markdown
st.markdown("### This is a markdown")

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
