camp = ('Sport Recife','Náutico','Santa Cruz','Salgueiro','Central','Afogados','Vitória','Petrolina','América','Flamengo Arcoverde')
c = 1
i = 0
j = 7
print('=============================')
print('3 PRIMEIRAS POSIÇÕES:')
print('=============================')
for i in range(0,3):    
    print(c,'º  .....',camp[i])  
    c += 1
    i += 1
print('=============================')
print('4 ÚLTIMAS POSIÇÕES:')
print('=============================')
for i in range(6,10):
    print(j,'º .....',camp[i])
    i += 1
    j += 1
print('=============================')
print('ORDEM ALFABÉTICA:') 
print('=============================')
print(sorted(camp))
print('=============================')
print('POSIÇÃO DO TIME VITÓRIA:')
print('=============================')
print('Vitória está na posição',camp.index('Vitória'))   
