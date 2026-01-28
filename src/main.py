# from textnode import * 
# def main():
#     dummy = TextNode("Dummy text node, inline", "link", "https://www.google.com.fj")
#     print(dummy)
    
# main()

import shutil
import os
from gencontent import generate_page

dir_path_content = "./content"
dir_path_public = "./public"
template_path = "./template.html"

try:
    shutil.rmtree("public")
    shutil.copytree("static", "public")

except:
    print("missing public folder!")
    print("creating one")
    
    os.mkdir("public")
    print("run the program again :)")

print("Generating page...")
generate_page(
    os.path.join(dir_path_content, "index.md"),
    template_path,
    os.path.join(dir_path_public, "index.html"),
)