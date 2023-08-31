import subprocess
import json
import sys
'''crawler class'''

class Crawler:
    domain_list =[]
    subdomain_list=[]
    fqdn = []
    results=[]

    
    def __init__(self, domain_list, subdomain_list):
        self.domain_list = domain_list
        self.subdomain_list = subdomain_list
        self.create_fqdn_list()       
        self.welcome_message()   


    def welcome_message(self):
        print("\n----------Berkay Tokdam----------")
        print(f"\n**********welcome crawler**********\n")
        

    def create_fqdn_list(self):
        for domain in self.domain_list:
            for subdomain in self.subdomain_list:
                full_subdomain = f"{subdomain}.{domain}"
                self.fqdn.append(full_subdomain)
            

    def get_domain_info_with_curl(self):
        for domain in self.fqdn:
            print(f"- [{domain}] :")
            curl_command = ["curl", "-sI", f"http://{domain}"]
            try:
                curl_output = subprocess.check_output(curl_command, stderr=subprocess.DEVNULL, text=True)
                header = curl_output.strip()
                server_type = None
                for line in header.split('\n'):
                    if line.lower().startswith("server:"):
                        server_type = line.split(": ", 1)[1]
                        print(f"\tserver type: {server_type}")
                        break
            except:
                server_type = None
            self.results.append(server_type)

        self.save_results_json("results.json")        


            
    def save_results_json(self, filename):
        result_dict = {fqdn: result for fqdn, result in zip(self.fqdn, self.results)}

        try:
            with open(filename, 'w') as json_file:
                json.dump(result_dict, json_file, indent=4)
            print(f"\nSonuclar kaydedildi: {filename}\n")
        except:
            print(f"Sonuclar kaydedilirken hata oldu")