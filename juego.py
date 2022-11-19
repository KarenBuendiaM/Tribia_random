from tkinter import *  # importamos la interfaz de tkinter para que corra el juego

def seleccionar (evento):  #creamos la funcion sellecionar que es la que corre todo el juego
    b = evento.widget
    val = b['text']

    for i in range(40): #con el for recorremos todas las preguntas del juego

        if val ==  respuestas_correctas[i]: #con este if miramos que pasa si la opcion elegida es correcta

            if val == respuestas_correctas[39]: 
                def cierre (): #funcion en donde cerramos la ventana del juego y la ventana que aparece cuando se gana el juego
                    ventana_2.destroy()
                    ventana.destroy()
                
                def jugar_nuevamente(): #esta funcion nos permite volver a jugar el juego
                    ayuda_50_50.config(image = img_50_50, state = NORMAL)
                    ayuda_sig_preg.config(image = img_sig_preg, state = NORMAL)
                    ventana_2.destroy() #cerramos la segunda ventana
                    marco_preguntas.delete(1.0, END)  #desde aqui se reinicia el juego, tomando el indice 0 de las listas quecreamos 
                    marco_preguntas.insert(END, total_preguntas[0])
                    opcion_a_boton.config(text = opciones_a[0])
                    opcion_b_boton.config(text = opciones_b[0])
                    opcion_c_boton.config(text = opciones_c[0])
                    opcion_d_boton.config(text = opciones_d)
                    ventana_2.destroy()
                
                #parte visual de como se ve lasegunda ventana
                ventana_2 = Toplevel()
                ventana_2.overrideredirect(True)
                ventana_2.config(background = '#5271ff') #fondo
                ventana_2.geometry('500x400+140+30') #dimensiones 
                ventana_2.title("ganaste $4.000.000") #titulo
                img_logo_2 = Label(ventana_2, image = img_logo, border = 0) #imagen del centro con el logo
                img_logo_2.pack(pady = 30) #espaciado
                ganar = Label(ventana_2, text = "Haz ganado", font = ('arial', 20, 'bold'), background = '#5271ff', foreground = '#ffc172')
                ganar.pack()
                jugar_denuevo = Button(ventana_2, text = "Jugar nuevamente", font = ('arial', 15, 'bold'), background = '#5271ff', foreground = '#ffc172', activebackground = '#5271ff', border = 0, cursor = 'hand2', command = jugar_nuevamente) #boton para jugar denuevo
                jugar_denuevo.pack()
                cierre_o = Button(ventana_2, text = "Abandonar juego", font = ('arial', 15, 'bold'), background = '#5271ff', foreground = '#ffc172', activebackground = '#5271ff', border = 0, cursor = 'hand2', command = cierre) #boton para cerrar el juego
                cierre_o.pack()
                ventana_2.mainloop
                break
            
            marco_preguntas.delete(1.0, END)
            marco_preguntas.insert(END, total_preguntas[i + 1]) #las preguntas se recorren 1 a 1 con sus respectivas opciones y puntos
            opcion_a_boton.config(text = opciones_a[i + 1])
            opcion_b_boton.config(text = opciones_b[i + 1])
            opcion_c_boton.config(text = opciones_c[i + 1])
            opcion_d_boton.config(text = opciones_d[i + 1])
            puntos.config(image = img_pts[i])

        if val not in respuestas_correctas: #con este if miramosque pasa si la opcion elejida es incorecta 

            def intentar_nuevamente(): #funcion para volver a jugar
                ayuda_50_50.config(image = img_50_50, state = NORMAL)
                ayuda_sig_preg.config(image = img_sig_preg, state = NORMAL)
                ventana_1.destroy()
                marco_preguntas.delete(1.0, END)
                marco_preguntas.insert(END, total_preguntas[0]) #aqui se reinicia el juego, tomando el indice 0 de las listas quecreamos 
                opcion_a_boton.config(text = opciones_a[0])
                opcion_b_boton.config(text = opciones_b[0])
                opcion_c_boton.config(text = opciones_c[0])
                opcion_d_boton.config(text = opciones_d[0])
                puntos.config(image = img_pts[0])

            def cerrar_juego(): #funcion para cerra el juego
                ventana_1.destroy()
                ventana.destroy()

            #parte visual de la primera ventana en caso de perder 
            ventana_1 = Toplevel()
            ventana_1.overrideredirect(True)
            ventana_1.config(background = '#5271ff')
            ventana_1.geometry('500x400+30+0')
            ventana_1.title("obtuviste 0 puntos")
            img_logo_1 = Label(ventana_1, image = img_logo, border = 0)
            img_logo_1.pack(pady = 30)
            perder = Label(ventana_1, text = "Perdiste", font = ('arial', 20, 'bold'), background = '#5271ff', foreground = '#ffc172')
            perder.pack()
            intenta_denuevo = Button(ventana_1, text = "Intentalo de nuevo", font = ('arial', 15, 'bold'), background = '#5271ff', foreground = '#ffc172', activebackground = '#5271ff', border = 0, cursor = 'hand2', command = intentar_nuevamente)#boton para jugar denuevo
            intenta_denuevo.pack()
            cerrar = Button(ventana_1, text = "Abandonar juego", font = ('arial', 15, 'bold'), background = '#5271ff', foreground = '#ffc172', activebackground = '#5271ff', border = 0, cursor = 'hand2', command = cerrar_juego) #boton para abandonar el juego
            cerrar.pack()
            ventana_1.mainloop()
            break

