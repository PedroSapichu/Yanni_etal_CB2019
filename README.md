# Tutorial to use script from Yanni et al. Curr. Biol. 2019.

## Getting Started

The [Python script](https://github.com/PedroSapichu/Yanni_etal_CB2019/blob/master/ScriptAssortment.py) provided here works with binary images. For this reason, it is useful for 2-strain competitions only. You can run, for instance, one of our [example images](https://github.com/PedroSapichu/Yanni_etal_CB2019/blob/master/AssortedFigure.png). After running the script on each image there will be 2 assortment calculations given, one for the black pixels and one for the white. Just keep in mind which strain represents each of these colors.

### Prerequisites

You need to have inslalled Python (version 3 is recommended). Within Python, you will need to have installed the following packages: skimage, numpy, and scipy. 

## Running the script

Make sure that the script is located in the same folder where you have your image. This will also be the folder where the results will be stored, in .CSV files. 

## After running the script

You will find 2 .CSV files for each image analyzed, corresponding to the assortment values of the strains analyzed in each image. Note that there is an assortment value for each of the radius determined in the script (max. default radius is 500 pixels, so if your images are much bigger you can increase this parameter). 

## Authors

* **David Yanni (Georgia Tech, School of Physics)** 
* **Pedro Márquez-Zacarías (Georgia Tech, School of Biological Sciences)**
* **Peter J. Yunker (Georgia Tech, School of Physics)**
* **William C. Ratcliff (Georgia Tech, School of Biological Sciences)**
