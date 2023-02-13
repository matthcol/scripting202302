import sys

match sys.argv[1:]:
    case [installdir, app]:
        recursive = False
    case ["-r", installdir, app]:
        recursive = True
    case _:
        print("Error: wrong usage")
        print("\tpython install.py [-r] installdir app")
        sys.exit(0)
print(f"Will install <{app}> in <{installdir}> (recursive mode: {recursive})")
