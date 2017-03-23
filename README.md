# github_navigator
A tiny github repository search tool

This program queries the github API search with a search term, fetches the response and shows it at the following URL:
localhost:9876/navigator?search_term=%term%


<b>Installation</b>

command-line: 
(done outside the project root)
1) create a virtualenv (if virtualenv not installed run pip install virtualenv)
```
virtualenv -p /usr/bin/python2.7 github_navigator_env
```

2) activate it
```
source ./github_navigator_env/bin/activate
```

3) install the requirements
```
pip install -r github_navigator/requirements.txt
```

4) run application.py
```
python github_navigator/application.py
```

5) open a browser and go to localhost:9876/navigator?search_term=arrow
