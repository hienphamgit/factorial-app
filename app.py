import streamlit as st
from factorial import fact

def main():
    st.title("Factorial Calculator")
    st.write("This app calculates the factorial of a given number.")    
    
    number = st.number_input("Enter a number:", min_value=0, max_value=999, value=0, step=1)
    
    if st.button("Calculate Factorial"):
        result = fact(number)
        st.write(f"The factorial of {number} is {result}")
if __name__ == "__main__":
    main()