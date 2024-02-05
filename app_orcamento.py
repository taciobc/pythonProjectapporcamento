larg = float(input('Qual a largura do terreno? '))
alt = float(input('Qual a altura da parede? '))
area = larg * alt
print('A área da parede é de {} x {} = {}m²'.format(larg, alt, area))

# Cálculo de tinta
tinta = area / 2
print('A quantidade de litros de tinta é de {}L'.format(tinta))

# Cálculo de materiais de construção (valores arbitrários)
areia_por_m2 = 0.5  # em kg por metro quadrado
cimento_por_m2 = 0.2  # em kg por metro quadrado
pedra_por_m2 = 0.8  # em kg por metro quadrado
tijolos_por_m2 = 12  # quantidade de tijolos por metro quadrado
telhas_por_m2 = 8  # quantidade de telhas por metro quadrado
lajes_por_m2 = 1  # quantidade de lajes por metro quadrado

quantidade_areia = area * areia_por_m2
quantidade_cimento = area * cimento_por_m2
quantidade_pedra = area * pedra_por_m2
quantidade_tijolos = area * tijolos_por_m2
quantidade_telhas = area * telhas_por_m2
quantidade_lajes = area * lajes_por_m2

print('Quantidade de areia necessária: {:.2f} kg'.format(quantidade_areia))
print('Quantidade de cimento necessária: {:.2f} kg'.format(quantidade_cimento))
print('Quantidade de pedra necessária: {:.2f} kg'.format(quantidade_pedra))
print('Quantidade de tijolos necessária: {:.0f} unidades'.format(quantidade_tijolos))
print('Quantidade de telhas necessária: {:.0f} unidades'.format(quantidade_telhas))
print('Quantidade de lajes necessária: {:.0f} unidades'.format(quantidade_lajes))
