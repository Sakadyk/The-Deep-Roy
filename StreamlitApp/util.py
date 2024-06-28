import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import cv2
import os
import tempfile

# Load your trained model (make sure the path is correct)
model = tf.keras.models.load_model('./StreamlitApp/model/model_pi_roy.h5')

def classify_image(file):
    img = Image.open(file)
    img = img.convert('RGB')  # Ensure image is in RGB mode
    img = img.resize((200, 200))  # Resize to match the input size expected by the model
    img_array = image.img_to_array(img)  # Convert image to array
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = img_array / 255.0  # Rescale the image

    print("Image array shape:", img_array.shape)  # Debugging statement
    print("Image array data type:", img_array.dtype)  # Debugging statement

    # Make prediction
    prediction = model.predict(img_array)
    confidence_real = prediction[0][0]
    confidence_fake = 1 - confidence_real
    
    # Determine the label based on the prediction
    label = 'fake' if confidence_real < 0.5 else 'real'
    
    return {'label': label, 'confidence_real': confidence_real, 'confidence_fake': confidence_fake}

def classify_video(file):
    # Save the uploaded video file to a temporary location
    temp_file_path = os.path.join(tempfile.gettempdir(), "temp_video.mp4")
    with open(temp_file_path, "wb") as f:
        f.write(file.read())

    video_capture = cv2.VideoCapture(temp_file_path)

    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_step = total_frames // 20  # Divide video into 20 frames

    predictions = []

    for i in range(0, total_frames, frame_step):
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = video_capture.read()
        if not ret:
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)
        frame = frame.resize((200, 200))  # Resize to match the input size expected by the model
        img_array = image.img_to_array(frame)  # Convert image to array
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        img_array = img_array / 255.0  # Rescale the image

        # Make prediction
        prediction = model.predict(img_array)
        predictions.append(prediction[0][0])

    video_capture.release()
    # cv2.destroyAllWindows()

    avg_prediction_real = np.mean(predictions)
    avg_prediction_fake = 1 - avg_prediction_real

    # Determine the label based on the average prediction
    label = 'fake' if avg_prediction_real < 0.5 else 'real'

    # Delete the temporary file
    os.remove(temp_file_path)

    return {'label': label, 'confidence_real': avg_prediction_real, 'confidence_fake': avg_prediction_fake}
