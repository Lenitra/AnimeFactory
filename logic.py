from cryptography.fernet import Fernet
import yaml


# region Cryptage des données
secret_key = b'gZTtOPorjsy8tdTFeLWXKWqG9EcX1Ifd1oiaFDXgFFg='

def encode(message: str):
    key = secret_key
    message = bytes(message, "utf-8")
    return Fernet(key).encrypt(message)


def decode(token: bytes):
    key = secret_key
    return (Fernet(key).decrypt(token)).decode("utf-8")

# endregion


# Appelée pour register l'utilisateur
# Retourne :
# 0 si un champ est vide
# 1 si le mail est invalide
# 2 si le mail est déjà prit
# 3 si le pseudo est déjà prit
# 4 si le pseudo est pas conforme
# 5 si le mdp est pas conforme
# 255 enregistrement réussi !
def register(mail, mdp, pseudo):

    with open('data/accounts.yaml', encoding='utf8') as f:
        users = yaml.load(f, Loader=yaml.FullLoader)

    if mail == "" or mdp == "" or pseudo == "":
        return 0

    if "@" in mail:
        if "." in mail.split("@")[1]:
            pass
        else:
            return 2
    else:
        return 2

    for e in users:
        if e["mail"] == mail:
            return 2

    for e in users:
        if e["pseudo"] == pseudo:
            return 3

    if len(mdp) <= 5:
        return 5

    else:
        mdp = encode(mdp)
        users.append({"mail": mail, "mdp": mdp, "pseudo": pseudo})
        with open('data/accounts.yaml', 'w') as f:
            data = yaml.dump(users, f)

        user = 0

        with open(f'data/players/{pseudo}.yaml', 'w', encoding='utf8') as f:
            data = yaml.dump(user, f)
            
        return 255
