# Solicitando o tipo de imóvel e normalizando para letras minúsculas
tipo_imovel = input("Informe o tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()

# Solicitando o consumo mensal em m3
consumo = float(input("Informe o consumo mensal de água em m3: "))

# Estrutura de decisão para classificação e emissão de alertas
if tipo_imovel == "comercial": 
    
    print("Tarifa comercial aplicada – consulte o plano corporativo.")

elif tipo_imovel == "apartamento" and consumo < 10:

    print("Consumo econômico – excelente controle de água!")

elif (tipo_imovel == "apartamento" and consumo <= 25) or (tipo_imovel == "casa" and consumo <= 25):

    print("Consumo moderado – dentro do padrão residencial.")

else:

    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")