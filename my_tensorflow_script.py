import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  # Disable oneDNN custom operations

import tensorflow as tf

# Your TensorFlow code starts here
print("TensorFlow version:", tf.__version__)
