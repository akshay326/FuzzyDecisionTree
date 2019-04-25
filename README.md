# Decision Tree Program
**Python3** implementation of ID3 algorithm based on categorical datasets.

![Sample Decision Tree](https://drive.google.com/uc?export=view&id=1VMyTxclWMfpgkgHBshep_koCPaoyPHOJ)

## Features
+ The tree is created using ``DecisionTree.py`` file. 
+ Its implementation of **ID3 algorithm** and returns the resulting tree as a multi-dimensional dictionary.
+ Works on **categorical datasets only**.
+ Unpredictable outputs are denoted by **?**
+ Added ``DrawTree.py`` to generate decision tree **png image** using ``pyDot`` library 


## Installation
+ Open the terminal or command prompt. Head for the directory with source code
+ *PyDot* package is based on *GraphViz*. Get the instructions to install it [here](https://emden.github.io/download/)
+ Install python requirements: 
```
pip install -r requirements.txt
```


## Sample Output
Output of Test Cases:   

**Weather.csv**

| Entry | Output |
-------|------
entry1 | no  
entry2 | no
entry3 | yes
entry4 | yes
entry5 | no

**Vote.csv**

| Entry | Output |
-------|------
entry1 | democrat
entry2 | democrat
entry3 | republican
entry4 | democrat
entry5 | democrat  

**Soybean.csv**

| Entry | Output |
-------|------
entry1 | ?
entry2 | frog-eye-leaf-spot
entry3 | frog-eye-leaf-spot
entry4 | brown-spot
entry5 | ?


## Contributing
Feel free to leave any comments (as issues) or make suggestions (as a pull request). 
