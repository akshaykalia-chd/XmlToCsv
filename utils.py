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


def fix_key(data: dict = None, key: str = None):
    if data and key:
        try:
            # print(data)
            output = list()
            items = data.get(key)
            # print(items)
            for item in items:
                output.append(item.get_text())
            # print(output)
            return output
        except Exception as e:
            print(e)
    else:
        print("Data and key are need to operate")


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
                    output.append(temp)
                for dnsSufix in item.get('DNS Suffix(es)'):
                    temp = {}
                    for label in fieldnames:
                        temp[label] = None
                    temp['VM ID'] = item.get('VM ID')
                    temp['vCenter Server'] = item.get('vCenter Server')
                    temp['VM Name'] = item.get('VM Name')
                    temp['Adapter ID'] = 0
                    temp['DNS Suffix(es)'] = dnsSufix
                    output.append(temp)
            except Exception as e:
                print(e)
    return output


def prep_Adapter_ID_n(data: list = None, fieldnames: list = None):
    output = list()
    if data and fieldnames:
        for item in data:
            index = 0
            ips = item.get('IP Address')
            subnets = item.get('Subnet Mask')
            gateways = item.get('Gateway(s)')
            while(index <= (len(ips) - 1)):
                temp = {}
                for label in fieldnames:
                    temp[label] = None
                temp['VM ID'] = item.get('VM ID')
                temp['vCenter Server'] = item.get('vCenter Server')
                temp['VM Name'] = item.get('VM Name')
                temp['IP Address'] = ips[index]
                temp['Subnet Mask'] = subnets[index]
                if len(gateways) == len(ips):
                    temp['Gateway(s)'] = gateways[index]
                else:
                    temp['Gateway(s)'] = gateways[-1]
                temp['Adapter ID'] = index + 1
                index += 1
                output.append(temp)
    return output
