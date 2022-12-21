from tkinter import *
import math

"""o objetivo final do código é criar um cronômetro no método POMODORO que calcula 25 minutos de 
atividade e cinco minutos de descanso e na oitava vez, calcula 20 minutos de intervalo"""
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = NONE


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_lable.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
"""essa função serve para resetar o relógio, a função after cancel é uma função interna (built in) e é passado a
 varíavel timer, ou seja, a função cancela o timer, mas também foi preciso configurar tudo o que precisa voltar ao estado
   inicial"""
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        count_down(long_break_sec)
        title_lable.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_lable.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        title_lable.config(text="WORK", fg=GREEN)



""" What is a global variable? A global variable is a variable that is declared outside the function
 but we need to use it inside the function."""
"""função para iniciar a contagem quando o botão start é pressionado, só é passada a outra função e adicionada
a função no código do botão, a função também determina o tempo de trabalho e repouso, multiplicando por 60
as variáveis constantes acima declaradas, também é mudado o título de acordo com o momento. Reparar como é mais fácil
ter colocado esse código de mudança de status nessa parte do código"""
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks =""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
            check_marks.config(text=marks)


"""o código acima serve para criar os minutos e segundos, primeiro ele usa o math floor que pega o número float e 
arrendonda para o número inteiro, por exemplo, 4,60 para 4, depois o segundo usa o resto da divisão do número estabelecido 
no count por 60 para estabelecer os segundos, abaixo é alterado o mostrador para mostrar os dois números. Reparar a lógica
aqui utilizada para se chegar aos minutos e segundos. O else serve para que a função reinicie após o tempor e vá
para os minutos de descanso"""
"""A primeira linha da função count_down serve para que o texto vá sendo substituido pelo número da contagem,
reparar que no canvas a função é passada com uma sintaxe diferente, aqui só foi passado o item e o que se quer
mudar no item
A função after é uma função build in que funciona assim:
 Code language: Python (python) The after () method calls the callback function once
after a delay milliseconds (ms) within Tkinter’s main loop. If you don’t provide the callback,
the after () method behaves like the time.sleep () function. However, the after () method uses
the millisecond instead of the second as the unit. """
"""o primeiro if serve para que quando o segundo esteja em 0, apareça 00, isso só é possivel graças ao Dynamic Data Type
do Python, que é: Dynamic Typing Python is a dynamically typed language. This means that the Python interpreter does
 type checking only as code runs, and the type of a variable is allowed to change over its lifetime.
  Portanto, ele verifica modifica o tipo de string para int enquanto o código roda. Já o for loop serve para acrescentar
  um sinal de check a cada rodada, ou seja, a cada work + break"""
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
"""os códigos acima são para criar a janela e colocar nela o título, já o pad é o espaço entre a tela e a 
imagem, o bg é o background, reparar como o YELLOW é uma constante criada no começo do código com o código 
da cor específica"""
title_lable = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_lable.grid(column=1, row=0)

"""os códigos acima são para o título do código, mudou-se a forma de encaixe das partes para grid"""
canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
"""as linhas acima servem para colocar a imagem baixada como fundo, primeiro é reservado um espaço do tamanho
da imagem, depois é criada a variável da imagem, então é criada a imagem passa a localização x e y, que é 
metade do tamanho da imagem, por fim é chamado o método grid para localizar a imagem. obs. canvas significa
tela. Depois o código create_text cria o cronômetro que vai ficar no meio da imagem, é passada as posições
e os demais dados de preenchimento, como se fosse um documento do WORD"""
count_down(0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
"""dentro dos argumentos de criação do botão, já foi passada a função que fará o sistema começar ao 
ser pressionado o botão"""

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


"""os códigos acima criam os botôes de start e reset, e um check mark, reparar a diferença entre o comando Button e o
 comando Label que apenas cria um símbolo na tela"""

window.mainloop()
"""o window.mainloop serve para manter a janela aberta, ele verifica a todo momento se algo está acontecendo"""