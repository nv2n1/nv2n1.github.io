---
title: "find_next_best_node(9)"
name: "find_next_best_node"
section: "9"
letter: "f"
url: "/docs/linux/man/9-find_next_best_node/"
---

find_next_best_node - find the next node that should appear in a given node's fallback list

<h2>Synopsis</h2>

<pre><code>int find_next_best_node(int node, nodemask_t *used_node_mask);</code></pre>

<h2>Arguments</h2>

<i>node</i>
<dl><dd><dd>node whose fallback list we're appending</dl>
 

 <i>used_node_mask</i>
<dl><dd>nodemask_t of already used nodes</dl>

<h2>Description</h2>

We use a number of factors to determine which is the next node that should appear on a given node's fallback list. The node should not have appeared already in <i>node</i>'s fallback list, and it should be the next closest node according to the distance array (which contains arbitrary distance values from each node to each node in the system), and should also prefer nodes with no CPUs, since presumably they'll have very little allocation pressure on them otherwise. It returns -1 if no node is found.

<h2>Copyright</h2>


