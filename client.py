
class Client:
    def __init__(self,serveIPAdress=None,LocalIP=None) -> None:
        self.IPAdress=serveIPAdress
        self.LocalIP=LocalIP
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
    client=Client(None, " 192.168.0.1")
    client.check_IP_adress()