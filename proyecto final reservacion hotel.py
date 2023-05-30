from tkinter import *
from tkinter import ttk

numeros=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,4,5,6,7,8,9]

for i in numeros:
    class Hotel():
            def __init__(self, ventana):
                self.ventana = ventana
                self.ventana.title("Proyecto final Jiménez Ramos Jonathan Fernando")
                self.ventana.geometry("700x700")
                self.habitaciones = {"sencilla": 974,"doble": 1635, "VIP": 2296, "golden": 2957}
                self.create_widgets()

            def create_widgets(self):
                self.titulo = Label(
                    self.ventana, text="Datos del usuario:", font="console")
                self.titulo.grid(row=0, column=0)

                self.lblnom = Label(self.ventana, text="Nombre: ")
                self.lblnom.grid(row=1, column=0)

                self.lblnum = Label(self.ventana, text="Número de telefono:")
                self.lblnum.grid(row=2, column=0)

                self.lblpers = Label(self.ventana, text="Número de personas:")
                self.lblpers.grid(row=3, column=0)

                self.lblhab = Label(
                    self.ventana, text="¿Qué tipo de habitación quieres?:")
                self.lblhab.grid(row=4, column=0)

                self.lbldias = Label(
                    self.ventana, text="Días que durará su estancia:")
                self.lbldias.grid(row=5, column=0)

                self.entnom = Entry(self.ventana)
                self.entnom.grid(row=1, column=1)

                self.entnum = Entry(self.ventana)
                self.entnum.grid(row=2, column=1)

                self.entpers = Entry(self.ventana)
                self.entpers.grid(row=3, column=1)

                self.enthab = ttk.Combobox(self.ventana)
                self.enthab.grid(row=4, column=1)
                self.enthab['values'] = list(self.habitaciones.keys())
                self.enthab.current(0)

                self.entdia = Entry(self.ventana)
                self.entdia.grid(row=5, column=1)

                self.btntotales = Button(
                    self.ventana, text="imprimir ticket", command=self.imprimir_ticket)
                self.btntotales.grid(row=6, column=0)

                self.btnleer = Button(
                    self.ventana, text="leer archivo", command=self.read_file)
                self.btnleer.grid(row=6, column=1)

                self.lbltotalprice = Label(self.ventana, text="")
                self.lbltotalprice.grid(row=7, column=1, columnspan=2)

                self.preciostext = Label(ventana, text="precios p/noche", font=25)
                self.preciostext.grid(row=0, column=3)

                self.precios = Label(
                    self.ventana, text="Sencilla=   974$mx\nDoble=  1635$mx\nVIP=    2296$mx\nGolden= 2957$mx", bg="dark green", fg="white")
                self.precios.grid(row=1, column=3)

                self.lblread = Label(self.ventana, text="")
                self.lblread.grid(row=8, column=0, columnspan=2)

                self.enthab['values'] = list(self.habitaciones.keys())
                self.enthab.current(0)

                self.entdia = Entry(self.ventana)
                self.entdia.grid(row=5, column=1)

                self.btntotales = Button(
                    self.ventana, text="imprimir ticket", command=self.imprimir_ticket)
                self.btntotales.grid(row=6, column=0)

                self.btnleer = Button(
                    self.ventana, text="leer archivo", command=self.read_file)
                self.btnleer.grid(row=6, column=1)

                self.lbltotalprice = Label(self.ventana, text="")
                self.lbltotalprice.grid(row=7, column=0, columnspan=2)

                self.lblread = Label(self.ventana, text="")
                self.lblread.grid(row=8, column=1, columnspan=2)

                self.btnsalir = Button(self.ventana, text="salir", command=ventana.destroy)
                self.btnsalir.grid(row=7, column=2)


            def read_file(self):
                try:
                    with open("proyfinal.txt", "r") as file:
                        content = file.read()
                        self.lblread.config(text=content)
                except:
                    self.lblread.config(text="Error al leer el archivo")

            def imprimir_ticket(self):
                try:
                    nombre = self.entnom.get()
                    numero = self.entnum.get()
                    personas = self.entpers.get()
                    habitacion_string = self.enthab.get()
                    habitacion_num = self.habitaciones[habitacion_string]
                    dias = self.entdia.get()
                except:
                    self.lbltotalprice.config(
                        text="La habitación seleccionada no existe en el diccionario", bg="red", font="console")
                try:
                    totalnoiva = int(dias) * habitacion_num
                    totalconiva = int(totalnoiva+(totalnoiva*.16))
                    if totalconiva<1:
                        lblhi=Label(ventana, text="no puede continuar")
                        lblhi.grid(row=9,column=1)
                    elif totalconiva>1:
                        lblhi=Label(ventana, Text="puede seguir con el codigo")
                        lblhi.grid(row=9,column=1)
                    self.lbltotalprice.config(text="Nombre: {}\nNumero de telefono: {}\nNumero de personas: {}\nTipo de habitacion: {}\nDias: {}\nTotal sin IVA: ${}\nTotal con IVA: ${}".format(
                        nombre, numero, personas, habitacion_string, dias, totalnoiva, totalconiva), bg="blue")
                    with open("proyfinal.txt", "a") as file:
                        file.write("\nNombre: {}\nNumero de telefono: {}\nNumero de personas: {}\nTipo de habitacion: {}\nDias: {}\nTotal sin IVA: ${}\nTotal con IVA: ${}".format(nombre, numero, personas, habitacion_string, dias, totalnoiva, totalconiva))

                except ValueError:
                    self.lbltotalprice.config(
                        text="Por favor, llene todos los campos", bg="red", font="console")
        
    class total(Hotel):
            def __init__(self):
                super().__init__()


    ventana = Tk()
    mi_hotel = Hotel(ventana)
    ventana.mainloop()

    break