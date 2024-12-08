# To test, use the command line: pipenv run python -m spkb.keyswitch

from . import mx_keyswitch

print("Rendering mx_keyswitch() to mx_keyswitch.scad...")
mx_keyswitch().save_as_scad("mx_keyswitch.scad")
