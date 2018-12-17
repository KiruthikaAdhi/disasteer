# Disasteer

Smart Navigation App that steers you clear during disasters


## DISASTER MANAGEMENT, RELIEF AND RECOVERY WITH OUR APPLICATION :
  Our application plays an important role in disaster management, relief and recovery.  
  It can be used for the following purposes :
  1) It can be used by Motorists to find damage road and take a safe route which is not damaged, thus it saves lives of the motorists.
  2) It can be used by Emergency responders to efficiently operate their disaster relief operations by avoiding the damaged roads and reach people in need quickly.
  3) It can be used by Government Officials to reconstruct and repair damaged roads thus helping in disaster recovery.
  
## IMPLEMENTATION : 
   The solution we propose is feasible and efficient in the following ways : 
   1) The application depends only on satellite images which is readily available during disasters
   2) The detection can be updated in real time using the post disaster images taken over time
   
   The detection is composed of the following four phases  
   1) Data Collection  
   2) Training an Deep Neural Network for Road Segmentation
   3) Generating Road Segements from Pre and Post Disaster Satellite Images
   4) Find the difference between the pre and post disaster road segments to detect damaged Road
   

### Data Collection   
  The dataset which we have used is the Massachusetts Roads Dataset https://www.cs.toronto.edu/~vmnih/data/.  
  It consists of input images and target Maps
  1) Input Images : It consists of high resolution satellite images
  2) Target Maps : The corresponding maps for the target images
  The following files are used for data collection :
  1) download.py : to scrap the data from https://www.cs.toronto.edu/~vmnih/data/ 
  2) createDataset.py : to create a trainDataset.csv file from input images and target maps  
  The features consists of pixels of input image and label consists of 1 or 0 indicating whether the pixel belongs to road or not. This can be calculated from the target map as follows:  
  
  `If the corressponding pixel for the input satellite image pixel in the target map value is (255,255,255)`  
   `then` 
      `it belong to road`     
   `else` 
      `it does not belong to a road`
      
  ### Training
  The Deep Neural Network DNNClassifier from tensorflow is used for performing the binary classification. The model's accuracy is 82.5%.
  1) train.ipynb : Trains the Deep Neural Network.
  2) Model : The model is saved in the 'model' folder.
  
  ### Road Segmentation
  The pre and post disaster satellite images were taken from Digital Globe Open Data program.
  classify.ipynb : It takes in the trained model and segments the roads from pre and post disaster satellite images
  #### Pre Disaster
  ##### Satellite Image
  ![pre sat](https://github.com/KiruthikaAdhi/safe-route-finder/blob/master/preDisaster/channelviewPre.jpg?raw=true)
  
  ##### Extracted Road Segment
  ![pre road](https://github.com/KiruthikaAdhi/safe-route-finder/blob/master/classify_output/channelviewPreRoad.jpeg?raw=true)
  
  #### Post Disaster
  ##### Satellite Image
  ![post sat](https://github.com/KiruthikaAdhi/safe-route-finder/blob/master/postDisaster/channelview.jpg?raw=true)
  
  ##### Extracted Road Segment
  ![post road](https://github.com/KiruthikaAdhi/safe-route-finder/blob/master/classify_output/channelviewPostRoad.jpeg?raw=true)
  
  ### Damage Road detection
  damageRoadDetector.ipynb : The two road segments are compared and the difference between the roads is detected as damaged road.
  
  #### Difference between pre and post disaster road segments
  ![diff](https://github.com/KiruthikaAdhi/safe-route-finder/blob/master/damageRoad.jpeg?raw=true)
  
  #### Overlay on the Post Disaster Image
  ![overlay](https://github.com/KiruthikaAdhi/safe-route-finder/blob/master/overlayDamagedRoad.jpeg?raw=true)
