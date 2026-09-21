"""
Classificador de perfil de consumo de água.

Campanha de conscientização ambiental da companhia de saneamento.
O programa pergunta o tipo de imóvel e o consumo mensal (em m³)
e exibe um alerta educativo de acordo com o perfil do morador.
"""

# Limites definidos pelas regras de negócio da campanha
LIMITE_ECONOMICO = 10  # m³ - abaixo disso, apartamento é considerado econômico
LIMITE_RESIDENCIAL = 25  # m³ - acima disso, consumo residencial é excessivo

# --- Entrada de dados ---
# strip() e lower() evitam erro se o usuário digitar espaços ou letras maiúsculas
tipo_imovel = input("Tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()

# replace troca vírgula por ponto, porque o float() só aceita ponto (ex.: 12,5 -> 12.5)
consumo_mensal = float(input("Consumo mensal de água (m³): ").replace(",", "."))

# --- Classificação ---
print()  # linha em branco para separar a entrada do resultado

# Valida o tipo primeiro: sem isso, um tipo inválido cairia no "consumo excessivo"
if tipo_imovel != "comercial" and tipo_imovel != "casa" and tipo_imovel != "apartamento":
    print("Tipo de imóvel inválido – digite comercial, casa ou apartamento.")

elif tipo_imovel == "comercial":
    # Comercial tem tarifa própria, então o consumo não entra na análise
    print("Tarifa comercial aplicada – consulte o plano corporativo.")

elif tipo_imovel == "apartamento" and consumo_mensal < LIMITE_ECONOMICO:
    print("Consumo econômico – excelente controle de água!")

elif consumo_mensal <= LIMITE_RESIDENCIAL:
    # Aqui só chegam casa ou apartamento (comercial e inválidos já foram tratados)
    print("Consumo moderado – dentro do padrão residencial.")

else:
    # Casa ou apartamento acima do limite residencial
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")