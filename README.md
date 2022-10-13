***RELÓGIO DIGITAL PYTHON***<hr>

Utilizaremos o Tkinter para a GUI.

Vamos começar criando uma janela vazia no tkinter.
 

![image](https://user-images.githubusercontent.com/94480509/195378839-37593242-b3f0-481c-b30d-91cefb038917.png)

No código acima, criamos uma janela vazia no Tkinter, e definimos algumas cores que usaremos para nossa aplicação, a variável cor, será a cor da fonte, e a variável fundo será a cor de fundo.
E então importaremos o datetime, o que nos permitirá trabalhar com o horário e calendário.

![image](https://user-images.githubusercontent.com/94480509/195379191-e7f60c55-ca23-4b80-aafc-bccf027df634.png)

Depois disso, obteremos a hora, o dia da semana, o mês e o ano.

![image](https://user-images.githubusercontent.com/94480509/195379356-6f6d458c-6855-497e-8bc0-aaed5f3b077f.png)
![image](https://user-images.githubusercontent.com/94480509/195379515-d5a4fbe9-7f2b-46c7-beb7-b7ea5c4e9076.png)

Vamos criar uma função e passar todos esses valores para essa função.

![image](https://user-images.githubusercontent.com/94480509/195673267-368618be-0fb2-4959-adf2-5b105b74155a.png)

Depois disso vamos criar um label que mostrará a hora.

![image](https://user-images.githubusercontent.com/94480509/195673402-961d6b0c-2870-4450-aa9a-20a5d087a945.png)

Agora vamos passar o valor da hora para o label que acabamos de criar, e executar a função.

![image](https://user-images.githubusercontent.com/94480509/195673520-bc62d4fc-d720-4977-b629-4d7b78879244.png)

Para manter o tempo dinâmico, usaremos o seguinte l1.after(200, relogio) execute a função relogio():

![image](https://user-images.githubusercontent.com/94480509/195673700-c439bf70-b4dd-48fc-85df-52a3c6931ae7.png)

Agora que o relógio já está funcionando, passaremos também os valores restantes, criando um novo label.

![image](https://user-images.githubusercontent.com/94480509/195673863-61eecb3e-8341-4188-9f3e-6d150b2a2825.png)

E dentro da função de relógio iremos configurar da seguinte forma:

![image](https://user-images.githubusercontent.com/94480509/195674030-141effd6-9dc9-4fc1-a7ef-86369c6bf25b.png)
![image](https://user-images.githubusercontent.com/94480509/195674134-0a80e0b4-3d2c-4046-a23d-0bce97ab09e3.png)

As funcionalidades do relógio já estão prontas, agora vamos estilizar nosso relógio para que pareça mais digital.
Primeiro vamos baixar a fonte aqui neste site. 

**font https://www.1001fonts.com/digital-7-font.html**<br/>
Depois de baixar e extrair as fontes, e coloca no mesmo diretório em que está o nosso script python, iremos adicionar ao nosso aplicativo, mas para isso teremos que instalar outra biblioteca Python primeiro, que é:

**pip install pyglet**
Após a instalação, escreva o seguinte código para adicionar a fonte que acabamos de baixar.

![image](https://user-images.githubusercontent.com/94480509/195674343-94c1fa84-b468-4908-9ec3-2256233b0fb5.png)

Após importar e vincular a fonte, basta usar a fonte e ela estará ativa.<hr>


****Relógio Digital****

![image](https://user-images.githubusercontent.com/94480509/195674728-0d13d23f-6d46-4719-8a05-6299a3426527.png)





