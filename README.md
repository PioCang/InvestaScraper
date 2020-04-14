# InvestaScraper

1. Install Python
2. Install __virtualenv__. You may need to install-uninstall-reinstall if needed.
```
sudo pip install virtualenv
```
3. Create a virtualenv then source it to enter it.
```
virtualenv --python=/usr/bin/python3.5 my_env
source my_env/bin/activate
```
To check if activation was successful,
```
which python; which python3
```
should point to a directory other than _/usr/bin/python/_

4. Install __selenium__
```
sudo pip install selenium
```
5. Download __geckodriver__ and put it in
```
/path/to/(my_env)/bin/
```
6. Run your Python script. 

7. When you're done, run
```
deactivate
```

