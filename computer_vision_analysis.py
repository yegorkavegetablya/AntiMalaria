def some_cool_neuronet_function(image_path):
    model = keras.models.load_model('Malaria Cells.h5')
    image = cv2.imread('path')
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
