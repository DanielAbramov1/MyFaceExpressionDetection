img_size = 48
# batch_size = 64
# datagen_train = ImageDataGenerator(horizontal_flip=True)
# train_generator = datagen_train.flow_from_directory("PATH OF TRAIN FOLDER",
#                                                     target_size=(img_size,img_size),
#                                                     color_mode="grayscale",
#                                                     batch_size=batch_size,
#                                                     class_mode='categorical',
#                                                     shuffle=True)
# datagen_validation = ImageDataGenerator(horizontal_flip=True)
# validation_generator = datagen_validation.flow_from_directory("PATH OF TEST FOLDER",
#                                                     target_size=(img_size,img_size),
#                                                     color_mode="grayscale",
#                                                     batch_size=batch_size,
#                                                     class_mode='categorical',
#                                                     shuffle=False)