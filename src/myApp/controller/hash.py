import hashlib
mdp = 'mermoz'  # mot de passe à chiffrer
mdp = hashlib.sha256(mdp.encode())
mdpC = mdp.hexdigest()  # mot de passe chiffré
print(mdpC)
