import os

challenges = [folder.name for folder in os.scandir('./amber/challs') if folder.is_dir()]

print(challenges)
