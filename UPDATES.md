### Update 01
- Created a new GitHub repository for the pet expression classification project.
- Installed necessary libraries including TensorFlow, Keras, OpenCV, NumPy, and Pandas.
- Downloaded the Pet's Facial Expression Image Dataset from Kaggle and explored its structure.
- Committed the initial project structure, including a README file outlining project goals and objectives.
### Update 02
Obsevation from the first training phase :
- The training accuracy increases steadily and approaches 100%, indicating the model fits the training data well.
- The validation accuracy fluctuates and remains significantly lower, showing poor generalization to unseen data.
### Update 03
Attempt to resolve the overfitting issue by using
- Data Augmentation
- Smaller Model Architecture
- Dropout Layers
- Early Stopping
### Update 04
Using transfer learning to improve the performance of the pet expression classification model
- Loaded the pre-trained VGG16 model without the top classification layer.
- Added custom layers for pet expression classification, including a global average pooling layer and dense layers.
- Evaluated the accuracy and loss parameters after the model was trained.
### Update 05
Evaluated model performance on test data with confusion matrix

![image](https://github.com/user-attachments/assets/bf5df560-c6bc-4291-99f1-ee573bf7e564)

### Update 06
Implemented Transfer Learning using a model trained on Animal Dataset for Pet Expression Classification
- Trained a model on an animal dataset consisting of classes like cat, dog, and other animals.
- Defined a convolutional neural network (CNN) architecture for the animal classification task.
- Trained the model and monitored training and validation accuracy/loss.
- Saved the trained animal classifier model for future use in transfer learning.
- Applied transfer learning by using the trained animal model to classify pet expressions.

After evaluating the performance of the model trained using animal model as the base model, it was found that the model did not yield satisfactory results for classifying pet expressions. Consequently, shifting our approach to utilize transfer learning with the VGG16 model, which has demonstrated better effectiveness in image classification tasks.

