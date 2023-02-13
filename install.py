import sys
from pathlib import Path
import shutil

match sys.argv[1:]:
    case [installdir, app]:
        recursive = False
    case ["-r", installdir, app]:
        recursive = True
    case _:
        print("Error: wrong usage")
        print("\tpython install.py [-r] installdir app")
        sys.exit(1)
print(f"Will install <{app}> in <{installdir}> (recursive mode: {recursive})")

installdirPath = Path(installdir)
appPath = Path(app)

# check installdir
if not installdirPath.exists():
    installdirPath.mkdir(parents=True, exist_ok=True)
elif not installdirPath.is_dir():
    print(f"Error: {installdir} n'est pas un répertoire")
    print("\tpython install.py [-r] installdir app")
    sys.exit(2)

# check application to install
if appPath.is_file():
    print('File will be deploy:', appPath)
    shutil.copy(appPath, installdir)
elif appPath.is_dir() and recursive:
    print('Directory will be deploy recursively:', appPath)
    shutil.copytree(appPath, installdir, dirs_exist_ok=True)
else:
    print(f"Error: {appPath} n'est pas un fichier ou répertoire en mode récursif")
    print("\tpython install.py [-r] installdir app")
    sys.exit(2)
print('Done')


