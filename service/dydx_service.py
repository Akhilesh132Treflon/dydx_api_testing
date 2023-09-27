from dydx3 import Client
from web3 import Web3
from dydx3.constants import API_HOST_GOERLI
from dydx3.constants import NETWORK_ID_GOERLI
"""
This class DydxPClient is responsible for initializing the DydxClient instance.
It has a function __create_dydx_Instance() that is responsible for initializing the dydx instance and returning it.
"""

WEB_PROVIDER = "https://goerli.infura.io/v3/2dff452478174fdf8035dc20eadb5667"
API_KEY= "98bdd3bc-4539-af3d-8f09-daa6d1f4b2fc"
SECRET_KEY="SR0UhCDdiftWB5stbdqvzKtSXFLj8Qas4JbVm-fh"
API_PASSPRASE="8JOXA_tP_dEQwWx0xvX7"
PRIVATE_KEY="ba7a44643aa5c0e1fd70226c0f67cbce09358d92db9a7093af35104b41bad356"
STARTK_PRIVATE_KEY="04841cd300a31dbf05dd5615edbabf5aabc117e79009fd1bda9817897b574c08"



client = None

class DydxPClient(object):
    def create_dydx_instance(self):
        client = Client(
            host=API_HOST_GOERLI,
            network_id=NETWORK_ID_GOERLI,
            stark_private_key=STARTK_PRIVATE_KEY,
            web3=Web3(Web3.HTTPProvider(WEB_PROVIDER)),
            eth_private_key=PRIVATE_KEY,
            api_key_credentials={
                "key":API_KEY, 
                "secret": SECRET_KEY,
                "passphrase":API_PASSPRASE,
            }
        )
        return client

    def client (self):
        if client:
            return client
        else: 
            return self.create_dydx_instance()


if __name__ == "__main__":
    d = DydxPClient()
    print(d)
