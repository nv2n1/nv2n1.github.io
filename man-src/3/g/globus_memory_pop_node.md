---
title: "globus_memory_pop_node(3)"
name: "globus_memory_pop_node"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_memory_pop_node/"
description: "Memory Pool –"
---

<h2 class="name">NAME</h2>
<p> Memory Pool &#8211; </p>
<h3>Functions</h3>
<p> <code>globus_bool_t</code> <code>globus_memory_init</code> (globus_memory_t *mem_info, int node_size, int node_count)<br />
 <i>Initialize memory pool. </i><br />
 void * <code>globus_memory_pop_node</code> (globus_memory_t *mem_info)<br />
 <i>Retrieve a memory item from a pool. </i><br />
 <code>globus_bool_t</code> <code>globus_memory_push_node</code> (globus_memory_t *mem_info, void *buffer)<br />
 <i>Return a memory item to the pool. </i><br />
 <code>globus_bool_t</code> <code>globus_memory_destroy</code> (globus_memory_t *mem_info)<br />
 <i>Destroy a memory pool. </i></p>
<h2>Detailed Description</h2>
<p> The globus_memory abstraction implements a memory management pool for groups of same-sized data items.</p>
<h2>Function Documentation</h2>
<h3><code>globus_bool_t</code> globus_memory_destroy (globus_memory_t *mem_info)</h3>
<p> Destroy a memory pool. Free all the memory associated with the memory management structure. For every call to <code>globus_memory_init()</code> there should be a call to <code>globus_memory_destroy()</code> or else memory will leak.</p>
<h3><code>globus_bool_t</code> globus_memory_init (globus_memory_t *mem_info, intnode_size, intnode_count)</h3>
<p> Initialize memory pool. Initialize the globus memory management structure. </p>
<p> Before using any functions associate with a memory structure this function must be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>mem_info</i> The memory management datatype<br />
 <i>node_size</i> The size of the memory to allocated with each pop.<br />
 <i>node_count</i> The initial number of nodes allocated with the memory management structure. If it is exceeded more will be allocated.</dl>
<h3>void* globus_memory_pop_node (globus_memory_t *mem_info)</h3>
<p> Retrieve a memory item from a pool. Pop a chunk of memory out of the memory management structure. Similar to malloc(). When no longer using this item, return it to the pool via <code>globus_memory_push_node()</code>.</p>
<h3><code>globus_bool_t</code> globus_memory_push_node (globus_memory_t *mem_info, void *buffer)</h3>
<p> Return a memory item to the pool. Push a chunk of memory back into the memory management structure. Similar to free().</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAJ">Author</a></p>
<dd></dl>
