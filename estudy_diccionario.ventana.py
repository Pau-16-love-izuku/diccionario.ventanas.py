import tkinter as tk
estudiantes = {}
contador = 1
def guardar_estudiante():
    global contador
    nombre = entry_nombre.get()
    calificacion = entry_calificacion.get()
    sexo = entry_sexo.get()

    if nombre and calificacion and sexo:
        try:
            calificacion = float(calificacion)
        except ValueError:
            resultado.insert(tk.END, "Calificación inválida. Usa un número.")
            return

        clave = f"est{contador}"
        estudiantes[clave] = {
            "nombre": nombre,
            "calificacion": calificacion,
            "sexo": sexo
        }

        entry_nombre.delete(0, tk.END)
        entry_calificacion.delete(0, tk.END)
        entry_sexo.delete(0, tk.END)

        contador += 1

        if contador > 3:
            boton_guardar.config(state=tk.DISABLED)
            resultado.insert(tk.END, "Ya ingresaste 3 estudiantes. Presiona 'Mostrar Estudiantes'.")

def mostrar_estudiantes():
    resultado.delete(0, tk.END)
    for i, est in enumerate(estudiantes.values(), start=1):
        texto = f"{i}. Nombre: {est['nombre']}, Calificación: {est['calificacion']}, Sexo: {est['sexo']}"
        resultado.insert(tk.END, texto)

ventana = tk.Tk()
ventana.title("Ingreso de Estudiantes")
ventana.geometry("400x400")

tk.Label(ventana, text="Nombre:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Calificación:").pack()
entry_calificacion = tk.Entry(ventana)
entry_calificacion.pack()

tk.Label(ventana, text="Sexo (M/F):").pack()
entry_sexo = tk.Entry(ventana)
entry_sexo.pack()

boton_guardar = tk.Button(ventana, text="Guardar Estudiante", command=guardar_estudiante)
boton_guardar.pack(pady=5)

tk.Button(ventana, text="Mostrar Estudiantes", command=mostrar_estudiantes).pack(pady=5)

resultado = tk.Listbox(ventana, width=50)
resultado.pack(pady=10)

ventana.mainloop()