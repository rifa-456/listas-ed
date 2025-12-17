from src.tree_map import TreeMap


class AVLTreeMap(TreeMap):
    """Sorted map implementation using an AVL tree."""

    # -------------------- nested _Node class --------------------
    class _Node(TreeMap._Node):
        """Node class for AVL maintains height value for balancing."""

        __slots__ = "_height"

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._height = 0

    def _recompute_height(self, p):
        """Recompute the height of position p based on its children's heights."""
        node = self._validate(p)
        node._height = 1 + max(self._height(self.left(p)), self._height(self.right(p)))

    def _isbalanced(self, p):
        """Return True if position p has balance factor between -1 and 1."""
        return abs(self._height(self.left(p)) - self._height(self.right(p))) <= 1

    def _height(self, p):
        """Return the height of the subtree rooted at Position p."""
        if p is None:
            return 0
        else:
            return p._node._height

    def _tall_child(self, p, favorleft=False):
        """Return the taller child of p (favor left child if heights are equal)."""
        if self._height(self.left(p)) + (1 if favorleft else 0) > self._height(
            self.right(p)
        ):
            return self.left(p)
        else:
            return self.right(p)

    def _tall_grandchild(self, p):
        """Return the taller grandchild of p, favoring alignment for tie-breaking."""
        child = self._tall_child(p)
        alignment = child == self.left(p)
        return self._tall_child(child, alignment)

    def _rebalance(self, p):
        """Rebalance the tree starting at position p and moving upward."""
        while p is not None:
            old_height = self._height(p)
            if not self._isbalanced(p):
                p = self._restructure(self._tall_grandchild(p))
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
            self._recompute_height(p)
            if self._height(p) == old_height:
                p = None
            else:
                p = self.parent(p)

    def _rebalance_insert(self, p):
        """Rebalance the tree after an insertion at position p."""
        self._rebalance(p)

    def _rebalance_delete(self, p):
        """Rebalance the tree after a deletion at position p."""
        self._rebalance(p)