def ayuda_50 (): #funcion para eleminar dos opciones incorrectas de cada pregunta
    ayuda_50_50.config(image = img_50_50_x, state = DISABLED)
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[0]:
        opcion_a_boton.config(text = '')
        opcion_d_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[1]:
        opcion_a_boton.config(text = '')
        opcion_c_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[2]:
        opcion_c_boton.config(text = '')
        opcion_d_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[3]:
        opcion_b_boton.config(text = '')
        opcion_c_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[4]:
        opcion_b_boton.config(text = '')
        opcion_c_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[5]:
        opcion_a_boton.config(text = '')
        opcion_b_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[6]:
        opcion_c_boton.config(text = '')
        opcion_d_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[7]:
        opcion_b_boton.config(text = '')
        opcion_d_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[8]:
        opcion_c_boton.config(text = '')
        opcion_d_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[9]:
        opcion_b_boton.config(text = '')
        opcion_d_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[10]:
        opcion_a_boton.config(text = '')
        opcion_c_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[11]:
        opcion_a_boton.config(text = '')
        opcion_c_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[12]:
        opcion_b_boton.config(text = '')
        opcion_d_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[13]:
        opcion_a_boton.config(text = '')
        opcion_d_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[14]:
        opcion_c_boton.config(text = '')
        opcion_d_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[15]:
        opcion_b_boton.config(text = '')
        opcion_d_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[16]:
        opcion_b_boton.config(text = '')
        opcion_c_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[17]:
        opcion_a_boton.config(text = '')
        opcion_b_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[18]:
        opcion_a_boton.config(text = '')
        opcion_c_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[19]:
        opcion_b_boton.config(text = '')
        opcion_c_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[20]:
        opcion_b_boton.config(text = '')
        opcion_d_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[21]:
        opcion_a_boton.config(text = '')
        opcion_d_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[22]:
        opcion_a_boton.config(text = '')
        opcion_d_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[23]:
        opcion_b_boton.config(text = '')
        opcion_c_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[24]:
        opcion_a_boton.config(text = '')
        opcion_d_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[25]:
        opcion_b_boton.config(text = '')
        opcion_d_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[26]:
        opcion_c_boton.config(text = '')
        opcion_b_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[27]:
        opcion_c_boton.config(text = '')
        opcion_d_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[28]:
        opcion_b_boton.config(text = '')
        opcion_d_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[29]:
        opcion_b_boton.config(text = '')
        opcion_c_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[30]:
        opcion_a_boton.config(text = '')
        opcion_b_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[31]:
        opcion_b_boton.config(text = '')
        opcion_d_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[32]:
        opcion_b_boton.config(text = '')
        opcion_c_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[33]:
        opcion_c_boton.config(text = '')
        opcion_d_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[34]:
        opcion_b_boton.config(text = '')
        opcion_c_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[35]:
        opcion_c_boton.config(text = '')
        opcion_d_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[36]:
        opcion_b_boton.config(text = '')
        opcion_c_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[37]:
        opcion_a_boton.config(text = '')
        opcion_c_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[38]:
        opcion_a_boton.config(text = '')
        opcion_b_boton.config(text = '')
    if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[39]:
        opcion_c_boton.config(text = '')
        opcion_d_boton.config(text = '')
        
