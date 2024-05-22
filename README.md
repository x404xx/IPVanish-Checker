<div align="center">

<img src="assets/logo.png" width="250" height="auto">

**IPVanish-Checker** is an IPVanish validity account checker.

</div>

## **Installation**

**Using** _`poetry`_

```
git clone https://github.com/x404xx/IPVanish-Checker.git
cd IPVanish-Checker
poetry shell
poetry install
```

**Using** _`pip`_

```
git clone https://github.com/x404xx/IPVanish-Checker.git
cd IPVanish-Checker
virtualenv env
env/scripts/activate
pip install -r requirements.txt
```

## Usage

```
usage: python -m vchecker [-h] -e EMAIL -p PASSWORD

IPVanish validity account checker.

options:
  -h, --help            show this help message and exit
  -e EMAIL, --email EMAIL
                        Email address of IPVanish account.
  -p PASSWORD, --password PASSWORD
                        Password of IPVanish account.
```

## Usage Example

```bash
python -m vchecker -e 'example@example.com' -p '123456'
```

## **Legal Disclaimer**

> [!Note]
> This was made for educational purposes only, nobody which directly involved in this project is responsible for any damages caused. **_You are responsible for your actions._**
