---
title: "ibv_inc_rkey(3)"
name: "ibv_inc_rkey"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_inc_rkey/"
---

<h2 class="name">NAME</h2>
 

 

 ibv_inc_rkey - creates a new rkey from the given one 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/verbs.h&gt;
uint32_t ibv_inc_rkey(uint32_t rkey);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 ibv_inc_rkey() Increases the 8 LSB of rkey and returns the new value.

<h2>RETURN VALUE</h2>

 

 ibv_inc_rkey() returns the new rkey.

<h2>NOTES</h2>

 

 The verb generates a new rkey that is different from the previous one on its tag part but has the same index (bits 0xffffff00). A use case for this verb can be to create a new rkey from a Memory window's rkey when binding it to a Memory region.

<h2>AUTHORS</h2>

 

 Majd Dibbiny &lt;majd [at] mellanox.com&gt;, Yishai Hadas &lt;yishaih [at] mellanox.com&gt; 

<h2>Index</h2>