def ayuda_next_question():
    ayuda_sig_preg.config(image = img_sig_preg_x, state = DISABLED) 
    for i in range(40): #con el for recorremos todas las preguntas del juego
        if marco_preguntas.get(1.0, 'end-1c') == total_preguntas[i]:  #con este if, conocemos cual pregunta se esta realizando
            cont = i
            break
    if cont == 39:#este if se utiliza en caso de que se use la ayuda en la ultima pregunta, por lo cual ganaria el juego
        """Retorna Ganado y pregunta si jugar de nuevo"""
        
    else: #Con este else, cambiamos la pregunta por la siguiente y le sumamos los puntos correpsondientes      
        marco_preguntas.delete(1.0, END)
        marco_preguntas.insert(END, total_preguntas[cont + 1]) #las preguntas se recorren 1 a 1 con sus respectivas opciones y puntos
        opcion_a_boton.config(text = opciones_a[cont + 1])
        opcion_b_boton.config(text = opciones_b[cont + 1])
        opcion_c_boton.config(text = opciones_c[cont + 1])
        opcion_d_boton.config(text = opciones_d[cont + 1])
        puntos.config(image = img_pts[cont])

ventana = Tk()  #creamos la ventana para el juego
ventana.geometry('1270x652+0+0') #creamos las dimensiones de la ventana
ventana.title("Tribia Random") #le asignamos un nombre a la ventana
ventana.config(background = '#5271ff') #le colocamos fondo a la venta 

#dividimos la ventana en dos marcos(verticales): derecho eizquierdo, con sus respectivos fondos y dimensiones
marco_izquierdo = Frame(ventana, background = '#5271ff', padx = 90) 
marco_izquierdo.grid(row = 0, column = 0)
marco_derecho = Frame(ventana, background = '#5271ff', padx = 50, pady = 25)
marco_derecho.grid(row = 0, column = 1)

#en el marco izquierdo  dividimos la ventana en tres marcos: superior, central e inferior, con sus respectivos fondos y dimensiones
marco_superior = Frame(marco_izquierdo, background = '#5271ff', pady = 15)
marco_superior.grid(row = 0, column = 0)
marco_central = Frame(marco_izquierdo, background = '#5271ff', pady = 15)
marco_central.grid(row = 1, column = 0)
marco_inferior = Frame(marco_izquierdo, background = '#5271ff', width = 900, height = 200)
marco_inferior.grid(row = 2, column = 0)

#el logo va en el marco central (en el marco izquierdo)
#aqui ponemos la imagen del logo
img_logo = PhotoImage(file = "logo.png")
logo = Label(marco_central, image = img_logo, background = '#5271ff', border = 0, width = 300, height = 200)
logo.grid(row = 0, column = 0)

#los dos botones van en el marco superior (en el marco izquierdo)
#creamos un boton con la ayuda 50/50 (borra dos respuestas incorrectas de las 4)
img_50_50 = PhotoImage(file = "mitad.png")
img_50_50_x = PhotoImage(file = "mitad_x.png")
ayuda_50_50 = Button(marco_superior, image = img_50_50, background = '#5271ff', border = 0, activebackground = '#5271ff', width = 180, height = 80, command = ayuda_50)
ayuda_50_50.grid(row = 0, column = 0)

