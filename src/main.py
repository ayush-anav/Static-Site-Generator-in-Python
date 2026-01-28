# from textnode import * 
# def main():
#     dummy = TextNode("Dummy text node, inline", "link", "https://www.google.com.fj")
#     print(dummy)
    
# main()

import shutil
import os
import sys 

from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_content = "./content"
dir_path_public = "./docs"
template_path = "./template.html"
default_basepath = "/"

try:
    shutil.rmtree("docs")
    shutil.copytree("static", "docs")

except:
    print("missing public folder!")
    print("creating one")
    
    os.mkdir("docs")
    print("run the program again :)")


basepath = default_basepath
if len(sys.argv) > 1:
    basepath = sys.argv[1]
        
print("Generating page...")
generate_pages_recursive(
    os.path.join(dir_path_content),
    template_path,
    dir_path_public,
    basepath
)