#### img-cryptor 


did you ever have to encrypt your data cause it is so sensitive that you cannot store it on hdd to read in normal batch processing? No? But I do, sadly (documents, scans, etc. which were used to feed deep learning model).


key, initialize vector creation, AES256, store images with ```.enc``` extension.In progress. 



Example usage:



Assuming that you'll store your image in ```example``` folder and save your keys in ```.bin``` format you can change your config param to provide an proper encryption. 



```
CONFIG.YAML 


IN_PATH : PATH of your input image 
OUT_PATH : PATH of encrypted file 
INVERSE_PATH : PATH OF DECRYPTER FILE 
IV_PATH : PATH TO INITIALIZE VECTOR 
KEY_PATH : PATH TO KEY

```


#### Decryption 


Decryption part is very simple, but I decided to omit image saving part because 
storing data in memory is the most important part. 
So, assuming that you have you data stored and proper defined in ```config``` file. 


```
import numpy as np 
from src import Cryptor, Decryptor 
from src.utils import read_key, read_config 


def main():

	
	config = read_config('config/config.yaml')	
	path = config['OUT_PATH']
	outpath = config['INVERSE_PATH']
	_key = read_key(config['KEY_PATH'])
	_iv = read_key(config['IV_PATH'])
	size = (258, 258, 3)	
	decr = Decryptor(path = path, outname = outpath, create = False, _key = _key, _iv = _iv)

	dect._write_data()

	# You should store image size if you want to return data in np. like format 
	_obj = np.frombuffer(decr._decrypt(), dtype = np.uint8).rehspae(size)


```


To dos:

	- FastAPI like inference
	- Add module to pytorch dataloader