#creamos un botos con la ayuda siguiente pregunta(si no se sabe la respuesta se puede pasar a la siguiente)
img_sig_preg = PhotoImage(file = "sig_pregunta.png")
img_sig_preg_x = PhotoImage(file = "sig_pregunta_x.png")
ayuda_sig_preg = Button(marco_superior, image = img_sig_preg, background = '#5271ff', border = 0, activebackground = '#5271ff', width = 180, height = 80, command = ayuda_next_question)
ayuda_sig_preg.grid(row = 0, column = 1)

#los puntos van en el marco derecho
#aqui ponemos las imagenes con los respectivos puntos (dinero) que el usuario va obteniendo
img_puntos = PhotoImage(file = "puntos.png")
img_puntos_1 = PhotoImage(file = "puntos1.png")
img_puntos_2 = PhotoImage(file = "puntos2.png")
img_puntos_3 = PhotoImage(file = "puntos3.png")
img_puntos_4 = PhotoImage(file = "puntos4.png")
img_puntos_5 = PhotoImage(file = "puntos5.png")
img_puntos_6 = PhotoImage(file = "puntos6.png")
img_puntos_7 = PhotoImage(file = "puntos7.png")
img_puntos_8 = PhotoImage(file = "puntos8.png")
img_puntos_9 = PhotoImage(file = "puntos9.png")
img_puntos_10 = PhotoImage(file = "puntos10.png")
img_puntos_11 = PhotoImage(file = "puntos11.png")
img_puntos_12 = PhotoImage(file = "puntos12.png")
img_puntos_13 = PhotoImage(file = "puntos13.png")
img_puntos_14 = PhotoImage(file = "puntos14.png")
img_puntos_15 = PhotoImage(file = "puntos15.png")
img_puntos_16 = PhotoImage(file = "puntos16.png")
img_puntos_17 = PhotoImage(file = "puntos17.png")
img_puntos_18 = PhotoImage(file = "puntos18.png")
img_puntos_19 = PhotoImage(file = "puntos19.png")
img_puntos_20 = PhotoImage(file = "puntos20.png")
img_puntos_21 = PhotoImage(file = "puntos21.png")
img_puntos_22 = PhotoImage(file = "puntos22.png")
img_puntos_23 = PhotoImage(file = "puntos23.png")
img_puntos_24 = PhotoImage(file = "puntos24.png")
img_puntos_25 = PhotoImage(file = "puntos25.png")
img_puntos_26 = PhotoImage(file = "puntos26.png")
img_puntos_27 = PhotoImage(file = "puntos27.png")
img_puntos_28 = PhotoImage(file = "puntos28.png")
img_puntos_29 = PhotoImage(file = "puntos29.png")
img_puntos_30 = PhotoImage(file = "puntos30.png")
img_puntos_31 = PhotoImage(file = "puntos31.png")
img_puntos_32 = PhotoImage(file = "puntos32.png")
img_puntos_33 = PhotoImage(file = "puntos33.png")
img_puntos_34 = PhotoImage(file = "puntos34.png")
img_puntos_35 = PhotoImage(file = "puntos35.png")
img_puntos_36 = PhotoImage(file = "puntos36.png")
img_puntos_37 = PhotoImage(file = "puntos37.png")
img_puntos_38 = PhotoImage(file = "puntos38.png")
img_puntos_39 = PhotoImage(file = "puntos39.png")
img_puntos_40 = PhotoImage(file = "puntos40.png")

#lista con las imagenes de los puntos para que en la funcion seleccionar las recorra 1 por 1
img_pts = [img_puntos_1, img_puntos_2, img_puntos_3, img_puntos_4, img_puntos_5, img_puntos_6, img_puntos_7, img_puntos_8, img_puntos_9, img_puntos_10, img_puntos_11, img_puntos_12, img_puntos_13, img_puntos_14, img_puntos_15, img_puntos_16, img_puntos_17, img_puntos_18, img_puntos_19, img_puntos_20, img_puntos_21, img_puntos_22, img_puntos_23, img_puntos_24, img_puntos_25, img_puntos_26, img_puntos_27, img_puntos_28, img_puntos_29, img_puntos_30, img_puntos_31, img_puntos_32, img_puntos_33, img_puntos_34, img_puntos_35, img_puntos_36, img_puntos_37, img_puntos_38, img_puntos_39, img_puntos_40]

