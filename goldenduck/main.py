import os
import goldenduck.pkg.config as config

c = config.load(os.getcwd()+"/conf.yaml")

print(c)