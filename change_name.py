import os
path = os.getcwd()
for root, dirs, files in os.walk(path):
    i = 609
    for file in files:
        if file.endswith(".jpg"):
            oldname = os.path.join(root, file)
            newname = "y" + str(i) + ".jpg"
            newname = os.path.join(root, newname)
            os.rename(oldname, newname)
            i += 1