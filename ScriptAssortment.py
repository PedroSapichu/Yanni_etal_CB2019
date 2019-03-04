# Note that the colors referred to here depends entirely on how the image is thresholded. 
# If red is black (0 pixel value), then red is assortment_1.  
# Red-blue names are only referring to the colors used in the paper,
# but it doesn't matter what colors the original images have,
# as long as there is a binarization. 

# Load packages needed
import skimage.io as io
import numpy as np
np.set_printoptions(threshold=np.nan)
from scipy import signal

# Load example image
image_title='AssortedFigure.png'

input1 = io.imread(image_title)
print(input1.shape[0])
print(input1.shape[1])

row_start=0
row_end=input1.shape[0]
column_start=0
column_end=input1.shape[1]

# Here define what is the maximum area that
# will be used for assortment calculations
areamax=500
assortment_1=[]
assortment_2=[]

# print input1
image=np.array(input1)
image2=np.empty((row_end,column_end))
for rownum in range(row_start,row_end):
    for colnum in range(column_start,column_end):
        if image[rownum,colnum]==255:
            image2[rownum,colnum]=-1
        else:
            image2[rownum,colnum]=1

# print image2
for x in range(3,areamax,2):
    a=np.ones((x,x),int)
    for i in range(0,len(a)):
        for k in range(0,a.shape[1]):
            if i/float((len(a)-1))==.5 and k/float((len(a)-1))==.5:
                a[i,k]=-np.sum(a)+1     
    convolved=signal.fftconvolve(image2,a)
    trimming_d=int((len(a)-1)/2)
    trimmed=convolved[trimming_d:-trimming_d, trimming_d:-trimming_d]
    blues=[]
    reds=[]        
    #print len(trimmed)
    for row in range(0,trimmed.shape[0]-1):
        for col in range(0,trimmed.shape[1]-1):
            if trimmed[row,col]>=1:
                reds.append(int(trimmed[row,col]))
            if trimmed[row,col]<=-1:
                blues.append(int(trimmed[row,col]))
            if int(trimmed[row,col])==0 and int(image2[row,col])==1:
                reds.append(0)
            if int(trimmed[row,col])==0 and int(image2[row,col])==-1:
                blues.append(0)                
    blues=np.absolute(blues)
    
# Calculate strain frequencies 
    blue_freq=float(len(blues))/(len(blues)+len(reds))
    red_freq = float(len(reds))/(len(blues)+len(reds))

# Calculate assortment
    red_assortment=(1-np.mean(reds)/(((len(a)**2)-1)*2) - red_freq) /(1-red_freq)
    blue_assortment=(1-np.mean(blues)/(((len(a)**2)-1)*2) - blue_freq) /(1-blue_freq)
    #print "mean blues", np.mean(blues)
    #print "mean reds", np.mean(reds)
    print("blue r", blue_assortment)
    print("red r", red_assortment)
    assortment_1.append(red_assortment)
    assortment_2.append(blue_assortment)
    
# Save data for analysis 
np.savetxt("assortment_str1_for_image_%s.csv" %(image_title), assortment_1, delimiter=",")
np.savetxt("assortment_str2_for_image_%s.csv" %(image_title), assortment_2, delimiter=",")
