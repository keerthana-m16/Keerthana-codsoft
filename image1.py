import tensorflow as tf
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Embedding, LSTM, Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from PIL import Image
import os

# Load pre-trained InceptionV3 model for feature extraction
def extract_features(image_path):
    base_model = InceptionV3(weights='imagenet')
    model = Model(base_model.input, base_model.layers[-2].output)

    # Preprocess the image
    img = Image.open(image_path).resize((299, 299))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    # Extract features
    features = model.predict(img)
    return features

# Prepare text data
def create_tokenizer(captions):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(captions)
    return tokenizer

def create_sequences(tokenizer, captions, max_length):
    sequences = []
    for caption in captions:
        seq = tokenizer.texts_to_sequences([caption])[0]
        for i in range(1, len(seq)):
            sequences.append(seq[:i+1])
    return pad_sequences(sequences, maxlen=max_length, padding='post')

# Define the model
def define_model(vocab_size, max_length):
    inputs1 = Input(shape=(2048,))
    fe1 = Dense(256, activation='relu')(inputs1)
    fe2 = Dropout(0.5)(fe1)

    inputs2 = Input(shape=(max_length,))
    se1 = Embedding(vocab_size, 256, mask_zero=True)(inputs2)
    se2 = LSTM(256)(se1)

    decoder1 = tf.keras.layers.add([fe2, se2])
    decoder2 = Dense(256, activation='relu')(decoder1)
    outputs = Dense(vocab_size, activation='softmax')(decoder2)

    model = Model(inputs=[inputs1, inputs2], outputs=outputs)
    model.compile(optimizer='adam', loss='categorical_crossentropy')
    return model

# Dummy dataset and tokenizer (replace with actual data)
captions = ["A cat sitting on a sofa.", "A dog playing in the park."]
tokenizer = create_tokenizer(captions)
vocab_size = len(tokenizer.word_index) + 1
max_length = max(len(caption.split()) for caption in captions)

# Extract features for a sample image
image_path = "sample_image.jpg"  # Replace with your image path
features = extract_features(image_path)

# Example usage
print("Image features extracted:", features.shape)

# Define the model
model = define_model(vocab_size, max_length)
model.summary()

# Note: This script sets up the basic structure for an image captioning model.
# To train it effectively, use a large dataset like MS COCO or Flickr8k with preprocessed features.
