import os

challenges = [folder.name for folder in os.scandir('./src/challs') if folder.is_dir()]

print(challenges)
