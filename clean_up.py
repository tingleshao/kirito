import os

test = True

os.system("rm *.jpg")
os.system("rm *.txt")
os.system("rm *.pto")
os.system("rm -r old_order_images")

if test:
    os.system("cp ~/dev/kirito/*.py .")
    os.system("cp /Users/chongshao/data/20170328173507/*.jpg .")
    os.system("cp ~/dev/kirito/*.cpp .")
    os.system("g++ -ggdb feature_finder.cpp -o feature_finder `pkg-config --cflags --libs opencv`")
