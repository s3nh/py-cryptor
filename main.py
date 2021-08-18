import argparse
import os 
from src.crypto import Cryptor, Encryptor 
from src.utils import read_key
import typing 
from typing import List, Dict, Union, Optional 
import yaml 


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type = str, help = 'config path', default = 'config/config.yaml')
    args = parser.parse_args()
    return args

def read_config(path : str):
    assert os.path.exists(path), 'Path does not exist'
    
    with open(path, 'r') as confile:
        config = yaml.safe_load(confile)
    return config


def main():
    arg = args()
    config = read_config(arg.config)
    path = config['IN_PATH']
    outpath = config['OUT_PATH']
    invpath = config['INVERSE_PATH']
    _ivpath = config['IV_PATH']
    _keypath = config['KEY_PATH']

    
    _iv = read_key(_ivpath)
    _key = read_key(_keypath)

    
    encr = Encryptor(path = path, outname = outpath, create = False, _key = _key, _iv = _iv)

    _shape = encr.data.shape
    print(_shape) 
    encr._write_data()

    
if __name__ == "__main__":
    main()
