# Dietary Management System for Campus Dining using Face Recognition

I have always wondered what would happen if the students in our school consume food that they are severely allergic to? 
What if they were not aware that the food contains those harmful ingredients? 
These thoughts came across to me when I faced up a disappointing news article talking about a student passing out from allergens. 
This is when I decided to take action about the circumstance and create a system that would prevent these incidents from happening. 

## Table of Content 
- [Set up the environment](https://github.com/SadDONUT1/Dietary-Management-System-for-Campus-Dining-using-Face-Recognition?tab=readme-ov-file#set-up-the-environment)
- [Step by Step on how to run the program](https://github.com/SadDONUT1/Dietary-Management-System-for-Campus-Dining-using-Face-Recognition?tab=readme-ov-file#step-by-step-on-how-to-run-the-program)
- [Editing few lines of code](https://github.com/SadDONUT1/Dietary-Management-System-for-Campus-Dining-using-Face-Recognition?tab=readme-ov-file#editing-few-lines-of-code)

## Set up the environment 
1. [Python](https://www.python.org/downloads/)
2. Install required python library modules
   
   a) open cv (pip install opencv-python)
   
   b) numpy (pip install numpy)
   
   c) pillow (pip install pillow)
   
   d) requests (pip install requests)

   e) tkinter (pip install tk)
   
4. [Download required algorithm file](https://github.com/kipr/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)

## Step by Step on how to run the program 

<img align = "right" width="500" alt="four_files" src="https://github.com/user-attachments/assets/35b06921-ede1-4109-a183-81d87279d71c">

1. Download four python files on the file list

2. Create a folder and name it as you want

3. In that folder, add all the files that you have downloaded

4. Create an empty folder called "dataset" and "trainer"

<img align = "centre" width="250" alt="four_files" src="https://github.com/user-attachments/assets/a68dae9a-ca51-45ef-8a9d-50bec7780f81">

## Editing few lines of code
### Changing paths of file according to the user's detail

1. Edit the first "face initialisation" file by copying the path of algorithm file and pasting it on line 4

2. Change line 33 to the path of your dataset folder

3. Move on to the second file and change line 6 to path of dataset folder

4. Change line 9 to algorithm file path and line 38 to path of trainer and add /trainer.yml at the end

5. Carry on to the third file and edit line 10 and 13 to "trainer.yml" path and algorithm file respectively

6. Change the host as your current IP address (_$ipconfig getifaddr en0 for mac_), same for the next file 

7. and.. you are ready!
   


