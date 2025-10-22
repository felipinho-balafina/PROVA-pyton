O código desenvolvido implementa um sistema de gerenciamento de frota de veículos, utilizando os principais conceitos da Programação Orientada a Objetos (POO) em Python: Herança, Polimorfismo, Encapsulamento e Simulação de Sobrecarga.

🔹 Estrutura Geral

O programa é composto por três classes principais:
Veiculo → Superclasse (ou classe base)
CarroPasseio → Subclasse que herda de Veiculo
CaminhaoCarga → Subclasse que também herda de Veiculo
Essas classes representam diferentes tipos de veículos e suas características específicas, permitindo o reuso de código e uma estrutura organizada e extensível.

🏎️ Classe Veiculo (Superclasse)

A classe Veiculo define os atributos comuns a todos os tipos de veículos, como:
marca
modelo
ano_fabricacao
chassi
cor
quilometragem
Além disso, ela possui um método para registrar manutenções (registrar_manutencao) e outro para exibir informações (exibir_informacoes).

🔒 Encapsulamento
Os atributos foram declarados com underscore (_) no início do nome (exemplo: _marca), o que indica que são atributos protegidos.
Para acessá-los de forma controlada, foram criados métodos getters e setters, o que é uma prática de encapsulamento — proteger os dados internos da classe.

🧾 Sobrecarga Simulada
O método exibir_informacoes(detalhado=False) possui um parâmetro opcional, permitindo dois comportamentos diferentes:
Se detalhado=False, mostra apenas informações básicas.
Se detalhado=True, mostra todos os atributos.
Isso simula o conceito de sobrecarga de métodos, que não existe diretamente em Python.

🚗 Classe CarroPasseio (Subclasse)

A classe CarroPasseio herda da classe Veiculo, aproveitando todos os atributos e métodos da superclasse.
Ela adiciona dois novos atributos específicos:
numero_portas
tipo_combustivel
Além disso, implementa dois novos métodos:
calcular_depreciacao(anos_uso, taxa_extra)
Calcula a depreciação do carro com base no tempo de uso e uma taxa adicional informada.
Exemplo de aplicação prática de lógica personalizada em subclasses.

exibir_informacoes()
O método é sobrescrito (Polimorfismo) para incluir também os novos atributos do carro de passeio.

🚚 Classe CaminhaoCarga (Subclasse)

A classe CaminhaoCarga também herda de Veiculo, mas adiciona características voltadas a caminhões:
capacidade_toneladas
eixos
Ela define dois novos métodos:
registrar_vistoria(motivo, multa=0)
Registra uma vistoria, exibindo o motivo e o valor da multa, se houver.
exibir_informacoes()
Método sobrescrito para mostrar as informações específicas do caminhão (Polimorfismo).

🔄 Herança e Polimorfismo em Ação
Herança:
Ambas as subclasses (CarroPasseio e CaminhaoCarga) herdam os métodos e atributos de Veiculo.
Isso evita repetição de código e permite reutilizar a estrutura da superclasse.
Polimorfismo:
As subclasses sobrescrevem o método exibir_informacoes(), adaptando-o ao seu contexto.
O mesmo nome de método se comporta de maneira diferente dependendo da classe — isso é polimorfismo.

🔧 Encapsulamento

Os atributos são privados (prefixados com _), e o acesso é feito apenas por métodos (get_ e set_).
Isso garante segurança e controle sobre os dados internos, impedindo que sejam alterados diretamente fora da classe.

💡 Demonstração Prática

No final do arquivo, há um bloco de testes dentro do comando:

if __name__ == "__main__":

Esse bloco cria objetos das subclasses e executa:
Registro de manutenção
Cálculo de depreciação
Exibição de informações detalhadas
Registro de vistorias
Dessa forma, o código mostra claramente o funcionamento dos conceitos de POO em situações reais.

🧠 Conclusão

Este sistema demonstra, de forma prática, como a Programação Orientada a Objetos permite construir programas modulares, reutilizáveis e organizados.
A Herança facilita a extensão de classes.
O Polimorfismo permite comportamentos diferentes com o mesmo método.
O Encapsulamento protege os dados.
A Sobrecarga simulada mostra como Python permite flexibilidade nos métodos.

O código é funcional, didático e segue boas práticas de POO, sendo ideal para apresentação acadêmica.
