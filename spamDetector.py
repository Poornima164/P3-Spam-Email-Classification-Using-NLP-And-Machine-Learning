import streamlit as st
import pickle

model = pickle.load(open('spam.pkl', 'rb'))
cv = pickle.load(open('vec.pkl', 'rb'))

# Sidebar for additional info
with st.sidebar:
    st.header("About the Project")
    st.write(
        """
        - 📧 **Purpose:** Spot and block unwanted spam emails effortlessly.
        - 🛠️ **Technology Stack:** NLP + Machine Learning (Multinomial Naive Bayes)
        - 🔍 **Email Analysis Method:** CountVectorizer (Bag of Words)
        - 🌟 **Performance:** Delivers ~98% accuracy on test data.
        """
    )

def main():
    st.title("🚀  IntelligentSpam Email Detection System")
    st.write(
        """
        Welcome to the **Spam Email Detector**, your go-to tool for ensuring a clean and spam-free inbox.  
        With the power of **AI and Machine Learning**, this system quickly identifies whether an email is legitimate or spam.
        """
    )
    st.subheader("🔍 Email Classification")
    
    user_input = st.text_area(
        "📩 Paste the email content below to check its authenticity:", 
        height=150
    )
    
    if st.button("🚦 Analyze Email"):
        if user_input:
            data = [user_input]
            vec = cv.transform(data).toarray()
            result = model.predict(vec)
            if result[0] == 0:
                st.success("🟢 This email is clean and **Not Spam**! 🎉")
            else:
                st.error("🔴 Alert! This email is classified as **Spam**! 🚨")
        else:
            st.warning("⚠️ Please paste the email content to proceed with the classification.")

main()
