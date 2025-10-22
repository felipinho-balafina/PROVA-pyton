# 🚗 Subclasse — CarroPasseio

class CarroPasseio(Veiculo):
    #Representa um carro de passeio, herdando as características de veiculo.
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem, numero_portas, tipo_combustivel):
        super().__init__(marca, modelo, ano_fabricacao, chassi, cor, quilometragem)
        self._numero_portas = numero_portas
        self._tipo_combustivel = tipo_combustivel
   
   # Método: Calcular Depreciação
    # ---
    def calcular_depreciacao(self, anos_uso, taxa_extra): #Calcula a depreciação com base no tempo de uso e taxa extra.
        depreciacao = (0.05 + taxa_extra) * anos_uso
        print(f"[DEPRECIAÇÃO] O carro {self._modelo} teve uma depreciação de {depreciacao * 100:.1f}% após {anos_uso} anos.")
        return depreciacao

     # Método Sobrescrito: Exibir Informações
    # ---
    def exibir_informacoes(self, detalhado=False): #Exibe informações do carro de passeio, incluindo seus atributos específicos.
        super().exibir_informacoes(detalhado)
        if detalhado:
            print(f"Número de Portas: {self._numero_portas}")
            print(f"Tipo de Combustível: {self._tipo_combustivel}")
