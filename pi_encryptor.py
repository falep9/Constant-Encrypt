import tkinter as tk

def criptografar():
    pi = "3141592653589"
    frase = entrada.get() # pega o texto da entrada
    i = 0
    mensagem_final = ""

    for letra in frase:
        letra = letra.upper()
        if letra.isalpha():
            posicao = ord(letra) - 64
            
            if posicao <= 11:
                resultado = posicao + 26
            else:
                digito_pi = int(pi[i])
                resultado = posicao + digito_pi
                i += 1
                if i >= len(pi):
                    i = 0
            
            mensagem_final = mensagem_final + str(resultado) + "."
    
    # exibe o resultado da interface
    label_resultado.config(text=f"Resultado: {mensagem_final}")

# configs da janela principal
janela = tk.Tk()
janela.title("Pi Encryptor")
janela.geometry("400x250") # define um tamanho pra janela

# elementos da interface 
label_instrucao = tk.Label(janela, text="Digite a frase para criptografar:")
label_instrucao.pack(pady=10)

entrada = tk.Entry(janela, width=40)
entrada.pack(pady=5)

botao = tk.Button(janela, text="Criptografar Agora", command=criptografar)
botao.pack(pady=20)

label_resultado = tk.Label(janela, text="Resultado: ", wraplength=350)
label_resultado.pack(pady=10)

janela.mainloop()