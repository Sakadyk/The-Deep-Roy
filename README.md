# The Deep Roy: Deepfake Detection using EfficientNetV2B0

Ran locally using [Anaconda Navigator](https://www.anaconda.com/download).

Setup:

```
conda create -n envname anaconda
```

```
conda activate envname
```

```
pip install tensorflow opencv-python numpy matplotlib streamlit
```

## Datasets

- deepfake and real images (Kaggle): [Link](https://www.kaggle.com/datasets/manjilkarki/deepfake-and-real-images)
- Deepfake Dataset (Kaggle): [Link](https://www.kaggle.com/datasets/aryansingh16/deepfake-dataset)

## Notebooks

- Train: [Link](https://github.com/Sakadyk/The-Deep-Roy/blob/main/EffNetV2B0_92/pi24_train.ipynb)
- Test: [Link](https://github.com/Sakadyk/The-Deep-Roy/blob/main/EffNetV2B0_92/pi24_test.ipynb)

## Models

- Hierarchical Data Format 5 (.h5): [Link](https://drive.google.com/file/d/1JKGaSYyAQDGdXMF1CAy4vULD3uYukazd/view?usp=sharing)
- Keras (.keras): [Link](https://drive.google.com/file/d/1D9zZ370Glb3OCk1YW8riYa_0vz6j9b9t/view?usp=sharing)
- TensorFlow SavedModel: [Link](https://drive.google.com/drive/folders/1HniYiwvXiYI3l-gqzxX61YXeDZNEWYWw?usp=sharing)

## Training Result

![alt text](https://github.com/Sakadyk/The-Deep-Roy/blob/main/Images/graph.png "Traning Result Graph")

## Testing Result

Test Accuracy: 92.24%
![alt text](https://github.com/Sakadyk/The-Deep-Roy/blob/main/Images/test_result.png "Testing Visualization")

## Streamlit

`TBD`
