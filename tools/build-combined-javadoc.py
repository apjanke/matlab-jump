import glob
import os.path
import re
import subprocess

def maybeMakedirs(dir):
  if not os.path.exists(dir):
    os.makedirs(dir)

jarDir = "opp/javadoc"
htmlDir = "javadocs"

maybeMakedirs(htmlDir)

jars = glob.glob(jarDir + "/*.jar")
for jar in jars:
  file = os.path.basename(jar)
  base = os.path.splitext(file)
  base = base[0]
  lib = re.compile('-javadoc').sub("", base)
  print("Extracting " + lib)
  htmlSubdir = htmlDir + "/" + lib
  maybeMakedirs(htmlSubdir)
  os.chdir(htmlSubdir)
  subprocess.run(["jar", "xf", "../../opp/javadoc/"+file ])
  os.chdir("../..")
