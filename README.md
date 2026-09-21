# 💧 Classificador de Consumo de Água

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-181717?style=for-the-badge&logo=github&logoColor=white)
![Sustentabilidade](https://img.shields.io/badge/Sustentabilidade-Água-00A6D6?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-2ea44f?style=for-the-badge)
![Feito com amor](https://img.shields.io/badge/Feito%20com-%E2%9D%A4-e25555?style=for-the-badge)

## 🌎 Sobre o projeto

Este projeto nasceu de uma campanha de conscientização ambiental de uma companhia de saneamento. A ideia é simples: o programa pergunta o **tipo de imóvel** e o **consumo mensal de água** e, com base nisso, mostra um alerta educativo pro morador, dizendo se o consumo está econômico, moderado ou alto demais.

É um script pequeno, feito para praticar os fundamentos de Python: variáveis, conversão de tipos, entrada de dados e estruturas condicionais.

## 🎯 O que ele faz

1. Pede o tipo de imóvel: `comercial`, `casa` ou `apartamento`.
2. Pede o consumo mensal em metros cúbicos (m³), aceitando decimais (pode digitar `12.5` ou `12,5`).
3. Classifica o perfil de consumo e exibe a mensagem correspondente.

### 📋 Regras de classificação

| Tipo de imóvel | Consumo | Mensagem |
|---|---|---|
| Comercial | qualquer | Tarifa comercial aplicada – consulte o plano corporativo. |
| Apartamento | menor que 10 m³ | Consumo econômico – excelente controle de água! |
| Casa ou apartamento | até 25 m³ | Consumo moderado – dentro do padrão residencial. |
| Casa ou apartamento | acima de 25 m³ | Consumo excessivo – adote medidas de economia e verifique vazamentos. |

> 💡 Se o tipo de imóvel digitado não for válido, o programa avisa em vez de classificar errado.

## 🛠️ Tecnologias

- 🐍 **Python 3** (não precisa instalar nenhuma biblioteca extra)
- 🐙 **Git e GitHub** para versionamento e hospedagem do código

## ▶️ Como executar

**1. Confira se o Python está instalado:**

```bash
python --version
```

Em alguns sistemas o comando é `python3` em vez de `python`.

**2. Clone o repositório:**

```bash
git clone https://github.com/BrunoBianchiVasc
cd Consumo-de-agua
```

**3. Rode o programa:**

```bash
python classificador_consumo.py
```

## 🖥️ Exemplo de uso

```text
Tipo de imóvel (comercial, casa ou apartamento): apartamento
Consumo mensal de água (m³): 8,5

Consumo econômico – excelente controle de água!
```

```text
Tipo de imóvel (comercial, casa ou apartamento): casa
Consumo mensal de água (m³): 30

Consumo excessivo – adote medidas de economia e verifique vazamentos.
```

## 📁 Estrutura do projeto

```text
.
├── classificador_consumo.py   # código principal
└── README.md                  # você está aqui 🙂
```

## 🌱 Dica da campanha

Uma torneira pingando pode desperdiçar dezenas de litros por dia. Conferir vazamentos de vez em quando ajuda o bolso e o planeta. 💙

## 👨‍💻 Autor

Feito por **Bruno** 
