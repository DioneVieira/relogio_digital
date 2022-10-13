***RELÓGIO DIGITAL PYTHON***<hr>

Utilizaremos o Tkinter para a GUI.

Vamos começar criando uma janela vazia no tkinter.
 
```ruby
from tkinter import *
import tkinter

#### Cores ####
cor1 = "#000000" # preta
cor2 = "#fafcff" # branca
cor3 = "#21c25c" # verde
cor4 = "#eb463b" # vermelho
cor5 = "#dedcdc" # cinza
cor6 = "#3080f0" # azul
cor7 = "#00FF00" # verde limão


fundo = cor1
cor = cor7

janela = Tk()
janela.title("Meu Relógio Python")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg = cor1)

janela.mainloop()
```

No código acima, criamos uma janela vazia no Tkinter, e definimos algumas cores que usaremos para nossa aplicação, a variável cor, será a cor da fonte, e a variável fundo será a cor de fundo.
E então importaremos o datetime, o que nos permitirá trabalhar com o horário e calendário.

```ruby
from datetime import datetime
```

Depois disso, obteremos a hora, o dia da semana, o mês e o ano.

```ruby
tempo = datetime.now()

    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b") #B maiusculo para aparecer nome do mes sem abreviação
    ano = tempo.strftime("%Y")

```

Vamos criar uma função e passar todos esses valores para essa função.

```ruby
def relogio():
    tempo = datetime.now()

    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b") #B maiusculo para aparecer nome do mes sem abreviação
    ano = tempo.strftime("%Y")
```

Depois disso vamos criar um label que mostrará a hora.

```ruby
l1 = Label(janela, text="", font=("digital-7 100"), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)
```

Agora vamos passar o valor da hora para o label que acabamos de criar, e executar a função.

```ruby
def relogio():
    tempo = datetime.now()

    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b") #B maiusculo para aparecer nome do mes sem abreviação
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
```

Para manter o tempo dinâmico, usaremos o seguinte l1.after(200, relogio) execute a função relogio():

```ruby
def relogio():
    tempo = datetime.now()

    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b") #B maiusculo para aparecer nome do mes sem abreviação
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)
   

l1 = Label(janela, text="", font=("digital-7 100"), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)

#executando
relogio()
```

Agora que o relógio já está funcionando, passaremos também os valores restantes, criando um novo label.

```ruby
l2 = Label(janela, text="", font=("digital-7 18"), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)
````
E dentro da função de relógio iremos configurar da seguinte forma:



As funcionalidades do relógio já estão prontas, agora vamos estilizar nosso relógio para que pareça mais digital.
Primeiro vamos baixar a fonte aqui neste site. 

```ruby
l2.config(text=dia_semana + ", " + str(dia) + "/" + str(mes) + "/" + str(ano))
```

**font https://www.1001fonts.com/digital-7-font.html**<br/>
Depois de baixar e extrair as fontes, e coloca no mesmo diretório em que está o nosso script python, iremos adicionar ao nosso aplicativo, mas para isso teremos que instalar outra biblioteca Python primeiro, que é:

**pip install pyglet**
Após a instalação, escreva o seguinte código para adicionar a fonte que acabamos de baixar.

```ruby
import pyglet("digital-7.ttf")
```

Após importar e vincular a fonte, basta usar a fonte e ela estará ativa.<hr>


****Relógio Digital****

![image](https://user-images.githubusercontent.com/94480509/195674728-0d13d23f-6d46-4719-8a05-6299a3426527.png)





