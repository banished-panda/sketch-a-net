import os
import requests
import numpy as np
import idx2numpy
import zlib

print('Data: Downloading...  ', end='\r')
# URLs for the MNIST dataset (in IDX format)
urls = {
    "train-images-idx3-ubyte.gz": "http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz",
    "train-labels-idx1-ubyte.gz": "http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz",
    "t10k-images-idx3-ubyte.gz": "http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz",
    "t10k-labels-idx1-ubyte.gz": "http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz"
}

# Download the files
for filename, url in urls.items():
    response = requests.get(url)
    decompressed_data = zlib.decompress(response.content, zlib.MAX_WBITS|32)
    with open(filename[:-3], 'wb') as f:  # remove '.gz' from filename
        f.write(decompressed_data)

print('Data: Converting...    ', end='\r')
# Convert the IDX files to numpy arrays
train_images = idx2numpy.convert_from_file('train-images-idx3-ubyte')
train_labels = idx2numpy.convert_from_file('train-labels-idx1-ubyte')
test_images = idx2numpy.convert_from_file('t10k-images-idx3-ubyte')
test_labels = idx2numpy.convert_from_file('t10k-labels-idx1-ubyte')

# Flatten the image arrays and add the labels as the first column
train_data = np.column_stack((train_labels, train_images.reshape(train_images.shape[0], -1)))
test_data = np.column_stack((test_labels, test_images.reshape(test_images.shape[0], -1)))

print('Data: Saving...         ', end='\r')
# Create 'data' directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Write the numpy arrays to CSV files in 'data' directory
np.savetxt('data/train.csv', train_data, fmt='%i', delimiter=',')
np.savetxt('data/test.csv', test_data, fmt='%i', delimiter=',')

print('Data: Cleaning up...       ', end='\r')
# Remove the intermediate IDX files
os.remove('train-images-idx3-ubyte')
os.remove('train-labels-idx1-ubyte')
os.remove('t10k-images-idx3-ubyte')
os.remove('t10k-labels-idx1-ubyte')

print('Data: downloaded! :)       ', end='\n')
