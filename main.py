from utils import write_csv, prep_Adapter_ID_0, prep_Adapter_ID_n
from xmltocsv import xmlToCsv

get_data = xmlToCsv(inputfile='multiple_nics.xml', root_tag='ProtectedVm')
data = list()
for item in get_data.read_vm_data():
    item['DNS Suffix(es)'] = get_data.fix_key(data=item, key='DNS Suffix(es)')
    item['DNS Server(s)'] = get_data.fix_key(data=item, key='DNS Server(s)')
    item['Gateway(s)'] = get_data.fix_key(data=item, key='Gateway(s)')
    item['IP Address'] = get_data.fix_key(data=item, key='IP Address')
    item['Subnet Mask'] = get_data.fix_key(data=item, key='Subnet Mask')
    data.append(item)
print(data)
#csv_data = prep_Adapter_ID_0(data=data, fieldnames=get_data.labels)
#write_csv(data=csv_data, filename="./SRM-Global-1.csv", fieldnames=get_data.labels)
test = (prep_Adapter_ID_n(data=data, fieldnames=get_data.labels))
write_csv(data=test, filename="./SRM-IPs-1.csv", fieldnames=get_data.labels)