puntos = Label(marco_derecho, image = img_puntos, background = '#5271ff')
puntos.grid(row = 0, column = 0)

#aqui colocamos una imagen donde van las respuesta junto con la pregunta
img_preg_resp = PhotoImage(file = "preguntas.png")
preg_resp = Label(marco_inferior, image = img_preg_resp, background = '#5271ff')
preg_resp.grid(row = 0, column = 0)

total_preguntas = ["¿Quién es el autor de la frase 'Pienso, luego existo'?", 
                   "¿Cuántos decimales tiene el número pi π?", 
                   "La sal común está formada por dos elementos ¿cuáles son?", 
                   "¿Quién pintó la obra 'Guernica'?", 
                   "¿Cuánto tiempo tarda la luz del Sol en llegar a la Tierra?", 
                   "¿Cuáles son los representantes más destacados de la literatura renacentista?", 
                   "¿En qué orden se presentaron los modelos atómicos?", 
                   "¿Cuál es la velocidad de la luz?", 
                   "¿Cuál de estos países se extiende entre dos continentes?", 
                   "¿Cuál fue el recurso utilizado inicialmente por el ser humano para explicar el origen de las cosas?", 
                   "¿Como se llaman los animales que nacen por huevos?",  
                   "¿En qué ciudad se han celebrado los primeros juegos olímpicos?", 
                   "¿Como se llama la escritura utilizada por personas ciegas?", "¿Como se llama la ciencia que estudia los mapas?",  
                   "¿Como se llama el sonido que hace la oveja?", 
                   "¿Cuál es la capital de Marruecos ?", 
                   "¿Cuantos huesos tiene un cuerpo humano adulto?", 
                   "¿A que cadena montañosa pertenece el pico Aneto?", 
                   "¿En qué año se fundó la dinastía Qing?", 
                   "¿Cual sistema fue posterior a la monarquía durante la Edad Media?", 
                   "¿En qué lugar si se realiza la fórmula 1?", 
                   "¿Cuál de los siguientes no es un término usado en física?", 
                   "¿Que significan las siglas NASA?", 
                   "¿Cual no es un integrante de la mesa redonda?", 
                   "¿Cuál de estos no es un instrumento?", 
                   "¿Que es el acronal?", 
                   "¿Cuál de estos no es el nombre de un avión?", 
                   "¿Que significa la frase en ingles 'I can't help it'?", 
                   "¿Cuáles son las siglas de HDMI?", 
                   "¿África, América, Antártida, Asia, Europa, y Oceanía son?",  
                   "¿La capital de Brasil es?", 
                   "¿Qué aparato es un medio de comunicación?", 
                   "¿La capital de México es?", 
                   "¿Cuántos planetas hay en el sistema solar?", 
                   "En el mesencéfalo se ubican:", 
                   "¿Quién pintó Las meninas?", 
                   "¿Cuál es la capital de Hungría?", 
                   "¿qué deporte no es de contacto?",
                   "¿Cuál es el país territorialmente más pequeño?",
                   "¿Qué órgano del cuerpo consume más energía?"]

