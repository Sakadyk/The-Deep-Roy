import streamlit as st

def app():
    st.image('./StreamlitApp/assets/TheDeepRoy.png', use_column_width=True)
    st.write("*Logo made using [BlueArchive-Style Logo Generator](https://tmp.nulla.top/ba-logo/)*")
    
    st.subheader("💡 Abstract")
    st.write('''
             Deepfake, a technology that utilizes machine learning to manipulate videos and images, has become a significant challenge in recent years. This research focuses on the development of a machine learning model to detect deepfakes in images and short videos. The model is developed using transfer learning methods with the pre-trained EfficientNetV2B0 model. The entire model development process is carried out locally using the Anaconda Virtual Environment, and the results are implemented in a web application using Streamlit. 
             
             The aim of this research is to produce a model that can accurately detect deepfakes, contribute to the field of machine learning, and be implemented in real-world applications to assist the public in identifying deepfakes.
             ''')

    st.subheader("🤖 What is \"The Deep Roy\"?")
    st.markdown('''
                “The Deep Roy” is a tool that harnesses the capabilities of deep learning to differentiate between authentic and manipulated images or videos. For example, if an individual takes your genuine image and superimposes your face onto a crime scene or morphs it onto another person’s body, “The Deep Roy” will label it as counterfeit, thereby minimizing the likelihood of it being misused to tarnish your reputation. Just upload the image (or video), and the machine learning model will assess it and deliver a verdict in a split second.
                ''')

    st.subheader("💾 Datasets")
    st.markdown('''The datasets was taken from Kaggle: 
    <li> [deepfake and real images](https://www.kaggle.com/datasets/manjilkarki/deepfake-and-real-images) </li>
    <li> [Deepfake Dataset](https://www.kaggle.com/datasets/aryansingh16/deepfake-dataset) </li>
                ''', unsafe_allow_html=True)
    st.image('./StreamlitApp/assets/faces.png', use_column_width=True)

    st.subheader("🏗️ Model Architecture")
    st.image('./StreamlitApp/assets/model.png', use_column_width=True)
    st.write(f'''
             The base model used for deepfake detection is EfficientNetV2B0, a pre-trained model using the ImageNet dataset. The following steps are taken to prepare the base model and adapt it for binary classification tasks (real vs. fake):
             - Uses weights that have been trained on the ImageNet dataset.
             - Removes the last classification layer to allow the addition of a custom classification layer.
             - Sets the input image size to 200x200 pixels with 3 color channels (RGB).
             - Uses Global Max Pooling on the output from the base model.
             - Includes the preprocessing required by EfficientNetV2B0.
             - Make the base model trainable.
             ''')

    st.subheader("📈 Results")
    st.image('./StreamlitApp/assets/accloss.png', use_column_width=True)
    st.markdown(f'''
                - The “Training and Validation Accuracy” graph shows an increase in accuracy for both training and validation data with more epochs, indicating effective learning and performance improvement over time.
                - The “Training and Validation Loss” graph demonstrates a decrease in loss for both training and validation data with more epochs, suggesting fewer errors over time and effective learning.
                - Despite slight differences in training and validation accuracy and loss, indicating potential overfitting, the small magnitude of these differences suggests that the model has minimal overfitting.
                ''')
    st.write("Confusion Matrix:")
    st.image('./StreamlitApp/assets/conmat.png', use_column_width=True)
    st.write("Classification Report:")
    st.code('''
            Report Title  precision    recall  f1-score   support

                    Fake       0.89      0.96      0.93     15492
                    Real       0.96      0.88      0.92     15413

                accuracy                           0.92     30905
               macro avg       0.93      0.92      0.92     30905
            weighted avg       0.93      0.92      0.92     30905
            ''')

    st.write(" ")

    st.write("*Try it out by clicking on \"The Deep Fake\" button on the Sidebar*")
