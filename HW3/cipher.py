from sys import argv, exit
import re

try:
  assert len(argv) == 4
except AssertionError:
  print "Usage: python cipher.py INPUT NED OUTPUT"
  exit()

with open(argv[1], 'r') as fin, \
  open(argv[2], 'r') as NED, \
  open(argv[3], 'w') as fout:
  
  N_E = NED.readline().split(" ")
  N, e = int(N_E[0]), int(N_E[1])
  
  for line in fin:
    line = line.rstrip()
    pack = []
    for char in line:
      if len(pack) == 4:
        plain = pakc[0]*(2**24)+
      else:
        pack.append(char)
