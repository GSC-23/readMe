# PupSense
PupSense is an IoT and ML based app that helps dogs in case of accidents by detecting their sounds and alerting the app.
It is a solution for all animal lovers and the ones hoping to change the scenario around.
It uses Convolutional Neural Network (CNN) layers to analyze the audio properties of a dog's bark and determine if they are in distress due to an accident. The app then updates data in Firebase, which notifies app users and NGOs nearby who can help the dog using nearby hospital locations shown in the app.

The solution also includes the use of cameras and built-in microphones in society cameras to increase its use cases. Additionally, PupSense can be used with a cost-effective IoT device that includes a microphone and GPU module.

# Getting Started
To get started with PupSense, download the app from the app store and create an account. Once you've logged in, you'll be taken to the home screen, where you can enable location and notifications.

# Using PupSense
PupSense is an automated to solution to save dog lives. If the app detects a sound, it will use its ML model to determine if the dog is in distress due to an accident. If so, it will send an alert notification to all the users nearby. The notification will include directions to the incident location and information about nearby veterinary and NGOs.

If you're near the incident location, you can use the directions provided by the app to reach the dog quickly. Once you've arrived, you can use the information about nearby veterinary to take the dog to the nearest facility for treatment. You may also contact the NGO for any kind of help.

After the incident is resolved, you can share your experience via posts. This will help other users learn from your experience and potentially save more dogs in the future.


The ML model could be loaded to the security cameras of different societies and nearby areas, where any voluntary dog lover can install the app and send the help immediately in case of any incident. So, a person from each society, NGOs and different animal lovers registered to the application can come together to save the lives of these beautiful creatures.

# Technologies Used
1. TensorFlow
2. Firebase
3. Python and related libraries
4. Android studio
5. Kotlin
6. Google maps SDK, APIs and related libraries
7. Google Colaboratory

![Blank diagram](https://user-images.githubusercontent.com/90051748/229815604-686358d1-dbf4-4c42-8164-7d589d6105a2.svg)


## IoT device
This project utilizes custom devices and repurposes audio output from pre-existing security cameras to create a prototype security system called pupSense. The prototype incorporates a Raspberry Pi as an IoT device with a microphone to capture sounds from the surroundings. A machine learning model is deployed on the device itself and is programmed to detect specific events. When an event is detected, a signal is sent to a database.

## ML model
Using CNN and TensorFlow, we have built the model detecting the dog bark. To make the accuracy as high as 92%, we have used [UrbanSound8k Dataset](https://urbansounddataset.weebly.com/urbansound8k.html) and built a sequential model, thus training upto 100 epochs.
To identify the crying dog, we are working upon its dataset to get the audio properties such as MFCC properties, Mel spectrogram, Frequency plots
A few audio Properties of a wav file using [audio processing.py](https://github.com/GSC-23/solution/blob/main/audio_processing.py)
![image](https://user-images.githubusercontent.com/90051748/229173239-0112f75e-37d6-4aef-a2c9-806d531db007.png)
![image](https://user-images.githubusercontent.com/90051748/229174137-ed4d6392-380a-46ad-abd8-78ab756267f3.png)
![image](https://user-images.githubusercontent.com/90051748/229174240-3f798687-8a29-4847-b3a4-03ce1909dbc4.png)

Using the audio processing file, we can create the dataset of different animals and then train our model to make the solution versatile for all animals

## Application
The mobile application is a sophisticated, native Android application developed exclusively using Kotlin within the Android Studio environment. As for its backend, it employs the full range of functionalities offered by the Google Firebase platform. Specifically, Firebase Authentication is utilized to provide secure email authentication, while Firebase Firestore is employed for efficient data storage. Additionally, the application seamlessly integrates the Google Maps Software Development Kit (SDK) to enable the accurate display of the location pinpointed by the Internet of Things (IoT) device. To further enhance the user experience, the Google Places API is integrated to facilitate the identification of nearby veterinary hospitals. Moreover, the Google Directions API enables the app to provide the most efficient pathway from the user's location to the incident location, while the Google Maps Static API supplies static images of the optimal route from the incident location to the nearest veterinary hospital.

# Future Scope
The solution's versatility could be extended to different animals and technology, to take the audio and video input. Its use case could be further extended to variety of animals. 

# Conclusion
PupSense is a valuable tool for dog owners and lovers alike. By detecting dogs in distress using ML-based technology and providing directions to the incident location, and information about nearby veterinary, PupSense can help save lives. Additionally, by creating blog posts about their experiences, users can help others learn from their experiences and potentially save more dogs in the future. The app's IoT capabilities and integration with cameras and microphones in society cameras further extend its use cases, and it can be used for other animals as well.
