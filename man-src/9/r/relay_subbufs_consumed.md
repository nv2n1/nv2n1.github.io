---
title: "relay_subbufs_consumed(9)"
name: "relay_subbufs_consumed"
section: "9"
letter: "r"
url: "/docs/linux/man/9-relay_subbufs_consumed/"
---

relay_subbufs_consumed - update the buffer's sub-buffers-consumed count

<h2>Synopsis</h2>

<pre><code>void relay_subbufs_consumed(struct rchan *chan, unsigned int cpu, size_t subbufs_consumed);</code></pre>

<h2>Arguments</h2>

<i>chan</i>
<dl><dd><dd>the channel</dl>
 

 <i>cpu</i>
<dl><dd>the cpu associated with the channel buffer to update</dl>
 

 <i>subbufs_consumed</i>
<dl><dd>number of sub-buffers to add to current buf's count</dl>

<h2>Description</h2>

Adds to the channel buffer's consumed sub-buffer count. subbufs_consumed should be the number of sub-buffers newly consumed, not the total consumed. 

 NOTE. Kernel clients don't need to call this function if the channel mode is 'overwrite'.

<h2>Copyright</h2>


