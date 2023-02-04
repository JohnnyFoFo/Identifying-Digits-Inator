from PIL import Image
from matplotlib import pyplot,image
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from keras.models import Sequential, model_from_json
from keras.layers import Dense, Dropout, Activation, LeakyReLU, Flatten
from keras.metrics import AUC
from keras import backend as K
from keras.datasets import mnist
from skimage import color
from matplotlib import image
from matplotlib import pyplot
import numpy as np

class NumberSolver:
    
    def __init__(self, filename: str, typefilename: str ):
        self.filename = filename
        self.typefilename = typefilename
    


    def resize_recolor(self):
        original_image = Image.open(f"{self.filename}{self.typefilename}")
        smaller_image = original_image.resize((28,28))
        gray_small_image = smaller_image.convert('L')
        gray_small_image.save(self.filename + 'new' + self.typefilename)

    
    def create_pixels(self):
        im = image.imread(self.filename + 'new' + self.typefilename)
        new_image = im.copy()
        new_image.setflags(write=1)
        new_image[new_image > .5] = 0
        final_image = new_image.astype(float)
        return np.array([final_image])
        
    def load_runModel(self,pixels):
        
        json_file = open('model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights("model.h5")
        
        print("Loaded model from disk")
        
    
        loaded_model.compile(
            loss='sparse_categorical_crossentropy',
            optimizer='adam',
            metrics=['accuracy'])
        loaded_model.summary()
        
        predictions = loaded_model.predict(pixels)
        print(predictions)
        
        chosen_predict = {
            "predicted": -1,
            "Strength": 0
        }
        
        
        for i in range(9):
            if predictions[0][i] > chosen_predict['Strength']:
                chosen_predict["Strength"] = predictions[0][i]
                chosen_predict["predicted"] = i
            
                
           
        return chosen_predict["predicted"]
       # return f"""
      #  0: {predictions[0][0]}   
     #   1: {predictions[0][1]}
      #  2:{predictions[0][2]}
      #  3:{predictions[0][3]}
      #  4:{predictions[0][4]}
      #  5:{predictions[0][5]}
       # 6:{predictions[0][6]}
       # 7:{predictions[0][7]}
       # 8:{predictions[0][8]}
       # 9:{predictions[0][9]}
        
#"""
        
        
        #get_3rd_layer_output = K.function([loaded_model.layers[0].input],[loaded_model.layers[3].output])
                
       # layerIndex = 1
       # func = K.function([loaded_model.get_layer('flatten_1').input], loaded_model.get_layer('dense_3').output)
        #layerOutput = func([np.array([self.number],dtype=np.uint8)])
       # 
       

    #loaded_model.predict(np.array([self.number], dtype=np.uint8))
    
    
    #loaded_model.get_layer(name="dense_3").output
    
    
#loaded_model.evaluate(pixels,np.array([self.number], dtype=np.uint8))

       
 #export function      

def main_func(name,typ):
                                  
    obj = NumberSolver(name,typ)
    obj.resize_recolor()
    pixels = obj.create_pixels()
    return (obj.load_runModel(pixels))
                                  
#print(main_func('THREEEEEEE','.png',3)) 
        
  
