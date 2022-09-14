lista=[]
while True:
    nota=float(input("Digite a nota:"))
    lista.append(nota)
    continuar=str(input("Deseja Continuar [S/N]?")).upper()
    if continuar=="N":
        maximo=max(lista)
        minimo=min(lista)
        media=sum(lista)/len(lista)
        break
print("Sua Nota máxima foi de {}".format(maximo))
print("Sua Nota mínima foi de {}".format(minimo))
print("Sua média ficou {:.2f}".format(media))