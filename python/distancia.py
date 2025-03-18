import math
import tkinter as tk

def horizontal():
    def calcular_horizontal():   

        distancia = float(nome.get())
        angulo1 = float(nome1.get())
        angulo2 = float(nome2.get())

        angulo1_seno = math.sin(math.radians(angulo1))
        angulo2_seno = math.sin(math.radians(angulo2))

        horizontale = distancia*angulo1_seno/angulo2_seno

        nome3.config(state='normal')
        resultado.set(f'{horizontale:.2f} metros')
        nome3.config(state="readonly")

    nova_janela = tk.Toplevel(aba, bg='white')
    nova_janela.geometry('550x300')

    quad = tk.Frame(nova_janela, bg="#ffffff", padx=80, pady=10)
    quad.pack(padx=20,pady=20)

    tt = tk.Label(quad, text='Lei do seno', font=("Arial", 14, "bold"), bg="white")
    tt.grid(column=0,row=0, columnspan=3)

    texto = tk.Label(quad, text='Distância do objeto:', font=("helvetica", 12), bg="#ffffff")
    texto.grid(row=1, column=0, padx=10, pady=10)

    texto1 = tk.Label(quad, text='Primeiro ângulo:', font=("helvetica", 12), bg="#ffffff")
    texto1.grid(row=2, column=0, padx=10, pady=10)

    texto2 = tk.Label(quad, text='Segundo ângulo:', font=("helvetica", 12), bg="#ffffff")
    texto2.grid(row=3, column=0, padx=10, pady=10)

    texto3 = tk.Label(quad, text='Resultado:', font=("helvetica", 12), bg="#ffffff")
    texto3.grid(row=4, column=0, padx=10, pady=10)

    nome = tk.Entry(quad, font=("helvetica", 12), width=10)
    nome.grid(row=1, column=1, padx=10, pady=10)

    nome1 = tk.Entry(quad, font=("helvetica", 12), width=10)
    nome1.grid(row=2,column=1, padx=10, pady=10)

    nome2 = tk.Entry(quad, font=("helvetica", 12), width=10)
    nome2.grid(row=3, column=1, padx=10, pady=10)

    resultado = tk.StringVar()

    resu = tk.Button(quad,text = 'Calcular', bg='lightblue', width=8, font=("Arial", 10),command=calcular_horizontal)
    resu.grid(row=4, column=2, padx=10, pady=10)


    nome3 = tk.Entry(quad, font=("helvetica", 12),textvariable=resultado, width=11, justify="center", state="readonly")
    nome3.grid(row=4, column=1, padx=10, pady=10)

    fec = tk.Button(quad,text = 'Fechar', bg='lightblue', width=8,justify="center", font=("Arial", 10),command=nova_janela.destroy)
    fec.grid(row=1, column=2, padx=10, pady=10)

def vertical():
    def calcular_vertical():
        distancia = float(nome.get())
        angulo = float(nome1.get())
        altura_teodolito = float(nome2.get())

        angulo_rad = math.radians(angulo)
        verticale = distancia * math.tan(angulo_rad) + altura_teodolito

        nome3.config(state='normal')
        resultado.set(f'{verticale:.2f} metros')
        nome3.config(state="readonly")

    nova_janela = tk.Toplevel(aba, bg='white')
    nova_janela.geometry('550x300')

    quad = tk.Frame(nova_janela, bg="#ffffff", padx=80, pady=10)
    quad.pack(padx=20,pady=20)

    tt = tk.Label(quad, text='Lei da tangente', font=("Arial", 14, "bold"), bg="white")
    tt.grid(column=0,row=0, columnspan=3)

    texto = tk.Label(quad, text='Distância:', font=("helvetica", 12), bg="#ffffff")
    texto.grid(row=1, column=0, padx=10, pady=10)

    texto1 = tk.Label(quad, text='Altura do medidor:', font=("helvetica", 12), bg="#ffffff")
    texto1.grid(row=2, column=0, padx=10, pady=10)

    texto2 = tk.Label(quad, text='Ângulo:', font=("helvetica", 12), bg="#ffffff")
    texto2.grid(row=3, column=0, padx=10, pady=10)

    texto3 = tk.Label(quad, text='Resultado:', font=("helvetica", 12), bg="#ffffff")
    texto3.grid(row=4, column=0, padx=10, pady=10)

    nome = tk.Entry(quad, font=("helvetica", 12), width=10)
    nome.grid(row=1, column=1, padx=10, pady=10)

    nome1 = tk.Entry(quad, font=("helvetica", 12), width=10)
    nome1.grid(row=2,column=1, padx=10, pady=10)

    nome2 = tk.Entry(quad, font=("helvetica", 12), width=10)
    nome2.grid(row=3, column=1, padx=10, pady=10)

    resultado = tk.StringVar()

    resu = tk.Button(quad,text = 'Calcular', bg='lightblue', width=8, font=("Arial", 10),command=calcular_vertical)
    resu.grid(row=4, column=2, padx=10, pady=10)

    nome3 = tk.Entry(quad, font=("helvetica", 12),textvariable=resultado, width=11, justify="center", state="readonly")
    nome3.grid(row=4, column=1, padx=10, pady=10)

    fec = tk.Button(quad,text = 'Fechar', bg='lightblue', width=8,justify="center", font=("Arial", 10),command=nova_janela.destroy)
    fec.grid(row=1, column=2, padx=10, pady=10)

