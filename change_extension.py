from PIL import Image
import os

root = "/home/dissana8/Naturalistic-Adversarial-Patch/eval_output/LAB_0.2/"
for path, subdirs, files in os.walk(root):
    for name in files:
        print(os.path.join(path, name))
        if name.endswith(".png"):
            im = Image.open(os.path.join(path, name))
            name=name.split('.')[0] + 'jpg'
            rgb_im = im.convert('RGB')
            rgb_im.save(os.path.join(path, name))
            # c+=1
            # print(os.path.join(directory, filename))
            continue
        else:
            continue