# Leetcode
A Site that record the leetcode solution by us

## data_structure
### Already Done
* `linked_list`
* `binary_tree`
* `binary_tree_visualizer`: visualize binary tree using `graphviz`
* `binary_index_tree`

### Usage
```python

from data_structure import make_random_tree, make_tree
from data_structure import BinaryTreeVisualizer

val_list = make_random_tree()
root = make_tree(val_list)
BinaryTreeVisualizer().visualizer_tree(root)
```