def cosseno():
    def calcular_cosseno():
        lado1 = float(nome.get())
        lado2 = float(nome1.get())
        angulo = float(nome2.get())

        angulo_radiano = math.radians(angulo)

        lado3 = math.sqrt(lado1**2+lado2**2 - 2 * lado1 * lado2 * math.cos(angulo_radiano))

        nome3.config(state='normal')
        resultado.set(f'{lado3:.2f} metros')
        nome3.config(state="readonly")

    nova_janela = tk.Toplevel(aba, bg='white')
    nova_janela.geometry('550x300')

    quad = tk.Frame(nova_janela, bg="#ffffff", padx=80, pady=10)
    quad.pack(padx=20,pady=20)

    tt = tk.Label(quad, text='Lei do cosseno', font=("Arial", 14, "bold"), bg="white")
    tt.grid(column=0,row=0, columnspan=3)

    texto = tk.Label(quad, text='Primeiro lado:', font=("helvetica", 12), bg="#ffffff")
    texto.grid(row=1, column=0, padx=10, pady=10)

    texto1 = tk.Label(quad, text='Segundo lado:', font=("helvetica", 12), bg="#ffffff")
    texto1.grid(row=2, column=0, padx=10, pady=10)

    texto2 = tk.Label(quad, text='Ângulo:', font=("helvetica", 12), bg="#ffffff")
    texto2.grid(row=3, column=0, padx=10, pady=10)

    texto3 = tk.Label(quad, text='Resultado:', font=("helvetica", 12), bg="#ffffff")
    texto3.grid(row=4, column=0, padx=10, pady=10)

    nome = tk.Entry(quad, font=("helvetica", 12), width=10)
    nome.grid(row=1, column=1, padx=10, pady=10)

    nome1 = tk.Entry(quad, font=("helvetica", 12), width=10)
    nome1.grid(row=2,column=1, padx=10, pady=10)

    nome2 = tk.Entry(quad, font=("helvetica", 12), width=10)
    nome2.grid(row=3, column=1, padx=10, pady=10)

    resultado = tk.StringVar()

    resu = tk.Button(quad,text = 'Calcular', bg='lightblue', width=8, font=("Arial", 10),command=calcular_cosseno)
    resu.grid(row=4, column=2, padx=10, pady=10)

    nome3 = tk.Entry(quad, font=("helvetica", 12),textvariable=resultado, width=11, justify="center", state="readonly")
    nome3.grid(row=4, column=1, padx=10, pady=10)

    fec = tk.Button(quad,text = 'Fechar', bg='lightblue', width=8,justify="center", font=("Arial", 10),command=nova_janela.destroy)
    fec.grid(row=1, column=2, padx=10, pady=10)


aba = tk.Tk()
aba.title("Calculadora")
aba.geometry("620x300")

quadrado = tk.Frame(aba, bg="#ffffff", padx=80, pady=10)
quadrado.pack(padx=20,pady=20)

t = tk.Label(quadrado,text='Calculadora de distâncias inacessiveis', font=("Arial", 14, "bold"), bg="white")
t.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

h = tk.Button(quadrado,text = 'Calcular distância horizontal\nLei do seno', width=25,height=4, bg="lightblue",font=("Arial", 10),command=horizontal)
h.grid(row=1,column=0,padx=10, pady=10)
v = tk.Button(quadrado,text = 'Calcular distância vertical\nLei da tangente', width=25,height=4, bg='lightblue',font=("Arial", 10),command=vertical)
v.grid(row=2,column=0,padx=10, pady=10)
v = tk.Button(quadrado,text = 'Lei do cosseno', width=25,height=4, bg='lightblue',font=("Arial", 10),command=cosseno)
v.grid(row=1,column=1,padx=10, pady=10)

f = tk.Button(quadrado,text = 'Fechar', width=25,height=4, bg='red',font=("Arial", 10),command=aba.destroy)
f.grid(row=2,column=1,padx=10, pady=10)


aba.mainloop()