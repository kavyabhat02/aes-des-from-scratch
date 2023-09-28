## AESDESecure

Yep, the package is named so because I like puns. 

### Usage:

#### Build
From the root of this repository, run: <br>
`python3 setup.py bdist_wheel`

#### Install
A wheel file is created in the `dist` folder that is created after the build. Install the library using: <br>
`pip install /path/to/<name of wheel file>.whl`

#### Import and use!
Add these lines to your code: <br>
```
import AESDESecure
```

Use the library functions you require, for example:
```
des_encrypted = AESDESecure.des("plaintext", "key")
```
will give you the encrypted binary for the word "plaintext" using DES.

##### To-Do:
1. Add support for AES and DES modes 
2. Document method usage