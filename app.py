import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import matplotlib.pyplot as plt
import time

# Load the trained model
model = load_model('vehicle_type_identifier_model.keras')


vehicle_types_names = ['bus', 'car', 'motorcycle', 'truck']

# Preprocess the image
def preprocess_image(image):
    img = image.resize((150, 150))
    img = img.convert('RGB')
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

# Sidebar menu
st.sidebar.title("Menu")
option = st.sidebar.selectbox("Choose an option", ["Prediction", "About the App"])
st.sidebar.image("App_UI_Images/sidebar_vehicles_image.jpg", caption="Upload an image of a vehicle and get predictions for its type (bus, car, motorcycle, or truck)", use_column_width=True)

if option == "Prediction":
    st.title("Vehicle Type Prediction Web App")
    
    st.write("### Upload an image of a vehicle")
    st.write("Drag and drop a file here or use the file uploader below.")
    
    
    uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        
        image = load_img(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
        
        if st.button('Predict'):
            
            #st.write("Processing image...")
            with st.spinner("Processing..."):
                time.sleep(2)

            progress_bar = st.progress(0)
               
            progress_bar.progress(30)
            preprocessed_image = preprocess_image(image)

            time.sleep(2)
            progress_bar.progress(60)

            # Make a prediction
            prediction = model.predict(preprocessed_image)
            predicted_class = np.argmax(prediction, axis=1)[0]
            predicted_label = vehicle_types_names[predicted_class]
            
            # Show the prediction result
            st.success(f"Predicted Vehicle Type: {predicted_label}")
            
            progress_bar.progress(100)

            # Plotting a bar chart of prediction probabilities
            st.write("Prediction Probabilities (Graph):")
            fig, ax = plt.subplots()
            ax.barh(vehicle_types_names, prediction[0])
            plt.xlim(0, 1)
            st.pyplot(fig)

elif option == "About the App":
    st.title("About the App")
    st.write("### Vehicle Type Prediction Web App")
    st.image("App_UI_Images/about_app_image2.jpg")
    st.write("This Streamlit app allows users to upload an image of a vehicle and get predictions for its type (bus, car, motorcycle, or truck) using a trained model.")
    st.write("#### Features")
    st.write("- Upload and display an image of a vehicle.")
    st.write("- Predict vehicle type using a trained model.")
    st.write("- Display prediction probabilities in graphical formats.")
