from utils import write_csv, prep_Adapter_ID_0, prep_Adapter_ID_n, fix_key
from xmltocsv import xmlToCsv

filename = input("Enter the Absolute path of XML file to process:")
output_filename = input("Enter the Absolute path for output csv file:")

get_data = xmlToCsv(input_file=filename)
get_data.read_vm_data()
data = list()
for item in get_data.vm_data:
    item['DNS Suffix(es)'] = fix_key(data=item, key='DNS Suffix(es)')
    item['DNS Server(s)'] = fix_key(data=item, key='DNS Server(s)')
    item['Gateway(s)'] = fix_key(data=item, key='Gateway(s)')
    item['IP Address'] = fix_key(data=item, key='IP Address')
    item['Subnet Mask'] = fix_key(data=item, key='Subnet Mask')
    data.append(item)
csv_data = prep_Adapter_ID_0(data=data, fieldnames=get_data.labels)
for dct in (prep_Adapter_ID_n(data=data, fieldnames=get_data.labels)):
    csv_data.append(dct)
write_csv(data=csv_data, filename=output_filename, fieldnames=get_data.labels)



