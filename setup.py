__author__ = 'h'
import os
import sys

args = sys.argv[:]
args.insert(0, "python")
print args

for d in os.listdir("."):
    setup = os.path.join(d, "setup.py")
    if os.path.exists(setup):
        os.chdir(d)
        os.system(" ".join(args))
        os.chdir("..")

