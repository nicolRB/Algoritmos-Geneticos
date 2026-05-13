# Algoritmos-Geneticos
Um sistema para encontrar, com IA baseada em seleção natural, um kit ideal de sobrevivência

## Como Executar
- faça download das bibliotecas com o comando no terminal ``pip install -r requirements.txt``
- execute o app com o comando ``python -m ui.app``

## Estrutura
- backend/ cuida da parte funcional do sistema, é onde os algoritmos que trabalham com genes e evolução são encontrados
- models/ possui os templates para as classes de cromossomos e itens utilizados
- data/ possui a tabela de itens e seus valores baseado no modelo de itens
- ui/ é o frontend do sistema e cuida da parte visual e interativa do sistema
- utils/ possui as constantes do sistema que definem o peso máximo e o número de cromossomos por individuo

## Funcionamento 
É feito uma tabela de itens com diferentes valores de sobrevivência e pesos. Aleatoriamente é gerado uma população inicial com diferentes cromossomos em que aqueles que ultrapassam o limite de peso são removidos. através do sistema de crossover, diferentes individuos selecionados tem seus genes cruzados e misturados para criar individuos novos com genes aleatoriamente selecionados dos pais, com uma chance de mutação que inverte um dos valores dos cromossomos de um novo individuo.