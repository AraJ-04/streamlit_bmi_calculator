import streamlit as st

st.title('Welcome to BMI Calculator')

weight = st.number_input("Enter Your Weight (in kgs): ")

status = st.radio("Select your height format: ",
                  ("cms","meters","feet"))

if(status == "cms"):
    
    height = st.number_input("Enter Your Height (in cms): ")

    try:
        bmi = weight / ((height/100)**2)
    
    except:
        st.text("Enter some value of height")

elif(status == "meters"):
    height = st.number_input("Enter Your Height (in meters): ")

    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value of height")

elif(status == "feet"):
    height = st.number_input("Enter Your Height (in feet): ")

    try:
        bmi = weight / (((height/3.28))**2)

    except:
        st.text("Enter some value of height")

if(st.button("Calculate Bmi")):

    st.text("Your BMI Index is {}.".format(bmi))

    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30):
        st.error("Extremely Overweight")

