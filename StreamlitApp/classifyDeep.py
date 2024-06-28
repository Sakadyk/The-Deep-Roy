import streamlit as st
import util

def classify_image(file):
    res = util.classify_image(file)
    return res

def classify_video(file):
    res = util.classify_video(file)
    return res

def app():
    st.title("Upload an image or video to see if it is a deepfake or a real.")
    st.sidebar.title("Choose Mode")
    mode = st.sidebar.selectbox("Choose whether you want to classify images or videos:", ("Image", "Video"))

    if mode == "Image":
        st.image('./StreamlitApp/assets/ImageBanner.gif', use_column_width=True)
        st.write("*Video: [Lil beast](https://youtu.be/Ky0nwzlZrMk)*")
        st.write("*Logo made using [BlueArchive-Style Logo Generator](https://tmp.nulla.top/ba-logo/)*")
        st.subheader("Upload an image to see if it is a fake or real face:")
        file_uploaded = st.file_uploader("Select Image File", type=["jpg", "png", "jpeg"])
        if file_uploaded is not None:
            res = classify_image(file_uploaded)

            c1, buff, c2 = st.columns([2, 0.5, 2])

            c1.subheader("Uploaded Image")
            c1.image(file_uploaded, use_column_width=True)
            c2.subheader("Classification Result")
            c2.write("This image is classified as **{}**.".format(res['label'].title()))
            c2.write("Confidence Real: {:.2f}".format(res['confidence_real']))
            c2.write("Confidence Fake: {:.2f}".format(res['confidence_fake']))
    
    elif mode == "Video":
        st.image('./StreamlitApp/assets/VideoBanner.gif', use_column_width=True)
        st.write("*Video: [Lil beast](https://youtu.be/Ky0nwzlZrMk)*")
        st.write("*Logo made using [BlueArchive-Style Logo Generator](https://tmp.nulla.top/ba-logo/)*")
        st.subheader("Upload a video to see if it is a fake or real face:")
        file_uploaded = st.file_uploader("Select Video File", type=["mp4"])
        if file_uploaded is not None:
            res = classify_video(file_uploaded)
            
            c1, buff, c2 = st.columns([2, 0.2, 3])  # Membagi tata letak menjadi tiga kolom

            c1.subheader("Uploaded Video")
            c1.video(file_uploaded)
            c2.subheader("Classification Result")
            c2.write("This video is classified as **{}**.".format(res['label'].title()))
            c2.write("Confidence Real: {:.2f}".format(res['confidence_real']))
            c2.write("Confidence Fake: {:.2f}".format(res['confidence_fake']))
