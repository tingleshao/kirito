# kirito

### You should have Hugin installed in your system, and you should current be in a directory with a runnable compiled feature_finder cpp program.

### To use the tool, first compile the opencv feature finder program in the current directory:
```bash
g++ -ggdb feature_finder.cpp -o feature_finder `pkg-config --cflags --libs opencv`
```

### Then type
```bash
python3 automatic_with_opencv.py [threshold for matching: recommend 0.1]
```

### for example:
```bash
python3 automatic_with_opencv.py 0.1
```
