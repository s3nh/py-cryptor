import numpy as np 
import pathlib

from Crypto.Cipher import AES
from Crypto import Random 
from typing import Union 
from pathlib import Path
from PIL import Image
from typing import TypeVar

Rd = TypeVar('Rd')

class Cryptor(object):

    def __init__(self, path : str, outname : str , create: bool = True):
        self.path = path 
        self.outname = outname
        if create:
            self._key, self._iv = self._init_keyiv()
        else:
            self._key = kwargs.get('_key')
            self._iv = kwargs.get('_iv')
        self.cipher = self._crt_cipher()

    def read_image(self):
        """Read the image based on path argument

        Params
        ----------
        None

        Returns
        -----------
        in_data: np.array, 

        shape: Tuples
            Shape of processed image.
        """
        in_data = np.asarray( Image.open(self.path) )
        return in_data

    def read_data(self):
        """
        Read data (crypted or encrypted)
        """
        infile = open(self.path, 'rb')
        data = infile.read()
        infile.close()
        return data

    def write_data(self):
        encfile = open(self.outname, 'wb')
        encfile.write(self.enc_data)
        encfile.close() 

    def initialize_keys(self) -> Union[Rd, Rd]:
        """ Initialize key and initialize vector
        """
        _key = Random.new().read(AES.block_size)
        _iv = Random.new().read(AES.block_size)
        return _key, _iv

    def create_cipher(self, algo : str = 'AES'):
        """Create new cipher
           with predefined algorithm name.

        Params
        ----------

        algo: str
            Algorithm name (#TODO list it)

        Returns
        ----------
        _cipher: Any
        """
        tmp_ciph = getatr(Crypto.Cipher, algo)
        _cipher = tmp_ciph.new(self._key, AES.MODE_CFB, self._iv)
        return _cipher

class Encryptor(Cryptor):
    def __init__(self, path, outname, create, **kwargs):
        super().__init__(path, outname, create, **kwargs)
        self.data = self._read_image()
        self.enc_data = self._encrypt()

    def _encrypt(self):
        return self.cipher.encrypt(self.data) 

class Decryptor(Cryptor):

    def __init__(self, path, outname, create, **kwargs):
        super().__init__(path, outname, create, **kwargs)
        self.data = self._read_data() 
        self.dec_data = self._decrypt()

    def _decrypt(self):
        return self.cipher.decrypt(self.data)    

    def _get_numpy(self):
       return np.frombuffer(self.dec_data, dtype = np.uint8).reshape()