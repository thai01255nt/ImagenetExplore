import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cv2

def plot_multi_images(images):
    '''
    :param images: [batch,h,w,BGR]
    :return: Plot images
    '''

    num_images = len(images)
    rows = int(np.sqrt(num_images))
    cols = rows
    fig = plt.figure(figsize=(16,16))
    if rows**2 < num_images:
        rows = rows + 1
    for i in range(len(images)):
        fig.add_subplot(rows, cols, i+1)
        plt.imshow(cv2.cvtColor(images[i],cv2.COLOR_BGR2RGB))
    plt.show()