import pandas as pd
import numpy as np
import os
import im_tools


N = 1024
FS = 20000
input_dir = "F20K-C"

csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

counter = 1
for file_name in csv_files:
    
    data = pd.read_csv(os.path.join(input_dir, file_name))
    freq = 100*counter

    current_fft = np.fft.fft(data['Current'])
    index_highest_current_fft = np.argmax(np.abs(current_fft))
    if(index_highest_current_fft > 512):
        index_highest_current_fft = 1024 - index_highest_current_fft

    index = int((N*freq)/FS)

    print(f'{freq}:\t{index}\t{index_highest_current_fft}\t{index_highest_current_fft-index}')
    counter = counter + 1
    if counter == 11:
        break