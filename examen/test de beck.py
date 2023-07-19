#test de beck parte 6
def on_mousewheel(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

def show_next_question():
    global current_question_index
    if current_question_index < len(questions) - 1:
        current_question_index += 1
        show_question()

def show_question():
    question_data = questions[current_question_index]
    question_label.config(text=question_data["question"])
    for i, option_radio in enumerate(option_radios):
        option_radio.config(text=question_data["options"][i], variable=answer_vars[current_question_index], value=i)

    if current_question_index == len(questions) - 1:
        next_button.config(text="Enviar respuestas", command=submit_answers)

def submit_answers():
    total_score = 0
    for answer_var in answer_vars:
        total_score += answer_var.get()
    result_label.config(text=f"Resultado: {total_score}")

root = tk.Tk()
root.title("test de beck :D")

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.config(yscrollcommand=scrollbar.set)
canvas.bind("<MouseWheel>", on_mousewheel)

frame = tk.Frame(canvas, bg="white")
canvas.create_window((0, 0), window=frame, anchor="nw")

questions = [
  {
        "question": "1. Tristeza",
        "options": ["0 No me siento triste.", 
                    "1 Me siento triste gran parte del tiempo",
                    "2 Me siento triste todo el tiempo.", 
                    "3 Me siento tan triste o soy tan infeliz que no puedo soportarlo."],
    },
    {
        "question": "2. Pesimismo",
        "options": ["0 No estoy desalentado respecto de mi futuro.",
                     "1 Me siento más desalentado respecto de mi futuro que lo que solía estarlo.", 
                     "2 No espero que las cosas funcionen para mí.", 
                     "3 Siento que no hay esperanza para mi futuro y que sólo puede empeorar."],
    },
     {
        "question": "3. Fracaso",
        "options": [ "0 No me siento como un fracasado.",
                     "1 He fracasado más de lo que hubiera debido.", 
                     "2 Cuando miro hacia atrás, veo muchos fracasos", 
                     "3 Siento que como persona soy un fracaso total."],
    },
     {
        "question": "4. Pérdida de Placer",
        "options": [ "0 Obtengo tanto placer como siempre por las cosas de las que disfruto.",
                     "1 No disfruto tanto de las cosas como solía hacerlo", 
                     "2 Obtengo muy poco placer de las cosas que solía disfrutar.", 
                     "3 No puedo obtener ningún placer de las cosas de las que solía disfrutar."],
    },
     {
        "question": "5. Sentimientos de Culpa",
       "options":  [ "0 No me siento particularmente culpable.",
                     "1 Me siento culpable respecto de varias cosas que he hecho o que debería haber hecho.", 
                     "2 Me siento bastante culpable la mayor parte del tiempo.", 
                     "3 Me siento culpable todo el tiempo."],
    },
     {
        "question": "6. Sentimientos de Castigo",
        "options": [ "0 No siento que este siendo castigado",
                     "1 Siento que tal vez pueda ser castigado.", 
                     "2 Espero ser castigado.", 
                     "3 Siento que estoy siendo castigado."],
    },
    
     {
        "question": "7. Disconformidad con uno mismo.",
        "options":  ["0 Siento acerca de mi lo mismo que siempre.",
                     "1 He perdido la confianza en mí mismo.", 
                     "2 Estoy decepcionado conmigo mismo.", 
                     "3 No me gusto a mí mismo."],
    },
     {
        "question": "8. Autocrítica",
       "options": [  "0 No me critico ni me culpo más de lo habitual",
                     "1 Estoy más crítico conmigo mismo de lo que solía estarlo", 
                     "2 Me critico a mí mismo por todos mis errores", 
                     "3 Me culpo a mí mismo por todo lo malo que sucede."],
    },
     {
        "question": "9. Pensamientos o Deseos Suicidas",
        "options": [ "0 No tengo ningún pensamiento de matarme.",
                     "1 He tenido pensamientos de matarme, pero no lo haría", 
                     "2 Querría matarme", 
                     "3 Me mataría si tuviera la oportunidad de hacerlo."],
    },
     {
        "question": "10. Llanto",
        "options": [ "0 No lloro más de lo que solía hacerlo.",
                     "1 Lloro más de lo que solía hacerlo", 
                     "2 Lloro por cualquier pequeñez.", 
                     "3 Siento ganas de llorar pero no puedo."],
    },
     {
        "question": "11 Agitación",
        "options": [ "0 No estoy más inquieto o tenso que lo habitual.",
                     "1 Me siento más inquieto o tenso que lo habitual.", 
                     "2 Estoy tan inquieto o agitado que me es difícil quedarme quieto", 
                     "3 Estoy tan inquieto o agitado que tengo que estar siempre en movimiento o haciendo algo."],
    },
     {
        "question": "12 Pérdida de Interés",
       "options": [  "0 No he perdido el interés en otras actividades o personas.",
                     "1 Estoy menos interesado que antes en otras personas o cosas.", 
                     "2 He perdido casi todo el interés en otras personas o cosas.", 
                     "3 Estoy tan inquieto o agitado que tengo que estar siempre en movimiento o haciendo algo"],
    },
     {
        "question": "13. Indecisión",
       "options": [  "0 Tomo mis propias decisiones tan bien como siempre.",
                     "1 Me resulta más difícil que de costumbre tomar decisiones", 
                     "2 Encuentro mucha más dificultad que antes para tomar decisiones.", 
                     "3 Tengo problemas para tomar cualquier decisión."],
    },
     {
        "question": "14. Desvalorización",
        "options": [ "0 No siento que yo no sea valioso",
                     "1 No me considero a mi mismo tan valioso y útil como solía considerarme", 
                     "2 Me siento menos valioso cuando me comparo con otros.", 
                     "3 Siento que no valgo nada."],
    },
     {
        "question": "15. Pérdida de Energía",
        "options": [ "0 Tengo tanta energía como siempre.",
                     "1. Tengo menos energía que la que solía tener.", 
                     "2. No tengo suficiente energía para hacer demasiado", 
                     "3. No tengo energía suficiente para hacer nada."],
    },
     {
        "question": "16. Cambios en los Hábitos de Sueño",
        "options": [ "0. No he experimentado ningún cambio en mis hábitos de sueño.",
                     "1. Duermo un poco menos que lo habitual.", 
                     "2. Duermo la mayor parte del día", 
                     "3. Me despierto 1-2 horas más temprano y no puedo volver a dormirme"],
    },
     {
        "question": "17. Irritabilidad",
       "options": [  "0. No estoy tan irritable que lo habitual.",
                     "1. Estoy más irritable que lo habitual.", 
                     "2. Estoy mucho más irritable que lo habitual.", 
                     "3. Estoy irritable todo el tiempo."],
    },
     {
        "question": "18. Cambios en el Apetito",
        "options": [ "0. No he experimentado ningún cambio en mi apetito.",
                     "1. Mi apetito es un poco menor que lo habitual.", 
                     "2. Mi apetito es mucho menor que antes", 
                     "3. No tengo apetito en absoluto"],
    },
    {
        "question": "19. Dificultad de Concentración",
        "options": [ "0. Puedo concentrarme tan bien como siempre.",
                     "1. No puedo concentrarme tan bien como habitualmente", 
                     "2. Me es difícil mantener la mente en algo por mucho tiempo.", 
                     "3. Encuentro que no puedo concentrarme en nada."],
    },
    {
        "question": "20. Cansancio o Fatiga",
        "options": [ "0. No estoy más cansado o fatigado que lo habitual.",
                     "1. Me fatigo o me canso más fácilmente que lo habitual.", 
                     "2. Estoy demasiado fatigado o cansado para hacer muchas de las cosas que solía hacer.", 
                     "3. Estoy demasiado fatigado o cansado para hacer la mayoría de las cosas que solía hacer."],
    },
    {
        "question": "21. Pérdida de Interés en el Sexo",
        "options": [ "0. No he notado ningún cambio reciente en mi interés por el sexo.",
                     "1. Estoy menos interesado en el sexo de lo que solía estarlo.", 
                     "2. Estoy mucho menos interesado en el sexo.", 
                     "3. He perdido completamente el interés en el sexo."],
    }
]

current_question_index = 0
answer_vars = [tk.IntVar() for _ in questions]
option_radios = []

question_label = tk.Label(frame, text="", bg="white")
question_label.grid(row=0, column=0, sticky="w")

for i in range(len(questions[0]["options"])):
    option_radio = tk.Radiobutton(frame, text="", variable=answer_vars[current_question_index], value=i, bg="white")
    option_radio.grid(row=i+1, column=0, sticky="w")
    option_radios.append(option_radio)

next_button = tk.Button(frame, text="Siguiente", command=show_next_question)
next_button.grid(row=len(questions[0]["options"])+1, column=0, pady=10)

result_label = tk.Label(frame, text="Resultado: ", bg="white")
result_label.grid(row=len(questions[0]["options"])+2, column=0)

frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

show_question()
root.mainloop()
#resultados para la desmostracion de hoy


def obtener_nivel_depresion(puntaje):
    if puntaje >= 0 and puntaje <= 13:
        return "Mínima depresión; sal a pasear un rato ;D"
    elif puntaje >= 14 and puntaje <= 19:
        return "Depresión leve; todo saldra bien te lo prometo"
    elif puntaje >= 20 and puntaje <= 28:
        return "Depresión moderada; habla con alguien de confianza :c"
    elif puntaje >= 29 and puntaje <= 63:
        return "Depresión grave, busca ayuda profesional por favor..."
    else:
        return "Oye eso niquiera es un numero >:v"

def mostrar_resultado():
    puntaje = int(entry_puntaje.get())
    resultado = obtener_nivel_depresion(puntaje)
    label_resultado.config(text=resultado)

# para una ventana
ventana = tk.Tk()
ventana.title("Niveles de depresión")

# mostrando resultados del test
label_puntaje = tk.Label(ventana, text="Ingrese el puntaje:")
label_puntaje.pack()

entry_puntaje = tk.Entry(ventana)
entry_puntaje.pack()

# boton enter para mostrar
btn_mostrar = tk.Button(ventana, text="Mostrar nivel de depresión", command=mostrar_resultado)
btn_mostrar.pack()

# etiqueta para mostrar el resultado xd
label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

# el bucle de la interfaz gráfica xd
ventana.mainloop()
