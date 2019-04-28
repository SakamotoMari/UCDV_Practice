#import csv

#with open('efi_smallest.csv') as f:
#    r=csv.reader(f,delimiter=',')
#    dict_efi={row[0]:row[1] for row in r}

#with open('hfi.csv') as f:
#    r=csv.reader(f,delimiter=',')
#    dict_hfi={row[0]:row[1] for row in r}

#keys=set(dict_efi.keys()+dict_hfi.keys())
#with open('output.csv','wb') as f:
#    w=csv.writer(f,delimiter=',')
#    w.writerows([[key, dict_efi.get(key,"''"),dict_hfi.get(key,"''")] for key in keys])

import pandas as pd

efi=pd.read_csv("efi_smallest.csv")
hfi=pd.read_csv("hfi.csv")

merged=efi.merge(hfi, on='Countries')
merged.to_csv("output.csv",index=False)
