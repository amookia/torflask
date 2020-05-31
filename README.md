# torflask
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.png?v=103)](https://opensource.org/licenses/mit-license.php)

*Flask 🌶️ | Tor 🧅 | Gunicorn🦄  | Docker🐳 | Fandogh 🌰*

# Run on fandogh
```bash
git clone https://github.com/amookia/torflask.git
cd torflask
fandogh image init --name torflask
fandogh image publish --version 1
fandogh service deploy --name torflask --version 1
```

# Usage
**Receive .onion from /domain**
```bash
amookia@ubuntu:~$ curl https://domain/link
nenogybaaac6ffocthfwimcwo6gyapslpalsplaszmwi6ngy6wad.onion
```

# Essential files and folders
* Dockerfile
* install/


## License
[MIT](https://choosealicense.com/licenses/mit/)
