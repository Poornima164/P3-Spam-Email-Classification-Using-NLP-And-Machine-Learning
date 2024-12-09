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
    st.title("Spam Email Classification using NLP and Machine Learning")
    st.write(
        """
        Welcome to **Spam Email Classification**, a user-friendly tool designed to classify emails as **Spam** or **Not Spam**.
        This application uses a Machine Learning model trained on a labeled email dataset.
        """
    )
    
    # Sidebar for additional info
    with st.sidebar:
        st.header("About")
        st.write(
            """
            - **Project:** Spam Email Classification using NLP and Machine Learning
            - **Model:** Multinomial Naive Bayes  
            - **Vectorization:** Bag of Words (CountVectorizer)  
            - **Accuracy:** ~98%
            """
        )
    
    st.subheader("Enter the Email for Classification")
    
    # User input area
    user_input = st.text_area("Paste the email content below:", height=200)
    
    # Classification button
    if st.button("Classify Email"):
        if user_input.strip():
            classification = classify_email(user_input.strip())
            if classification == 0:
                st.success("🟢 This is Not a Spam Email!")
            else:
                st.error("🔴 This is a Spam Email!")
        else:
            st.warning("⚠️ Please enter email content to classify.")

# Run the app
if __name__ == '__main__':
    main()
