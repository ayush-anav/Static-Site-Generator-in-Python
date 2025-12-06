# Split Delimiter
#### We want to take a text node like `this is `code` stuff` and make it:
```py
    txt = "this is `code` stuff"
    turn_to = [
        TextNode("this is ", TextNode.TEXT),
        TextNode("code", TextNode.CODE),
        TextNode(" stuff", TextNode.TEXT),
    ]
```

---

## Approach:
- Take our **old_nodes list, iterate over them**. 
- *Take delimiter*.
- Take text_type for our *special delimiter* e.g **`** = **TextType.CODE**

## Pseudo Code
- If node.text_type != TextType.TEXT: (then its plain text, just append to new_list) `new_list.append(node)`

- Split the 
```py 
    node.text.split(delimiter) 
    if len(parts) % 2 == 0:
            raise Exception("invalid md")


    ["text has split", "but maybe only 1 delimiter was given instead of 2"]
    # THAT's why throw ERROR.
```
- Start a for loop for i in range(len(parts))

- Create a temporary list **`tmp_list = []`**, then for every even index using a **modulo operator**, append to `tmp_list` and for **index 1**, append `tmp_list.append(TextNode(parts[i], text_type))`

- Return that list

---
# Walkthrough
![code walkthrough](/project-notes/imgs/delimiter_walkthrough.png)

---

# Idea
![code idea](/project-notes/imgs/delimiter_idea.png)

---