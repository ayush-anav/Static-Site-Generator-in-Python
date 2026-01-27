# from textnode import * 
# def main():
#     dummy = TextNode("Dummy text node, inline", "link", "https://www.google.com.fj")
#     print(dummy)
    
# main()

import shutil
import os
try:
    shutil.rmtree("public")
    shutil.copytree("static", "public")
except:
    print("missing public folder!")
    print("creating one")
    os.mkdir("public")
    print("run the program again :)")