"""

Sistema de Relatório de Vendas da SportMax

"""

nome_filial = input("Digite o nome da filial que será analisada: ")
total_vendas_tenis_dia = int(input("Digite a quantidade de tenis vendidos no dia: "))
faturamento_bruto_dia = float(input("Digite o faturamento bruto do dia: "))
resposta_estoque = input("O estoque de segurança está regularizado? True ou False: ")
estoque_seguranca = resposta_estoque.strip().lower() == "true"


#DEFINIÇÃO DE METAS
meta_minima = 250
faturamento_esperado = 50_000
padrao_estoque_exigido = True

# VALIDAÇÃO DOS DADOS 

if total_vendas_tenis_dia != 0:
    validacao_vendas = f"vendas válidas: {total_vendas_tenis_dia} pares registrados."
else:
    validacao_vendas = "ALERTA: vendas igual a zero - nenhum par vendido no dia."

if estoque_seguranca == padrao_estoque_exigido:
    validacao_estoque = "Estoque de segurança CONFERE com o padrão exigido."
else:
    validacao_estoque = "Estoque de segurança DIVERGENTE do padrão exigido."

# TOMADA DE DECISÃO - VERIFICAÇÃO DE METAS E OBJETIVOS

if faturamento_bruto_dia >= faturamento_esperado:
    if estoque_seguranca == padrao_estoque_exigido:
        diagnostico = "META ATINGIDA !!!"
        detalhe = "Quantidade Mínima em estoque suficiente."
    else:
        diagnostico = "META ATINGIDA, MAS COM ALERTA DE ESTOQUE !!!"
        detalhe = "ATENÇÃO: estoque de segurança INSUFICIENTE - risco de capacidade na entrega."

elif faturamento_bruto_dia  <= faturamento_esperado * 0.5:
    diagnostico = "DESEMPENHO CRÍTICO"
    detalhe = f"Filial atingiu: R$ {faturamento_bruto_dia:.2f}, Filial ficou em até 50% da meta - revisão urgente da operação."

elif faturamento_bruto_dia <= faturamento_esperado * 0.8:
    diagnostico = "DESEMPENHO ABAIXO DO ESPERADO"
    detalhe = f"Filial atingiu: R$ {faturamento_bruto_dia:.2f}, Filial ficou entre 50% e 80% da meta - reforce as ações de vendas."

elif faturamento_bruto_dia > faturamento_esperado * 0.95:
    diagnostico = "QUASE ATINGINDO A META"
    detalhe = f"Faltaram apenas R$ {faturamento_esperado - faturamento_bruto_dia:.2f} para o fechamento."

else:
    diagnostico = "DESEMPENHO INTERMEDIÁRIO"
    detalhe = "Filial ficou entre 80% e 95% da meta - resultado dentro do aceitável."

#GERANDO RELATORIO
percentual_meta = (faturamento_bruto_dia / faturamento_esperado) * 100
percentual_volume = (total_vendas_tenis_dia / meta_minima) * 100

# INTRODUÇÃO
print("*" * 50)
print("RELATÓRIO CONSOLIDADO - SPORTMAX")
print("*" * 50)
# DADOS DA EMPRESA
print(f"Filial analisada: {nome_filial.upper()}")
print(f"Pares vendidos: {total_vendas_tenis_dia} unidades.")
print(f"Faturamento bruto do dia: R$ {faturamento_bruto_dia:.2f}")
print(f"Segurança do estoque: {estoque_seguranca}")

# DADOS METAS
print("=" * 50)
print(f"Meta minima: {meta_minima} -- {percentual_volume:.2f}% atingido")
print(f"Faturamento minimo: {faturamento_esperado} -- {percentual_meta:.2f}% atingido")

print("=" * 50)
print(f"- {validacao_vendas}")
print(f"- {validacao_estoque}")

print("=" * 50)
print("DIAGNOSTICO FINAL")
print(f"{diagnostico}")
print(f"{detalhe}")
