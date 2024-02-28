#Welcome to the Coin Counter project! This sophisticated computer vision-based system is crafted to meticulously analyze live video input, allowing for the precise detection and identification of various coins, each with its assigned value. Leveraging the power of openCV, cvzone, and numpy libraries, this project excels in preprocessing images for accurate analysis. It is noteworthy that the system accomplishes these objectives without relying on any machine learning or deep learning algorithms.# Coin-Counter

#Project Structure:
main.py
The cornerstone of the project, main.py orchestrates live video processing. It dynamically fetches data from a user-specified URL (replace with your own), employing an arsenal of image processing techniques to robustly identify and evaluate coins within the video feed. The script showcases the capabilities of the cvzone library, particularly in contour detection and color analysis.

gui_main.py
For those seeking a more interactive and user-friendly experience, gui_main.py steps in with an intuitive graphical user interface (GUI). This GUI allows users to seamlessly upload an image for analysis using the "Upload File" button. Developed with the customtkinter library, this interface seamlessly incorporates the functionalities present in main.py.

areaValues.txt
This file provides an extra layer of sophistication by incorporating detailed logic for assigning values to coins based on their individual areas. It comprises a set of conditions meticulously crafted to determine the value of a coin based on its specific size.

requirements.txt
To ensure a seamless and hassle-free execution of the project, it is crucial to install the specified dependencies listed in the requirements.txt file.


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Coin Counter Project

Welcome to the Coin Counter project! This computer vision-based system is designed to analyze live video input for the detection and identification of various coins, along with their respective values. The project uses openCV, cvzone, and numpy libraries to preprocess the images for accurate analysis. Importantly, the system achieves these objectives without the use of any machine learning or deep learning algorithms.

## Files:

### `main.py`

This file contains the main code for the project, focusing on live video processing. It fetches data from a specified URL (replace with your own) and applies various image processing techniques to identify and evaluate coins in the video feed. The script uses the cvzone library for contour detection and color analysis.

### `gui_main.py`

For a more interactive experience, `gui_main.py` offers a graphical user interface (GUI). Users can upload an image for analysis using the "Upload File" button. The GUI is built using the customtkinter library and incorporates the functionalities from `main.py`.

### `areaValues.txt`

This file includes additional logic for assigning values to coins based on their area. It provides a set of conditions to determine the value of a coin based on its size.

### `requirements.txt`

To ensure a smooth run of the project, make sure to install the necessary dependencies listed in this file. You can install them using the command:

```bash
pip install -r requirements.txt


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Credits:
This collaborative project was developed by the following talented contributors:

Anirudha Upadhyay
Aditya Kudikala
Aayush Vishnoi
Ankna Litoriya
