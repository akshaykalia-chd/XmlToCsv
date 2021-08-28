from utils import write_csv, prep_Adapter_ID_0, prep_Adapter_ID_n, fix_key
from xmltocsv import xmlToCsv

get_data = xmlToCsv(input_file='multiple_nics.xml')
get_data.read_vm_data()
data = list()
for item in get_data.vm_data:
    item['DNS Suffix(es)'] = fix_key(data=item, key='DNS Suffix(es)')
    item['DNS Server(s)'] = fix_key(data=item, key='DNS Server(s)')
    item['Gateway(s)'] = fix_key(data=item, key='Gateway(s)')
    item['IP Address'] = fix_key(data=item, key='IP Address')
    item['Subnet Mask'] = fix_key(data=item, key='Subnet Mask')
    data.append(item)
print(data)
csv_data = prep_Adapter_ID_0(data=data, fieldnames=get_data.labels)
for dct in (prep_Adapter_ID_n(data=data, fieldnames=get_data.labels)):
    csv_data.append(dct)
write_csv(data=csv_data, filename="./SRM-IPs-1.csv", fieldnames=get_data.labels)



