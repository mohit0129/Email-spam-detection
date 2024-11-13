import streamlit as st
import pickle

model = pickle.load(open('spam.pkl','rb'))
cv = pickle.load(open('vectorizer.pkl','rb'))

st.title("Email spam Classification Application")
st.write("This is the spam detection system")
# st.text_area("Enter an email to classify:")
user_input = st.text_area("Enter an email to classify",height=50)
if st.button("Classify"):
    if user_input:
        data = [user_input]
        vect = cv.transform(data).toarray()
        pred = model.predict(vect)
        if pred[0] == 0:
            st.success("This email is not spam")
        else:
            st.error("This is a spam email")
    else:
        print("Please type email")
        