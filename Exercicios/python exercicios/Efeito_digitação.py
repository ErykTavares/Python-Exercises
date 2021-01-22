from time import sleep

text = "A Historia se inicia com 2 lendas se encarando frente a frente, e então a tela se escurece  e sons e mais sons de espadas se batendo aparecem no ar"
for i in text:
    sleep(0.1)
    print(i, end="", flush=True)
