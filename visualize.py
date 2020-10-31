import warnings
warnings.filterwarnings("ignore")

import matplotlib
matplotlib.use('agg')

import matplotlib.pyplot as plt
import pylab as pl
import numpy as np

def plotIt(clf, X_test, y_test):
    x_min=0.0
    x_max=1.0
    y_min=0.0
    y_max=1.0
    
    h = 0.01
    x, y = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[x.ravel(), y.ravel()])
    
    Z = Z.reshape(x.shape)
    
    plt.xlim(x.min(), x.max())
    plt.ylim(y.min(), y.max())
    
    plt.pcolormesh(x, y, Z, cmap=pl.cm.seismic)
    
    grade_sig = [X_test[i][0] for i in range(0, len(X_test)) if y_test[i]==0]
    bumpy_sig = [X_test[i][1] for i in range(0, len(X_test)) if y_test[i]==0]
    grade_bkg = [X_test[i][0] for i in range(0, len(X_test)) if y_test[i]==1]
    bumpy_bkg = [X_test[i][1] for i in range(0, len(X_test)) if y_test[i]==1]
    
    plt.scatter(grade_sig, bumpy_sig, color="b", label="fast")
    plt.scatter(grade_bkg, bumpy_bkg, color="r", label="slow")
    plt.legend()
    plt.xlabel("bumpiness")
    plt.ylabel("grade")
    
    plt.savefig("test.png")
    
    plt.show()
    
import base64
import json
import subprocess
#from PIL import Image

def output_image():
    Image.open("test.png").show
#f = Image.open("file.png").show()

def output_image1(name, format, bytes):
    image_start = "BEGIN_IMAGE_f9825uweof8jw9fj4r8"
    image_end = "END_IMAGE_0238jfw08fjsiufhw8frs"
    data={}
    data['name'] = name
    data['format'] = format
    data['bytes'] = base64.encodestring(bytes)
    print (image_start+json.dumps(data)+image_end)