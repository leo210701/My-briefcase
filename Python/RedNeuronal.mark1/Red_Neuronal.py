#Por si no se entiende estoy haciendo una red nueronal para pasar pulgadas a metros
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#Estoy declarando los enventos
entrada = np.array([1, 6, 30, 7, 70, 43, 503, 201, 1005, 99], dtype=float)
resultados = np.array([0.254, 0.1524, 0.762, 0.1778, 1.778, 1.0922, 12.776, 5.1054, 25.527, 2.514], dtype=float)

#Ahora se crea la topografia de la red, obvio sera sencilla una capa de entrada y otra de salida 
capa1 = tf.keras.layers.Dense(units=1, input_shape= [1]) #Aunque en vez de ser una red neuronal solo parece mi unica chucaracha jugando sola

#Se crea el tipo de red
modelo = tf.keras.Sequential([capa1])

# Asigno el optimizador y la metrica de perdidas, -En cristiano-, hago que la misma red se vaya autocorrigiendo en caso de un error 
# a medida que se vaya entrenando
modelo.compile(
    optimizer = tf.keras.optimizers.Adam(0.1),
    loss = 'mean_squared_error'
)
print("Entrenando la red")

#Procedemos a entrenar el modelo
entrenar = modelo.fit(entrada, resultados, epochs=600, verbose=False)

#Guardamos la red
modelo.save('RedNeuronal.mark1')
modelo.save_weights('pesos.mark1')

#Para ver como se comporta la cucaracha
plt.xlabel("Ciclos de entrenamiento")
plt.ylabel("Errores")
plt.plot(entrenar.history["loss"])
plt.show()

#Verifico que la red este entrenada
print("Terminamos")

# Creo la Prediccion
i= input("Digita el valor a pulgadas:")
i = float(i)
prediccion = modelo.predict([i])
print("El valor en metros es: ", str(prediccion))