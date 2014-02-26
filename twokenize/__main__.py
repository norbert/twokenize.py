import sys
from . import tokenize

if __name__=='__main__':
  for line in sys.stdin:
    print u" ".join(tokenize(line[:-1])).encode('utf-8')
