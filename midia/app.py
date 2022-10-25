
from dvd import DVD
from cd import CD

cd = CD(1, 9.99, 'Calypso', 'Tipo Musica', 'So os sucesso', '20 musicas', 'Dados ok', 14, 15)
dvd = DVD(1, 9.99, 'Velozes&Furiosos', 'Tipo Filme', 'Corrida de carro', '115 minutos', 'Dados ok', 1, 2)

print(cd.get_musica())
print(cd.get_detalhes())
cd.cd()
print('')
print(dvd.get_tipo())
print(dvd.get_nFaixas())
dvd.dvd()