import os, time, shutil

paths = input("Enter your path please: ")

oneday = (time.time())- 1 * 86400

try:
    for path in paths:
        for filename in os.listdir(path):
            if os.path.getmtime(os.path.join(path, filename)) < oneday:
                if os.path.isfile(os.path.join(path, filename)):
                    print(filename)
                    os.remove(os.path.join(path, filename))
                elif os.path.isdir(os.path.join(path, filename)):
                    print(filename)
                    shutil.rmtree((os.path.join(path, filename)))
                    os.remove(os.path.join(path, filename))
except:
    pass
                
print("Maintenance Complete!")