respuestas_correctas = ["Descartes", "Infinitos", "Sodio y Cloro", "Pablo Picasso", "8 minutos", 
                        "Miguel de Cervantes,\nWilliam Shakespeare,\nLuis de Camões", 
                        "Dalton, Thomson,\nRutherford, cuántico", "299 792 458\nmetros por segundo", 
                        "Rusia", "La mitología", "Ovíparos", "Atenas", "Braille", "Cartografía", 
                        "Balar", "Rabat", "206", "Los Pirineos", "1644", "Feudalismo", "San Marino", 
                        "Tono de Shepard", "National Aeronautics\nand Space Administration", 
                        "Sir Siegfried", "Bandura Ucraniana", "Un producto\npara sellar", "Helldrider", 
                        "No puedo evitarlo", "High Definition\nMultimedia Interface", "Continentes",  
                        "Brasilia", "El teléfono", "Ciudad de México", "8", 
                        "Colículos superiores\ne inferiores", "Francisco de Goya", "Viena", "Ajedrez",
                        "El vaticano", "El cerebro"]

opciones_a = ["Platón", "Dos", "Sodio y Cloro", "Pablo Picasso", "12 minutos", 
              "Leonardo da Vinci,\nMiguel Angel Buonarroti,\nSandro Boticelli", 
              "Thomson, Dalton,\nRutherford, Bohr", "300 000 000\nmetros por segundo", 
              "Rusia", "La filosofía", "Mamíferos", "Tokio", "Braille", "Geomorfología",  
              "Mugir", "Rabat", "206", "El Kilimanjaro", "1640", "Feudalismo", "Ucrania", 
              "Experimento de la\nDoble rendija", "National Administration\nof Spaceships Aerodynamics", 
              "Sir Bedivere", "Hurdy Gurdy", "Un desengrasate a\nbase de Alcohol", "Helldrider", 
              "No puedo ayudarlo", "High Definition\nMultimedia Interface", "Estados/provincias",  
              "Copacabana", "Una grabadora", "El cabo", "7", "Colículos superiores\ne inferiores", 
              "Diego Velázquez", "Praga", "Futbol", "Bermuda", "El cerebro"]
opciones_b = ["Galileo Galilei", "Millones", "Sodio y Potasio", "Diego Rivera", "1 día", 
              "Caravaggio,\nBernini,\nBorromini", "Dalton, Thomson,\nRutherford, cuántico", 
              "150 000 000\nmetros por segundo", "Groenlandia", "La astronomía", "Ovovivíparos", 
              "Atenas", "Cirílico", "Geografía", "Balar", "Casablanca", "203", "Los Alpes", 
              "1646", "Capitalismo", "Ghana", "Tono de Shepard", 
              "National Advances\nSector of America", "Sir Lamorak", "Bandura Ucraniana", 
              "Un compuesto para\naumentar octanaje", "Corsair", "No puedo evitarlo", 
              "High Data Media\nInterface", "Países", "Maracaibo", "Una estufa", 
              "Dublín", "8", "Las pirámides\nbulbares", "Francisco de Goya", "Estanbul", 
              "Ajedrez", "Andorra", "El corazon"]
opciones_c = ["Descartes", "Mil", "Cristal y Sodio", "Salvador Dalí", "12 horas", 
              "Goethe, Victor Hugo,\nGustavo Adolfo Bécquer", 
              "Bohr, Rutherford,\ncuántico, Einstein", "299 792 458\nmetros por segundo", 
              "Egipto", "La mitología", "Vivíparos", "Toronto", "Braile", "Cartografía",  
              "Maullar", "Marrakech", "210", "Los Pirineos", "1648", "Comunismo", 
              "San Marino", "Gato de Schrödinger", "National Aeronautics\nand Space Administration", 
              "Sir Bors", "Didyirido", "Un producto\npara sellar", "Osprey", "No puedo controlarlo", 
              "High Definition\nMedia Interface", "Municipios", "Sao paulo", "El teléfono", 
              "Zúrich", "12", "Deriva de la\nvesícula terciaria", "Salvador Dalí", 
              "Budapest", "Volleybal", "San Marino", "El pancreas"]
