from bs4 import BeautifulSoup

class xmlToCsv():
    def __init__(self, inputfile: str = None, root_tag: str = None):
        if inputfile and root_tag:
            file = open(inputfile, "r")
            contents = file.read()
            file.close()
            self.soup = BeautifulSoup(contents, 'xml')
            self.all_root_tag = self.soup.findAll(root_tag)
            self.vm_data = list()
            self.labels = ("VM ID",
                           "VM Name",
                           "vCenter Server",
                           "Adapter ID",
                           "DNS Domain",
                           "Net BIOS",
                           "Primary WINS",
                           "Secondary WINS",
                           "IP Address",
                           "Subnet Mask",
                           "Gateway(s)",
                           "IPv6 Address",
                           "IPv6 Subnet Prefix length",
                           "IPv6 Gateway(s)",
                           "DNS Server(s)",
                           "DNS Suffix(es)"
                           )
        else:
            print("Error cannot init without input file or root_tag")

    def read_vm_data(self):
        output = list()
        for data in self.all_root_tag:
            CustomizationSpec = data.findAll('CustomizationSpec')
            sites = list()
            for Customization in CustomizationSpec:
                sites.append(Customization['site'])
            for site in sites:
                site_data = data.find(attrs={'site': site})
                ip_settings = site_data.findAll('ConfigRoot')
                for setting in ip_settings:
                    temp = {}
                    temp['vCenter Server'] = site
                    temp['VM ID'] = data.ProductionVmMoId.get_text()
                    temp['VM Name'] = data.Name.get_text()
                    temp['Adapter ID'] = None
                    temp['DNS Domain'] = None
                    temp['Net BIOS'] = None
                    temp['Primary WINS'] = None
                    temp['Secondary WINS'] = None
                    temp['IPv6 Address'] = None
                    temp['IPv6 Subnet Prefix length'] = None
                    temp['IPv6 Gateway(s)'] = None
                    try:
                        temp['DNS Suffix(es)'] = setting.dnsSuffixes.findAll('e')
                    except Exception as e:
                        print("Error finding DNS Suffix(es)", e)
                        temp['DNS Suffix(es)'] = None
                    try:
                        temp['Subnet Mask'] = setting.findAll('subnetMask')
                    except Exception as e:
                        print("Error finding Subnet Mask", e)
                        temp['Subnet Mask'] = None
                    try:
                        temp['IP Address'] = setting.findAll('ipAddress')
                    except Exception as e:
                        print("Error finding IP Address", e)
                        temp['IP Address'] = None
                    try:
                        temp['DNS Server(s)'] = setting.dnsServerList.findAll('e')
                    except Exception as e:
                        print("Error finding DNS Server(s)", e)
                        temp['DNS Server(s)'] = None
                    try:
                        temp['Gateway(s)'] = setting.gateway.findAll('e')
                    except Exception as e:
                        print("Error finding Gateway(s)", e)
                        temp['Gateway(s)'] = None
                    output.append(temp)
        self.vm_data = output
        return output

    def fix_key(self, data: dict = None, key: str = None):
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
