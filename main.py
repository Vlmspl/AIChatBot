import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from utils import character_map, text_to_numerical

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Check if GPU is available
if tf.config.list_physical_devices('GPU'):
    print("GPU is available.")
else:
    print("GPU is not available. Running on CPU.")

print("CUDA:" + str(tf.test.is_built_with_cuda()))
print("Physical Devices:", tf.config.list_physical_devices())

# Load data
def load_data(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        inputs = f.read().splitlines()
    with open(output_file, 'r', encoding='utf-8') as f:
        outputs = f.read().splitlines()
    return inputs, outputs

# Convert data to sequences
def convert_data(inputs, outputs):
    input_sequences = [text_to_numerical(text) for text in inputs]
    output_sequences = [text_to_numerical(text) for text in outputs]
    return input_sequences, output_sequences

# Load and prepare data
input_file = 'database/input.txt'
output_file = 'database/output.txt'
inputs, outputs = load_data(input_file, output_file)
input_sequences, output_sequences = convert_data(inputs, outputs)

# Pad sequences to ensure uniform length
max_length = max(max(len(seq) for seq in input_sequences), max(len(seq) for seq in output_sequences))

# Ensure no negative values in sequences
input_sequences = pad_sequences(input_sequences, maxlen=max_length, padding='post', value=0)
output_sequences = pad_sequences(output_sequences, maxlen=max_length, padding='post', value=0)

# Convert outputs to one-hot encoding
num_classes = len(character_map)
output_sequences_one_hot = tf.keras.utils.to_categorical(output_sequences, num_classes=num_classes)

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=num_classes, output_dim=64, input_length=max_length),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(max_length * num_classes, activation='relu'),
    tf.keras.layers.Reshape((max_length, num_classes))
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(input_sequences, output_sequences_one_hot, epochs=100, batch_size=32)

# Save the model
model.save('chatbot_model.keras')

# Function to predict a response
def predict_response(model, input_text):
    input_sequence = text_to_numerical(input_text)
    input_sequence_padded = pad_sequences([input_sequence], maxlen=max_length, padding='post', value=0)
    prediction = model.predict(input_sequence_padded)
    response_sequence = np.argmax(prediction, axis=-1)[0]
    # Convert back to text
    inv_character_map = {v: k for k, v in character_map.items()}
    response = ''.join(inv_character_map.get(idx, '') for idx in response_sequence if idx in inv_character_map)
    return response.strip()

# Test the chatbot
test_input = "Hello"
response = predict_response(model, test_input)
print(f"Input: {test_input}\nResponse: {response}")
