import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model and vectorizer
model = pickle.load(open('spam.pkl', 'rb'))
cv = pickle.load(open('vectorizer.pkl', 'rb'))

def classify_email(email_text):
    """Classifies an email as Spam or Not Spam."""
    if email_text:
        data = [email_text]
        vec = cv.transform(data).toarray()
        result = model.predict(vec)
        return result[0]
    else:
        return None

# Main function for Streamlit app
def main():
    st.title("Spam Email Detection System")
    st.write(
        """
        Welcome to the **Spam Email Detection System**, an easy-to-use tool that identifies whether an email is **Spam** or **Not Spam**.  
        Using advanced Natural Language Processing (NLP) and Machine Learning, our system helps you keep your inbox clean and free from unwanted messages.
        """
    )
    
    # Sidebar for additional info
    with st.sidebar:
        st.header("Project Overview")
        st.write(
            """
            - **Objective:** Automatically detect and classify spam emails.
            - **Technology:** NLP, Machine Learning (Multinomial Naive Bayes)
            - **Vectorization Method:** CountVectorizer (Bag of Words)
            - **Accuracy:** ~98% on the test dataset
            """
        )
    
    st.subheader("Classify Your Email")

    # User input area
    user_input = st.text_area("Paste your email content here:", height=250)
    
    # Classification button
    if st.button("Check for Spam"):
        if user_input.strip():
            classification = classify_email(user_input.strip())
            if classification == 0:
                st.success("✅ This email is **Not Spam**.")
            else:
                st.error("🚫 This email is **Spam**.")
        else:
            st.warning("⚠️ Please paste an email to classify.")

# Run the app
if __name__ == '__main__':
    main()
