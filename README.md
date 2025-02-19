# Matam Course Wet Ex. 5

## Run this command on CSL3 terminals

Must run to setup git tmp dir

```bash
export TMPDIR=~/tmp
```

## Compile

```bash
python3 ex5.py
python3 test.py
```

## zip and final check

```bash
zip ex5.zip ex5.py
/home/mtm/public/2324a/ex5/finalcheck ex5.zip
```

## Tests README

All of the tests were randomly generated!   

If you notice any mistakes send me a message / open an issue in github or you can make pull request.    

Good Luck!


### Steps:
1. Change directory to Tests, and Move/Copy your 'ex5.py' to the Tests folder

```
cd ./Tests cp ../ex5.py ./ex5.py
```

2. Run [testRun.py](testRun.py) using your IDE or using ```python3 testRun.py```

3. You'll get a summary in the console and an 'output.txt' file with details in mere seconds :)

___

- To turn off Failed Tests printing in 'output.txt' go to line 24 and comment it

- TO turn on Passed Tests printing in 'output.txt' go to line 22 and uncomment it

* If you want to turn off a folder of tests, comment the the corresponding lines in the main function. Each folder is initialized with a path so it can be easily identified.

**~Clean up**: if you want to remove your outputs from the folders, use the 'cleanUp.py' script provided. 
can be used by IDE or ```python3 cleanUp.py```


### Tests Explanation
The supplied tests **ONLY** test the *loadEncryptionSystem(...)* function.  
There are dummy files with the targeted files to make sure only the wanted ones are being encrypted/decrypted.

Each folder is meant to test a different functionality:

caesar - encrypting files using caesar

caesar_enc\<i> - decrypting files using caesar, each folder with a different key

vigenere - encrypting files using vigenere

vigenere_encrypted - decrypting files using vigenere

___

The keys in each folder don't match the ones in other folders, i.e each folder is complelety independent

***-Error Files-*** are the files metioned before to test that no other files are being encrypted/decrypted
