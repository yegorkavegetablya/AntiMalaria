import keras
import cv2
import numpy as np

img_size = (224, 224)
# g_dict = train_gen.class_indices
# classes = list(g_dict.keys())
classes = ['Uninfected', 'Infected']

def some_cool_neuronet_function(image_path):
    global img_size, classes

    model = keras.models.load_model('Malaria_Cells.h5')
    image = cv2.imread(image_path)
    image = cv2.resize(image, img_size)  # Приведение изображения к нужному размеру
    image = image / 255.0  # Масштабирование значений пикселей
    prediction = model.predict(np.expand_dims(image, axis=0))  # Предсказание для одного изображения

# Получение наиболее вероятного класса
    predicted_class = np.argmax(prediction)
    class_name = classes[predicted_class]
    if class_name == 'Uninfected':
        return 0
    else:
        return 1
