# 二叉树
from treelib import Tree

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
        print(f"\n插入值 {value} 后的树结构：")
        self.print_tree()

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def print_tree(self):
        if self.root is None:
            print("树为空")
            return
        
        # 使用treelib创建可视化树
        visual_tree = Tree()
        self._build_visual_tree(self.root, visual_tree)
        visual_tree.show()

    def _build_visual_tree(self, node, visual_tree, parent=None, is_left=None):
        if node is None:
            return
        
        # 为每个节点创建唯一标识
        node_id = str(id(node))
        
        # 添加节点标签，标明是左子树还是右子树
        if parent is None:
            visual_tree.create_node(f"[根]{node.value}", node_id)
        else:
            position = "L" if is_left else "R"
            visual_tree.create_node(f"[{position}]{node.value}", node_id, parent=parent)
        
        # 递归构建左右子树
        self._build_visual_tree(node.left, visual_tree, node_id, True)
        self._build_visual_tree(node.right, visual_tree, node_id, False)

    # 前序遍历
    # 遍历顺序：根节点 -> 左子树 -> 右子树
    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    # 中序遍历
    # 遍历顺序：左子树 -> 根节点 -> 右子树
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    # 后序遍历
    # 遍历顺序：左子树 -> 右子树 -> 根节点
    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    # 查找节点
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

# 示例用法
if __name__ == "__main__":
    # 创建二叉树
    tree = BinaryTree()
    
    # 插入节点
    values = [5, 3, 7, 2, 4, 6, 8]
    print("开始构建二叉树...")
    for value in values:
        tree.insert(value)
    
    # 打印各种遍历结果
    print("\n遍历结果：")
    print("前序遍历:", tree.preorder_traversal())
    print("中序遍历:", tree.inorder_traversal())
    print("后序遍历:", tree.postorder_traversal())
    
    # 搜索节点
    print("\n搜索测试：")
    search_values = [4, 9]
    for value in search_values:
        if tree.search(value):
            print(f"值 {value} 存在于树中")
        else:
            print(f"值 {value} 不存在于树中") 