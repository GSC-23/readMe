import numpy as np
from keras.models import load_model
import librosa 
import numpy as np 
import pickle

model = load_model('C:/Users/jiya/Desktop/demo_dogs/weights.best.basic_mlp.hdf5')      # Change the path

# pickle_in = open('C:/Users/jiya/Desktop/demo_dogs/model trained.p','rb')
# model = pickle.load(pickle_in)

def extract_feature(file_name):
   
    try:
        audio_data, sample_rate = librosa.load(file_name) 
        mfccs = librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=40)
        mfccsscaled = np.mean(mfccs.T,axis=0)
        
    except Exception as e:
        print("Error encountered while parsing file: ")
        return None, None

    return np.array([mfccsscaled])


def print_prediction(file_name):
    prediction_feature = extract_feature(file_name) 

    predicted_vector = model.predict(prediction_feature)
    array=predicted_vector[0]
    m=np.amax(array)
    print("Accuracy:",m)
    if(m==array[3]):
      print("Dog Detected")
    else:
      print("No Dog Detected")
    # print("The predicted class is:", array, '\n') 
    
filename = input("Enter full path of audio(.wav) file: ") 
print_prediction(filename)