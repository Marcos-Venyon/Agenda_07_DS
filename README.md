Um script em Python simples e dinâmico que analisa o consumo mensal de água (m3) com base no tipo de imóvel (comercial, casa ou apartamento) e retorna mensagens organizadas sobre a tarifa aplicável.

---

## 🎯 Funcionalidades

- **Identificação do Imóvel:** Diferencia o fluxo de análise entre estabelecimentos comerciais, casas e apartamentos.
- **Tratamento de Entrada:** Normaliza a entrada do tipo de imóvel removendo espaços e ignorando maiúsculas/minúsculas.
- **Classificação de Consumo:**
  - 🏬 **Comercial:** Encaminha para consulta de plano corporativo.
  - 🟢 **Econômico (Apartamento, < 10 m3):** Alerta de excelente controle.
  - 🟡 **Moderado (Residencial, <= 25 m3>):** Notificação dentro do padrão esperável.
  - 🔴 **Excessivo (Qualquer residencial com > 25 m3):** Alerta de economia e verificação de vazamentos.

---

## 💻 Exemplo de Uso

Informe o tipo de imóvel (comercial, casa ou apartamento): Apartamento
Informe o consumo mensal de água em m3: 8.5
Consumo econômico – excelente controle de água!