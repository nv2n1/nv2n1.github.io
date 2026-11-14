---
title: "current_time(9)"
name: "current_time"
section: "9"
letter: "c"
url: "/docs/linux/man/9-current_time/"
---

current_time - Return FS time

<h2>Synopsis</h2>

<pre><code>struct timespec current_time(struct inode *inode);</code></pre>

<h2>Arguments</h2>

<i>inode</i>
<dl><dd><dd>inode.</dl>

<h2>Description</h2>

Return the current time truncated to the time granularity supported by the fs. 

 Note that inode and inode-&gt;sb cannot be NULL. Otherwise, the function warns and returns time without truncation.

<h2>Copyright</h2>


