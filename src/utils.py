#!/usr/bin/env python3


#logging
import logging

#threading
from threading import Thread

# packages for confusion matrix plots
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

# numpy
import numpy as np

class Utils(object):
    global logger
    
    def __init__(self):
        self.logger = logging.getLogger('mohadelrezk-utils-class')
    
    
    
        hdlr = logging.FileHandler('utils.log')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        self.logger.addHandler(hdlr)
        self.logger.setLevel(logging.INFO)

       
        
    ##Plot function for Confusion Matrix
    #plt.rcParams['figure.figsize'] = (6.0, 6.0)
    def plot_confusion_matrix(self, cm, title='Confusion matrix', cmap=plt.cm.Blues):
    
        labels=['functional','functional needs repair','non functional']
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar(shrink=0.7)
        tick_marks = np.arange(len(labels))
        plt.xticks(tick_marks, labels, rotation=45, ha='right', fontsize=12)
        plt.yticks(tick_marks, labels , fontsize=12)
        plt.tight_layout()
        plt.ylabel('True label', fontsize=12)
        plt.xlabel('Predicted label', fontsize=12)

