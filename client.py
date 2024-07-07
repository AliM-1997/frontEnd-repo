import yaml
import os
class Client:
    def __init__(self, config_path=None):
        with open(config_path, 'r') as file:
            self.reader = yaml.safe_load(file)
        self.server_ip = self.reader.get("ServerIPAddress")
        self.LocalIP=self.reader.get("localIPAddress")
        self.connect=False

    def check_IP_adress(self):
        if self.IPAdress!=None:
            print(f"connected to server with IP: {self.IPAdress}")
            self.connect=True
        else:
            print("not connected to any server")
            self.connect=False
            print(f"Local IP{self.LocalIP}")
    
if __name__=="__main__":
    config_name="config.yml"
    parent_directory=os.getcwd()
    config_path=os.path.join(parent_directory,config_name)
    print(config_path)
    client=Client(config_path)
    client.check_IP_adress()