opciones_d = ["Sócrates", "Infinitos", "Potasio y Cloro", "Frida Kahlo", "8 minutos", 
              "Miguel de Cervantes,\nWilliam Shakespeare,\nLuis de Camões", 
              "Dalton, Einstein,\ncuántico, Sheldon Cooper", "350 000 000\nmetros por segundo", 
              "Filipinas", "La matemática", "Ovíparos", "Paris", "Morse", "Topografía", 
              "Ladrar", "Agadir", "207", "El Monte Everest", "1644", "Anarquía", "Colombia", 
              "Entropía", "National Aerodynamics\nof Space Advance", "Sir Siegfried", 
              "Arpa de boca",  "Un pegamento de\nsuperficies metalicas", "Warthog", 
              "No puedo ayurle", "High Distance\nMedia Interface", "Continentes", 
              "Brasilia", "Un reloj", "Ciudad de México", "9", "El cuarto ventrículo", 
              "Pablo Picaso", "Viena", "Ultimate", "El vaticano", "El estomago"]

#aqui es donde se ve la pregunta en la ventana principal 
marco_preguntas = Text(marco_inferior, font = ('times new roman', 14, 'bold'), width = 40, height = 2, wrap = 'word', background = '#5271ff', foreground = '#ffc172', border = 0)
marco_preguntas.place(x = 70, y = 10)
marco_preguntas.insert(END, total_preguntas[0])

#aqui se ve el cuadro de la opcion A junto con el boton
opcion_a = Label(marco_inferior, text = "A: ", background = '#5271ff', foreground = '#ffc172', font = ('times new roman', 16, 'bold'))
opcion_a.place(x = 60, y = 110)
opcion_a_boton = Button(marco_inferior, text = opciones_a[0], font = ('times new roman', 14, 'bold'), background = '#5271ff', foreground = '#ffc172', border = 0, activebackground = '#5271ff', activeforeground =  '#ffc172', cursor = 'hand2')
opcion_a_boton.place(x = 100, y = 100)

#aqui se ve el cuadro de la opcion B junto con el boton
opcion_b = Label(marco_inferior, text = "B: ", background = '#5271ff', foreground = '#ffc172', font = ('times new roman', 16, 'bold'))
opcion_b.place(x = 330, y = 110)
opcion_b_boton = Button(marco_inferior, text = opciones_b[0], font = ('times new roman', 14, 'bold'), background = '#5271ff', foreground = '#ffc172', border = 0, activebackground = '#5271ff', activeforeground =  '#ffc172', cursor = 'hand2')
opcion_b_boton.place(x = 370, y = 100)

#aqui se ve el cuadro de la opcion C junto con el boton
opcion_c = Label(marco_inferior, text = "C: ", background = '#5271ff', foreground = '#ffc172', font = ('times new roman', 16, 'bold'))
opcion_c.place(x = 60, y = 190)
opcion_c_boton = Button(marco_inferior, text = opciones_c[0], font = ('times new roman', 14, 'bold'), background = '#5271ff', foreground = '#ffc172', border = 0, activebackground = '#5271ff', activeforeground =  '#ffc172', cursor = 'hand2')
opcion_c_boton.place(x = 100, y = 180)

#aqui se ve el cuadro de la opcion D junto con el boton
opcion_d = Label(marco_inferior, text = "D: ", background = '#5271ff', foreground = '#ffc172', font = ('times new roman', 16, 'bold'))
opcion_d.place(x = 330, y = 190)
opcion_d_boton = Button(marco_inferior, text = opciones_d[0], font = ('times new roman', 14, 'bold'), background = '#5271ff', foreground = '#ffc172', border = 0, activebackground = '#5271ff', activeforeground =  '#ffc172', cursor = 'hand2')
opcion_d_boton.place(x = 370, y = 180)

#Con el método bind asigna una dirección, en este casi el voton, y un número de puerto,que seria seleccionar, para que el respectivo boton haga lo que se coloco en la funcion seleccionar
opcion_a_boton.bind('<Button-1>', seleccionar)
opcion_b_boton.bind('<Button-1>', seleccionar)
opcion_c_boton.bind('<Button-1>', seleccionar)
opcion_d_boton.bind('<Button-1>', seleccionar)

ventana.mainloop() #cerramos la ventana del juego