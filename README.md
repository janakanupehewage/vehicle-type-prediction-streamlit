# Vehicle Type Prediction Web App

This is a Streamlit web application that allows users to upload images of vehicles and predicts their type (bus, car, motorcycle, or truck) using a trained model.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)

## Overview
This application allows users to upload images of vehicles and predicts their type using a trained Convolutional Neural Network (CNN). The model can identify four different types of vehicles: bus, car, motorcycle, and truck. It features an intuitive interface, real-time progress updates, and a visual representation of prediction probabilities.

## Features
- **Image Upload**: Users can upload images in JPG, JPEG, or PNG formats (up to 200MB).
- **Vehicle Type Prediction**: The app predicts vehicle type using a pre-trained model.
- **Progress Bar**: A progress bar gives real-time feedback during prediction.
- **Sidebar Navigation**: The sidebar provides easy navigation between two options:
  - **Prediction**: Upload an image and get vehicle type predictions.
  - **About the App**: Learn more about the app and its functionality.
- **Visualization**: The app displays a graph showing the probabilities for each vehicle type.

## Installation

### Prerequisites
Ensure that you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)

### Instructions
1. **Clone this repository**:
    ```bash
    git clone https://github.com/janakanupehewage/vehicle-type-prediction-streamlit.git
    cd vehicle-type-prediction-app
    ```

2. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit application**:
    ```bash
    streamlit run app.py
    ```

## Usage

### Prediction
1. Select the "Prediction" option from the sidebar.
2. Upload an image of a vehicle.
3. Click the "Predict" button to get the predicted vehicle type and see the probability graph.

### About the App
1. Select the "About the App" option from the sidebar to read about the app's features and functionality.

