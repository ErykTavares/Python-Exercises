class TV():
    """tentativa de simular uma televisão"""
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume 

    def Cnl(self, C):
        """Altera o canal"""
        self.canal = C
        if self.canal >= 1 or self.canal <= 30:
            return F"Canal {self.canal}"
        else:
            return "Canal não disponivel!"

    
    def Vol(self, V):
        """aumenta ou diminui o volume"""
        self.volume = V
        if self.volume >= 1 and self.volume <= 50:
            return F"Volume {self.volume }"
        elif self.volume >= 50:
            return "Volume maximo excedido"
        elif self.volume == 0:
            return "Menor volume atingido"

    