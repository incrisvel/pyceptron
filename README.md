# Pyceptron

Uma implementação de Perceptron em Python para classificação de potabilidade da água usando validação cruzada K-Fold.

## Componentes Principais

### `Pyceptron` 
Implementação do algoritmo perceptron com:
- **Inicialização**: Pesos zerados e bias zero para cada feature
- **Net Input**: Cálculo de entrada ponderada + bias
- **Ativação**: Função degrau (0 ou 1)
- **Treinamento**: Atualização iterativa de pesos com correção de erro
- **Predição**: Classificação de novos dados

### `Reader`
- Lê dataset a partir de arquivo CSV
- Cria objetos `Water` para cada registro
- Embaralha o dataset

### `KFold`
- Divide dataset em K folds (padrão: 5)
- Gera conjuntos de treino e teste para cada fold
- Implementa estratégia de validação cruzada

### `Models`
- `PyceptronSet`: Contém features (dicionários) e labels
- `FoldSets`: Agrupa conjuntos de teste e treino
- `Water`: Abstração dos dados de potabilidade da água

## Como Rodar

### Pré-requisitos
- Python 3.8+

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/incrisvel/pyceptron.git
cd pyceptron
```

2. Verifique que o Python está instalado:
```bash
python3 --version
```

### Execução

Para rodar o treinamento e avaliação do modelo:

```bash
cd src
python3 main.py
```

#### Saída Esperada
O script executará 5 folds de validação cruzada e exibirá:
- Resultado de cada fold (acertos/total e porcentagem)
- Lista de acurácias por fold
- **Acurácia média final (K-Fold)**

Exemplo:
```
FOLD 1/5
Acertos no Fold 1: 410/655 = 62.60%

FOLD 2/5
Acertos no Fold 2: 394/655 = 60.15%

...

RESULTADOS FINAIS
Acurácias por Fold: ['62.60%', '60.15%', '60.31%', '62.90%', '59.15%']
Acurácia Média (5-fold): 61.02%
```

## Configuração

### Parâmetros do Perceptron (`pyceptron.py`)
```python
self.learning_rate = 0.1  # Taxa de aprendizado
self.epochs = 1            # Número de épocas de treinamento
```

### Parâmetros do K-Fold (`main.py`)
```python
K_VALUE = 5  # Número de folds
```

## Dataset

O projeto utiliza o dataset **Water Potability**:
- **Arquivo**: `data/water_potability.csv`
- **Formato**: CSV com múltiplas features de qualidade da água relacionadas à potabilidade
- **Rótulos**: 0 (não potável) ou 1 (potável)