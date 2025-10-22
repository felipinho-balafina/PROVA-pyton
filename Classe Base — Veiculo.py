
# 🏎️ Classe Base — Veiculo

class Veiculo:
    
    # Representa as características comuns a qualquer veículo da frota.
    

    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem):
        #  Atributos encapsulados
        self._marca = marca
        self._modelo = modelo
        self._ano_fabricacao = ano_fabricacao
        self._chassi = chassi
        self._cor = cor
        self._quilometragem = quilometragem
        self._manutencoes = []  # Lista de manutenções realizadas

    # Encapsulamento: Getters e Setters
    # -----
    def get_marca(self):
        return self._marca

    def set_marca(self, nova_marca):
        self._marca = nova_marca

    # Método: Registrar Manutenção
    # ---
    def registrar_manutencao(self, tipo, custo): # Registra uma manutenção no histórico do veículo.
        
        self._manutencoes.append((tipo, custo))
        print(f"[MANUTENÇÃO] O veículo {self._modelo} teve uma manutenção de '{tipo}' com custo de R$ {custo:.2f}.")

    # Método: Exibir Informações
    # ---
    def exibir_informacoes(self, detalhado=False):
     #Exibe informações básicas ou detalhadas do veículo.
        if not detalhado:
            print(f"{self._marca} {self._modelo} — {self._quilometragem} km")
        else:
            print(f"Marca: {self._marca}")
            print(f"Modelo: {self._modelo}")
            print(f"Ano de Fabricação: {self._ano_fabricacao}")
            print(f"Chassi: {self._chassi}")
            print(f"Cor: {self._cor}")
            print(f"Quilometragem: {self._quilometragem} km")
