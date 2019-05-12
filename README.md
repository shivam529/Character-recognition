# Character-recognition
Using TensorFlow's ImageNet model to identify digits from an image.<br>
The driver file is test.py<br>
Not required to run train.py which was used to generate training images.<br>
I standardized the training images to size 30x30 and centered their centre of masses and similary test images were pre processed the same way before classifying(predicting them)<br>
I used TensorFlow's ImageNet architecture using the retrain.py(again not required to run) which creates a model for us which can be re used again and again.<br>
The test images used for this model were made from train.py and all the images were replicated 10 times since TensorFlow model requires atleast 20 images.<br>
I Didn't think roatation of images were required for the given test images and the results can be seen test_results1,2,3.png respectively with just one error,which could be improved with much more training data.<br>
Also for this small scale problem, template matching would be enough as can be seen in my Sudoku Detection(augmented reality) project in my Github Repository.<br>
The train image files and the saved model graph is in this link: https://drive.google.com/open?id=113jpgg3iuiCUpjver6YQalZKBYxnNYzzit needs to be in the same folder as all the other files. The files needed to be downloaded are: <br>
1: retrained_graph.pb <br>
2: Train 1 folder containig train images.(not required to download although)
