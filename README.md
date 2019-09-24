# Video_Face_Recognition


## About this repo:  
This repository represents a simple app that aims to recognize faces from a video streaming.  
It has been tested on a PC running on Ubuntu and a Raspberry Pi running on Raspbian using Python 3+ with both.    


## Content:  

- **Cascades:** a folder containing `haarcascade_frontalface_default.xml`, the file that is used for face detection.  
- **dataset:** a folder that will contain the training data (the photos that will be taken for the users).  
- **templates:** a folder containing `index.html`, the file used to display the video-streaming on the browser.  
- **trainer:** a folder containing `trainer.yml`the file used for training.  
- **camera.py:** the file that's used to capture the video.  
- **facedataset.py:** the files used to take the photos of the user (to prepare the dataset).  
- **facetraining.py:** the file that's used to train the classifier on the dataset.  
- **main.py:** the file used to run the face recognition.  
- **requirements.txt:** a text file containing the needed packages to run the project.  

## Usage:  

*NB: Use python 3+ only.* 

**1. Clone the repo:** `git clone https://github.com/maky-hnou/Video_Face_Recognition.git`  
**2. Get into the cloned repo:** `cd Video_Face_Recognition/`  
**3. Install the requirements:** `pip3 install -r requirements.txt`  
**4. Add the new user name:** open the file `camera.py` with your preferred editor, then add the new username to `names = ['None']` to be `names = ['None', 'Alex']` (Suppose that the new username is Alex).  
**5. Create new dataset:** `python3 facedataset.py` You'll be asked to enter the new user ID (1 for the first user and so on).
**6. Train the classifier:** `python3 facetraining.py`  
**7. Test the face recognition:** `python3 main.py` Then open http://0.0.0.0:5000/ on your browser.  
