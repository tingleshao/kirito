import os

test = True

os.system("rm *.jpg")
os.system("rm *.txt")
os.system("rm *.pto")
os.system("rm -r old_order_images")

if test:
    os.system("cp ~/dev/kirito/*.py .")
    os.system("cp ~/dev/kirito/*.jpg .")
