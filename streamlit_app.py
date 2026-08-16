import streamlit as st

st.title("🧮 Simple Calculator")

operator = st.selectbox(
    "Choose an operation:",
    ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)" ]
)

if operator == "Addition (+)":
    values = st.text_input(
        "Enter values separated by comma:",
        placeholder="10,20,30,40"
    )

    if st.button("Calculate"):
        try:
            new_list = [float(val.strip()) for val in values.split(",")]
            result = sum(new_list)
            st.success(f"Sum of all given values = {result}")
        except ValueError:
            st.error("Please enter valid numbers separated by commas.")


elif operator == "Subtraction (-)":
    num1 = st.number_input("Enter first value:", value=0.0)
    num2 = st.number_input("Enter second value:", value=0.0)

    if st.button("Calculate"):
        st.success(f"{num1} - {num2} = {num1 - num2}")
        st.success(f"{num2} - {num1} = {num2 - num1}")


elif operator == "Multiplication (*)":
    values = st.text_input(
        "Enter values separated by comma:",
        placeholder="2,3,4"
    )

    if st.button("Calculate"):
        try:
            new_list = [float(val.strip()) for val in values.split(",")]

            result = 1
            for val in new_list:
                result = result * val

            st.success(f"Multiplication of all values = {result}")

        except ValueError:
            st.error("Please enter valid numbers separated by commas.")


elif operator == "Division (/)":
    num1 = st.number_input("Enter first value:", value=0.0)
    num2 = st.number_input("Enter second value:", value=0.0)

    if st.button("Calculate"):
        if num2 != 0:
            st.success(f"{num1} / {num2} = {num1 / num2}")
        else:
            st.error("You cannot divide by zero.")

st.write("---")
st.write("Thank you! 😊")
