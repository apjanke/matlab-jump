import glob
import os.path
import re
import subprocess

def maybeMakedirs(dir):
  if not os.path.exists(dir):
    os.makedirs(dir)

jarDir = "opp/javadoc"
htmlDir = "javadocs"
indexFile = htmlDir + "/index.html"

maybeMakedirs(htmlDir)

fIndex = open(indexFile, 'w')
indexHead = """<html>
<body>

<h2>Java Libraries shipped with Matlab R2019b</h2>

<ul>
"""
fIndex.write(indexHead)

jars = glob.glob(jarDir + "/*.jar")
jars.sort()
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
  fIndex.write(f'  <li><a href="{lib}/index.html">{lib}</a></li>\n')

indexTail = """
</ul>

</body>
</html>
"""
fIndex.close()

