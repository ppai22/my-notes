## 1 - Load data using ImageDataGenerator

```python
import tensorflow as tf

TRAIN_DATA_PATH = '.\\Datasets\\train\\'
generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1.0/255.0)
train_generator = generator.flow_from_directory(
    directory=TRAIN_DATA_PATH,
    target_size=(224, 224),
    batch_size=32,
    shuffle=True,
    class_mode='categorical'
)
```
[Reference](https://towardsdatascience.com/keras-data-generators-and-how-to-use-them-b69129ed779c)

## 2 - Use of fit_generator method

```python
model.fit_generator(
    train_generator,
    steps_per_epoch=2000,
    epochs=50,
    validation_data=validation_generator,
    validation_steps=800)
```
```steps_per_epoch``` parameter generally is calculated as ```NO_OF_ITEMS_IN_DATASET // BATCH_SIZE```<br>
[Reference](https://towardsdatascience.com/keras-data-generators-and-how-to-use-them-b69129ed779c)
