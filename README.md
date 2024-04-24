# DETECTING RICE LEAF DISEASES 
## INTRODUCTION:

Rice is by far the most significant food crop for people in low- and lower-middle-income nations, out of the three primary crops (rice, wheat, and maize). Although both rich and poor people eat rice in low-income nations, the poorest people consume comparatively little wheat and are thus heavily influenced by rice prices and availability.

Rice is a vital and often irreplaceable staple in many Asian countries, particularly among the impoverished. Rice accounts for about half of the food expenditures and a fifth of total family expenditures for Asia's extreme poor, who subsist on less than 1.25 per-day_on_average. This group alone spends 62 billion (in purchasing power parity) on rice each year. Rice is vital to the food security of many of the world's impoverished.

## THE PROJECT HAS BEEN ORGANISED INTO MULTIPLE STAGES:

1.INTRODUCTION

2.ABOUT THE DATASET

3.IMPORT NEEDED LIBRARIES

4.PREPARING THE DATASET

5.CREATING THE VALIDATION SETS

6.CREATING THE TRAINNG SET FOR EACH CLASS

7.CREATING THE DATAFRAME FOR "DATA","TRAIN" & "VALIDATION" , BY RESTTING THE INDEX ACCORDINGLY

8.CHECKING THE VALUE_COUNTS

9.PREPROCESSING THE DATASET

10.VISUALISATION

11.SETTING UP & TEST THE AUGUMENTATIONS

* DEFINING THE TRANSFORM PARAMETER
* GETTING AN IMAGE TO TEST TRANSFORMATIONS
* TEST THE TRANSFORMATION
  
12.BUILDING THE DATA GENERATORS
  
* TRAIN GENERATOR
* BUILDING THE FUNCTION
* VAL GENERATOR
* TEST GENERATOR
  
13.MODEL BUILDING ARCHITECTURE
  
14.TRAIN THE MODEL
* EVALUATE THE MODEL ON THE VAL SET
* LOADING THE TRAIN MODEL
  
15.PLOTTING THE CURVES
  
16.MAKE A PREDICTION ON THE VAL SET

17.CONFUSION MATRIX & CLASSIFICATION REPORT

18.TESTING OUR MODEL WITH RANDOM PICTURE DOWNLOADED FROM GOOGLE

19.CONCLUSION:



