class Node:
    l = None
    r = None
    genue = None
    

def count(l, r):
    l_prob = get_prob(l)
    r_prob = get_prob(r)
    a_set = set().union(l_prob.keys(), r_prob.keys())
    res = dict()
    for key in a_set:
        val_l = 0
        val_r = 0
        if key in l_prob:
            val_l = l_prob[key]
        if key in r_prob:
            val_r = r_prob[key]
        res.update({key: (val_r + val_l) / 2.0})
    return res
            
            
def get_prob(n):
    if n.genue is not None:
        if n.genue[0] == n.genue[1]:
            return {n.genue[0]:1.0}
        else:
            return {n.genue[0]:0.5, n.genue[1]:0.5}
    else:
        return count(n.l, n.r)
        
root = Node()
root.l = Node()
root.r = Node()
root.l.l = Node()
root.l.r = Node()
root.l.l.genue = ["A", "a"]
root.l.r.genue = ["a", "A"]
root.r.genue = ["a", "A"]



probs = get_prob(root)
keys = list(probs.keys())
if len(keys) == 2:
    print(keys[0]+keys[1], probs[keys[0]]*probs[keys[1]]*2)
    print(keys[1]+keys[1], probs[keys[1]]*probs[keys[1]])
print(keys[0]+keys[0], probs[keys[0]]*probs[keys[0]])
