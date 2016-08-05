class abr_search:
    
    def __init__(self, tree, val)
    	self.tree = tree
        self.val = val
    def run()
    	ptr = self.tree.root
    	if ptr.value = val
        	return val
        elif val < ptr.value
        	return abr_search(ptr.left, val)
        else
        	return abr_search(ptr.right, val)