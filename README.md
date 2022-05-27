## Proyecto LM Final (1º Parte)

---

### -La ejecución y salida de 3 peticiones a la API principal (si eliges dos API, solo a una de ella) utilizando curl. Estas peticiones se harán sobre URL con parámetros.

* Todos los hosts que tengan el puerto 22 abierto filtrado por organizaciones y sistemas operativos.

![image](https://github.com/Pacodiz02/ProyectoFinal_LM-Parte1/blob/main/doc/img/consulta1.png)



* Toda la informacióm referente a la dirección IP que le pongamos.(Servicios,protocolos,organización a la que perteneze, puertos, etc.)

![image](https://github.com/Pacodiz02/ProyectoFinal_LM-Parte1/blob/main/doc/img/consulta2.1.png)

![image](https://github.com/Pacodiz02/ProyectoFinal_LM-Parte1/blob/main/doc/img/consulta2.png)


* Todos los puertos que rastrea shodan por internet.

![image](https://github.com/Pacodiz02/ProyectoFinal_LM-Parte1/blob/main/doc/img/consulta3.png)


### -3 programas python que muestren información de las consultas a la API (se pueden usar las mismas consultas que has utilizado en el punto anterior) utilizando la librería requests. Una descripción de lo que va a hacer tu aplicación web utilizando estos servicios web.

- Programa 1
El programa nos pregunta por un puerto y nos dice cuantos dispositivos encuentra con ese puerto abierto en la red. También nos da la opción de utilizar un filtro para la busqueda(org,os).

![image](https://github.com/Pacodiz02/ProyectoFinal_LM-Parte1/blob/main/prog1/comprobacion_si_programa1.png)


- Programa 2
El programa nos pide que introduzcamos una dirección IP y nos muestra toda la información que recopila sobre ella.(Servicios,protocolos,organización a la que perteneze, puertos, etc.)

![image](https://github.com/Pacodiz02/ProyectoFinal_LM-Parte1/blob/main/prog2/comprobacion2_programa2.png)

![image](https://github.com/Pacodiz02/ProyectoFinal_LM-Parte1/blob/main/prog2/comprobacion1_programa2.png)

![image](https://github.com/Pacodiz02/ProyectoFinal_LM-Parte1/blob/main/prog2/comprobacion3_programa2.png)


- Programa 3
El programa nos da a elegir si mostrar una lista de puertos que rastrea shodan o otra de protocolos.

![image](https://github.com/Pacodiz02/ProyectoFinal_LM-Parte1/blob/main/prog3/comprobacion1_ports_programa3.png)

![image](https://github.com/Pacodiz02/ProyectoFinal_LM-Parte1/blob/main/prog3/comprobacion2_ports_programa3.png)

![image](https://github.com/Pacodiz02/ProyectoFinal_LM-Parte1/blob/main/prog3/comprobacion1_protocols_programa3.png)

![image](https://github.com/Pacodiz02/ProyectoFinal_LM-Parte1/blob/main/prog3/comprobacion2_protocols_programa3.png)


### -Las URL de la docuementación del servicio web (o servicios) que vais a utilizar.

URL de la documentación de la API: https://developer.shodan.io/api
