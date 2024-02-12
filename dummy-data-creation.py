import pandas as pd
import random

# declaring lists
khewat_nos = []
khewat_khasras_list = []
khewat_khasras = []
khewat_rqbas = []
khasra_nos = []
khasra_rqbas = []
owner_name = []

# creating khewat nos list. It will contain khewats ranging from 1 to 200
print('# creating khewat nos...')
for i in range(1, 201):
  khewat_nos.append(i)

# creating khewat khasras list for iterating from 1000 to 1200. Storing i in a sub list i.e. khewat_khasras and when the sublist counts to 4 values then appending that to
# the main khewat_khasras_list (that will be used while creating DataFrame). In each appending, clearing the sublist in order to use it for further iterations
print('# creating khewat khasras list...')
for i in range(1000, 1801):
  khewat_khasras.append(i)
  if len(khewat_khasras) == 4:
    khewat_khasras_list.append(khewat_khasras)
    khewat_khasras = []

# creating khasra nos.It will contain khasras ranging from 1 to 200
print('# creating khasra nos...')
for i in range(1000, 1200):
  khasra_nos.append(i)

# creating khasra_rqbas list uisng the {knl}-{mrla}-{feet} as string format. The list will have 200 values
print('# creating khasra_rqbas list...')
for i in range(1, 201):
  knl = random.randint(1, 200)
  mrla = random.randint(0, 19)
  feet = random.randint(0, 271)
  khasra_rqbas.append(f"{knl}-{mrla}-{feet}")

# creating khewat_rqbas list using khasra_rqbas list, previously created
print('# creating khewat_rqbas list...')
khewat_rqbas = khasra_rqbas.copy()

# creating owner name list (keeping length to 200 because each khasra will have a khewat and owner name in real data.)
for i in range(0, 200):
  owner_name.append('Malik Nasir Ali Khan')

# creating and saving the DataFrame as csv
df = pd.DataFrame({'owner_name': owner_name, 'khewat_nos': khewat_nos, 'khewat_khasras_list': khewat_khasras_list, 'khewat_rqbas': khewat_rqbas, 'khasra_nos': khasra_nos, 'khasra_rqbas': khasra_rqbas})
df.to_csv('land_ledger_dummy.csv')

# printing details about the data created
print(f"Size: khewat_nos : {len(khewat_nos)}. Data sample: {khewat_nos[1]}")
print(f"Size: khewat_khasras_list : {len(khewat_khasras_list)}. Data sample: {khewat_khasras_list[1]}")
print(f"Size: khewat_rqbas : {len(khewat_rqbas)}. Data sample: {khewat_rqbas[1]}")
print(f"Size: khasra_nos : {len(khasra_nos)}. Data sample: {khasra_nos[1]}")
print(f"Size: khasra_rqbas : {len(khasra_rqbas)}. Data sample: {khasra_rqbas[1]}")
print(f"Size: owner_name : {len(owner_name)}. Data sample: {owner_name[1]}")

print('All done successfully.')
