import sys
import tarfile
import os

tarball = os.path.abspath(sys.argv[1])
dirname = os.path.abspath(sys.argv[2])
if platform.system() == 'OS/390':
  os.system("cd %s && (iconv -f IBM-1047 -t ISO8859-1 %s | gunzip -c > temp.tar) && pax -ofrom=ISO8859-1,to=IBM-1047 -rf temp.tar" % (dirname, tarball))
else:
  tfile = tarfile.open(tarball,'r:gz');
  tfile.extractall(dirname)
sys.exit(0)
