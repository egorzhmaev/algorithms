import re
strs = ["vxOoOoVvx","abBa","AbBa"]
for target in strs:
     modtarg = re.sub(r"(?-i:([a-zA-Z])(?!\1)(?i:\1))", "", target)
     print( target, "\t-->  (", len(modtarg), ") ", modtarg )