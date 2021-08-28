import csv


def write_csv(data: list = None, filename: str = None, fieldnames: list = None):
    if filename and data and fieldnames:
        file = open(filename, 'w')
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for dct in data:
            writer.writerow(dct)
        file.close()
    else:
        print("Error in write_csv look like you did no provide data,fieldnames or filename")


def prep_Adapter_ID_0(data: list = None, fieldnames: list = None):
    output = list()
    if data and fieldnames:
        for item in data:
            try:
                for dns in item.get('DNS Server(s)'):
                    temp = {}
                    for label in fieldnames:
                        temp[label] = None
                    temp['VM ID'] = item.get('VM ID')
                    temp['vCenter Server'] = item.get('vCenter Server')
                    temp['VM Name'] = item.get('VM Name')
                    temp['Adapter ID'] = 0
                    temp['DNS Server(s)'] = dns
                    temp['IP Address'] = None
                    temp['Subnet Mask'] = None
                    temp['Gateway(s)'] = None
                    temp['DNS Suffix(es)'] = None
                    output.append(temp)
                for dnsSufix in item.get('DNS Suffix(es)'):
                    temp = {}
                    for label in fieldnames:
                        temp[label] = None
                    temp['VM ID'] = item.get('VM ID')
                    temp['vCenter Server'] = item.get('vCenter Server')
                    temp['VM Name'] = item.get('VM Name')
                    temp['Adapter ID'] = 0
                    temp['DNS Server(s)'] = None
                    temp['IP Address'] = None
                    temp['Subnet Mask'] = None
                    temp['Gateway(s)'] = None
                    temp['DNS Suffix(es)'] = dnsSufix
                    output.append(temp)
            except Exception as e:
                print(e)
    return output


def prep_Adapter_ID_n(data: list = None, fieldnames: list = None):
    output = list()
    if data and fieldnames:
        for item in data:
            try:
                ips = item.get('IP Address')
                subnets = item.get('Subnet Mask')
                gateways = item.get('Gateway(s)')
                for i in range(0, len(ips)):
                    temp = {}
                    for label in fieldnames:
                        temp[label] = None
                    temp['VM ID'] = item.get('VM ID')
                    temp['vCenter Server'] = item.get('vCenter Server')
                    temp['VM Name'] = item.get('VM Name')
                    temp['DNS Server(s)'] = None
                    temp['DNS Suffix(es)'] = None
                    temp['IP Address'] = ips[i]
                    temp['Subnet Mask'] = subnets[i]
                    if len(gateways) == len(ips):
                        temp['Gateway(s)'] = gateways[i]
                    else:
                        temp['Gateway(s)'] = gateways[0]
                    temp['Adapter ID'] = i+1
                output.append(temp)
            except Exception as e:
                print(e)
    return output
