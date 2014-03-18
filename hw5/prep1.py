Names = {}
Names['Albert'] = 'Einstein'
Names['Satyendra'] = 'Bose'
Names['Richard'] = 'Feynman'
Names['Ludwig'] = 'Boltzmann'
# checkpoint 1
for name in Names: print name, Names[name]
a = Names.pop('Albert')
# checkpoint 2
del Names['Richard']
# checkpoint 3
L = Names.keys()
M = Names.values()
#checkpoint 4
b = 'Wolfgang' in Names
#checkpoint 5
