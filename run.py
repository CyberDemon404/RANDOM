import os, platform
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    from ran64 import sup
    sup()
elif bit == '32bit':
    from ran32 import sup
    sup()
