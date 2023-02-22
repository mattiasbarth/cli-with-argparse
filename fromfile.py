import argparse

# the command python fromfile.py @args.txt won't work in
# windows powershell, but works fine in linux

parser = argparse.ArgumentParser(fromfile_prefix_chars="@")

parser.add_argument("one")
parser.add_argument("two")
parser.add_argument("three")

args = parser.parse_args()

print(args)