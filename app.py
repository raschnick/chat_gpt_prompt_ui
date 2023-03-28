import streamlit as st

from request_service import generate_response


def main():
    st.set_page_config(page_title='Chat GPT UI')
    st.header('My Own GPT prompt Interface')

    input_text = st.text_input('Please enter your question:')

    if input_text:
        output_text = generate_response(input_text)
        st.write(output_text)


if __name__ == "__main__":
    main()