### Rice Leaf Disease:
![image](https://github.com/Tanwar-12/DETECTING-RICE-LEAF-DISEASES/assets/110081008/a3d4216e-f5ee-4399-a40c-248c25ecdc72)

- This dataset contains 120 jpg images of disease infected rice leaves. The images are grouped into 3 classes based on the type of disease. There are 40 images in each class.

 - [X] Classes<br>
    - [x] Leaf smut
    - [x] Brown spot
    - [x] Bacterial leaf blight

## IMPORT NEEDED LIBRARIES
* NUMPY
* PANDAS
* SKLEARN
* TENSORFLOW
* MATPLOTLIB
* CV2
  
 ### PREPARING THE DATASET
* Creating The Dataframe Containing all the Images
* Creating The 3 List Of Classes
  
#### CREATING THE VALIDATION SETS 

##### CREATING THE TRAINNG SET FOR EACH CLASS

#### CREATING THE DATAFRAME FOR "DATA","TRAIN" & "VALIDATION" , BY RESTTING THE INDEX ACCORDINGLY

##### CHECKING THE VALUE_COUNTS

## PREPROCESSING THE DATASET
**Transform the target Here we will do one hot encoding to the target classes.**

#### BASIC CHECKS

 ###   Saving the dataframes as compressed csv files 
 <b>Note</b><br>
    → These csv files will allow us to use Pandas chunking to feed images into the generators.. <br>  
</div>

## VISUALISATION
* Displaying The Images of some Class
  ![image](https://github.com/Tanwar-12/DETECTING-RICE-LEAF-DISEASES/assets/110081008/ca5b13cd-59f5-4472-9a34-7551ace24a06)

## SETTING UP & TEST THE AUGUMENTATIONS

#### DEFINING THE TRANSFORM PARAMETER

### GETTING AN IMAGE TO TEST TRANSFORMATIONS
![image](https://github.com/Tanwar-12/DETECTING-RICE-LEAF-DISEASES/assets/110081008/a2cff4d7-58ee-47d8-b005-a059ffef8508)

#### TEST THE TRANSFORMATION
![image](https://github.com/Tanwar-12/DETECTING-RICE-LEAF-DISEASES/assets/110081008/99478b07-89ca-4d46-8554-241dbdbdc00a)

## BUILDING THE DATA GENERATORS
### TRAIN GENERATOR
#### BUILDING THE FUNCTION
* Train images have been augmented.
  ![image](https://github.com/Tanwar-12/DETECTING-RICE-LEAF-DISEASES/assets/110081008/053de21d-b998-4ff7-96c0-442d8bead8cf)

  ### VAL GENERATOR
  ![image](https://github.com/Tanwar-12/DETECTING-RICE-LEAF-DISEASES/assets/110081008/3e911572-090f-4bc9-8446-f55f4db3e8c6)

  ### TEST GENERATOR
  ![image](https://github.com/Tanwar-12/DETECTING-RICE-LEAF-DISEASES/assets/110081008/9f917151-ae5a-45d3-9db6-438e773ce2d9)
  ## MODEL BUILDING ARCHITECTURE
  ![image](https://github.com/Tanwar-12/DETECTING-RICE-LEAF-DISEASES/assets/110081008/746f160b-8d0e-4a1c-bcbd-a081fbcc3988)
  ## TRAIN THE MODEL
  ### EVALUATE THE MODEL ON THE VAL SET
  ## LOADING THE TRAIN MODEL
val_loss: 1.0603946447372437

val_acc: 0.9333333373069763

### PLOTTING THE CURVES

![image](https://github.com/Tanwar-12/DETECTING-RICE-LEAF-DISEASES/assets/110081008/24f34489-b6a6-4fc6-866c-058285882283)

![image](https://github.com/Tanwar-12/DETECTING-RICE-LEAF-DISEASES/assets/110081008/88809ab0-e7ed-4f56-aace-5784595d14bd)

**We can see from the graph that the loss is decreasing and the accuracy is increasing with the increase in the epochs**

### MAKE A PREDICTION ON THE VAL SET
#### GET Y_PRED AS INDEX VALUES
#### GET Y_TRUE AS INDEX VALUES
### COMPARE Y_TRUE & Y_PRED
[2 1 0 1 0 0 2 1 0 0 2 1 1 1 2]

[2 1 0 1 0 0 2 1 0 0 2 2 1 1 2]

## CONFUSION MATRIX & CLASSIFICATION REPORT
![image](https://github.com/Tanwar-12/DETECTING-RICE-LEAF-DISEASES/assets/110081008/f8a13b74-63f8-4ec0-86ec-c903e12db5b5)


     precision               recall     f1-score    support

     bacterial_leaf_blight     1.00      1.00         1.00         5
           brown_spot          0.83      1.00         0.91         5
            leaf_smut          1.00      0.80         0.89         5

             accuracy                                 0.93        15
            macro avg          0.94      0.93         0.93        15
         weighted avg          0.94      0.93         0.93        15
  ## TESTING OUR MODEL WITH RANDOM PICTURE DOWNLOADED FROM GOOGLE 
  ![image](https://github.com/Tanwar-12/DETECTING-RICE-LEAF-DISEASES/assets/110081008/0abd8916-f408-4e40-8380-caeb6896f25f)
  ![image](https://github.com/Tanwar-12/DETECTING-RICE-LEAF-DISEASES/assets/110081008/62bb0f3b-c93f-44a0-90ee-e7d6411d494a)
  ![image](https://github.com/Tanwar-12/DETECTING-RICE-LEAF-DISEASES/assets/110081008/52053f58-b7c9-4d09-b470-85299bf0a2b2)

  ## CONCLUSION:
* We have used 25 images from bacterial blight,brown spot class and 24 from leaf smut class for training (104 training images)
* We have used 5 images from each class for validation (15 validation images)
* Created an image directory
* Fine tuned a MobileNet model that was pre-trained on imagenet.
* Used Adam optimizer, categorical crossentropy loss and a constant learning rate of 0.0001
* We have used callbacks such as EarlyStopping, ReduceLROnPlateau, ModelCheckpoint,LearningRateScheduler
* We didn't use the pre-processing method that was applied to the imagenet images that were used to pre-train Mobilenet. Instead we normalized all images by dividing by 255.
* Performed image augmentation using the Albumentations library. Image augmentation helped to reduce overfitting, improved our model performance and helped the model to generalize better.
We predicted the random images from Google to check the working of our model




