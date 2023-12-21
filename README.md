# SecureTrack-HR
[![wakatime](https://wakatime.com/badge/github/Aby-ss/SecureTrack-HR.svg)](https://wakatime.com/badge/github/Aby-ss/SecureTrack-HR)

**In designing an Employee Management System integrating face recognition for attendance with an SQL Database, the core architecture revolves around efficient data management, authentication, and system integration. The SQL Database serves as the backbone for storing employee data, payroll information, scheduling, and attendance records.**

**The system begins with the SQL Database schema setup, encompassing tables for Employees, Payroll, Scheduling, and potentially a separate table for biometric data linked to employees' profiles. These tables store employee details, salary information, schedules, and attendance records, ensuring a comprehensive repository for managing workforce-related data.**

```python
# Functionality for face recognition and attendance logging
def recognize_face(image):
    employee_id = match_face_to_employee(image)
    if employee_id:
        log_attendance(employee_id, timestamp, status='clock-in')
        return f"Attendance recorded for employee ID: {employee_id}"
    else:
        return "Face not recognized. Access denied."
```

**The integration of face recognition occurs at designated entry points or terminals within the organization. Upon capturing an employee's facial features, the system employs face recognition libraries to match the detected face with the encoded biometric data stored securely in the SQL Database. This recognition process leads to the logging of attendance with the associated employee ID and timestamp.**

**The SQL Database integrates not only attendance-related data but also handles payroll information. The Payroll table connects to the Employees table, storing salary details, tax information, deductions, and payment history.**

```sql
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    -- Other employee details
);

CREATE TABLE Payroll (
    payroll_id INT PRIMARY KEY,
    employee_id INT,
    salary DECIMAL(10, 2),
    -- Other payroll details
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);
```

**This database linkage facilitates automated salary processing, leveraging attendance records for accurate salary calculations, considering leaves, overtime, and bonuses. Administrators can generate payroll reports using SQL queries, providing insights for financial analysis and compliance checks.**

**The system's security is paramount, especially concerning biometric data. Employing encryption techniques, the system encrypts and securely stores biometric information in the SQL Database. Access controls and permissions are implemented rigorously, ensuring only authorized personnel can access sensitive employee data and biometric information.**

**API integration and a user-friendly web interface enhance the system's functionality. APIs enable seamless interaction with the system, allowing for data retrieval, attendance logging, and schedule updates. Meanwhile, the web interface empowers administrators and employees to manage schedules, view attendance records, and access payroll information with ease.**


**Incorporating "Teachable Machines" into the development process involves leveraging its capabilities to create a base Keras model for facial recognition. Initially, gather a diverse dataset of facial images representing employees within the system. Utilize "Teachable Machines" to train a machine learning model, perhaps a Convolutional Neural Network (CNN), to recognize these faces.**

**Upon training, export the model, integrating it into the Employee Management System's architecture. Use the OpenCV library in Python to handle the integration and execution of the trained model for facial recognition.**

```python
# Sample code snippet for using OpenCV with the trained Keras model
import cv2
from keras.models import load_model

# Load the trained Keras model
model = load_model('trained_model.h5')

# Initialize OpenCV's face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)  # Access the webcam

while True:
    ret, frame = cap.read()  # Capture video frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        face_roi = gray[y:y + h, x:x + w]  # Region of interest containing the face
        # Preprocess the face_roi if needed (e.g., resize, normalize)

        # Use the loaded model for face recognition
        predicted_employee = model.predict(face_roi)  # Make predictions

        # Perform actions based on the predicted employee
        # Log attendance, grant access, etc., based on the prediction

    cv2.imshow('Face Recognition', frame)  # Display the frame with face detection

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()  # Release the webcam
cv2.destroyAllWindows()  # Close all OpenCV windows
```

**This integration allows real-time face detection using OpenCV while utilizing the trained Keras model for face recognition within the Employee Management System. As employees present themselves for attendance, the system captures their facial features, employs the model for recognition, and executes designated actions like logging attendance or granting access based on the recognized employee's identity.**
