# 🚚 Subclasse — CaminhaoCarga

class CaminhaoCarga(Veiculo):#Representa um caminhão de carga, herdando as características de Veiculo.
    
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem, capacidade_toneladas, eixos):
        super().__init__(marca, modelo, ano_fabricacao, chassi, cor, quilometragem)
        self._capacidade_toneladas = capacidade_toneladas
        self._eixos = eixos

    # Método: Registrar Vistoria
    # ---
    def registrar_vistoria(self, motivo, multa=0): #Registra o motivo de uma vistoria e o valor da multa (se houver).
        
        print(f"[VISTORIA] Motivo: {motivo}. Multa: R$ {multa:.2f}.")

    # Método Sobrescrito: Exibir Informações
    # ---
    def exibir_informacoes(self, detalhado=False):#Exibe informações do caminhão de carga, incluindo seus atributos específicos.
        
        super().exibir_informacoes(detalhado)
        if detalhado:
            print(f"Capacidade de Carga: {self._capacidade_toneladas} toneladas")
            print(f"Número de Eixos: {self._eixos}")
