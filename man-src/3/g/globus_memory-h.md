---
title: "globus_memory-h(3)"
name: "globus_memory-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_memory-h/"
description: "globus_memory.h –"
---

<p>globus_memory.h &#8211; </p>
<p> Memory Pool.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_types.h&#8217;<br />
 #include &#8216;globus_module.h&#8217;<br />
 #include &#8216;globus_thread.h&#8217; </p>
<h3>Functions</h3>
<p><code>globus_bool_t</code> <code>globus_memory_init</code> (globus_memory_t *mem_info, int node_size, int node_count)<br />
 <i>Initialize memory pool. </i><br />
 void * <code>globus_memory_pop_node</code> (globus_memory_t *mem_info)<br />
 <i>Retrieve a memory item from a pool. </i><br />
 <code>globus_bool_t</code> <code>globus_memory_push_node</code> (globus_memory_t *mem_info, void *buf)<br />
 <i>Return a memory item to the pool. </i><br />
 <code>globus_bool_t</code> <code>globus_memory_destroy</code> (globus_memory_t *mem_info)<br />
 <i>Destroy a memory pool. </i></p>
<h2>Detailed Description</h2>
<p>Memory Pool. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_common from the source code.</p>
