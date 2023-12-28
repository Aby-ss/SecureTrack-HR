from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np
import sqlite3
import datetime

from rich import print, box, text


from rich.align import Align
from rich.panel import Panel

from rich.prompt import Prompt
from rich.progress import track
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn

from rich.traceback import install
install(show_locals=True)

# Database connection
employee_conn = sqlite3.connect("EmployeeDatabase.db")
cursor = employee_conn.cursor()

def clock_in_employee(employee_name):
    current_time = datetime.datetime.now()
    try:
        cursor.execute("UPDATE EmployeeDatabase SET ClockIn = ? WHERE Name = ?", (current_time.strftime("%Y-%m-%d %H:%M:%S"), employee_name))
        employee_conn.commit()
        print(f"Clocked In at {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(f"Error during Clock-In: {e}")

def clock_out_employee(employee_name):
    current_time = datetime.datetime.now()
    try:
        cursor.execute("UPDATE EmployeeDatabase SET ClockOut = ? WHERE Name = ?", (current_time.strftime("%Y-%m-%d %H:%M:%S"), employee_name))
        employee_conn.commit()
        print(f"Clocked Out at {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(f"Error during Clock-Out: {e}")

print(Panel.fit("Choose an Option:\n1- Clock In for the day\n2- Clock Out of Work", box=box.SQUARE, border_style="bold white"))
user_choice = Prompt.ask("Enter a Choice")

employee_name = "Rao"  # Replace with the actual employee name

if int(user_choice) == 1:
    clock_in_employee(employee_name)
elif int(user_choice) == 2:
    clock_out_employee(employee_name)

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)
confidence_threshold = 0.8

while True:
    ret, image = camera.read()
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    cv2.imshow("Webcam Image", image)

    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    image = (image / 127.5) - 1

    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = prediction[0][index]

    if confidence_score > confidence_threshold:
        print(Panel.fit(f"Class: {class_name}\nConfidence Score: {str(np.round(confidence_score * 100))[:-2]}%", border_style="bold green", box=box.SQUARE))

    keyboard_input = cv2.waitKey(1)
    if keyboard_input == 27:  # ASCII for the esc key
        break

camera.release()
cv2.destroyAllWindows()
employee_conn.close()