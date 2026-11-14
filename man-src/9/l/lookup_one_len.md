---
title: "lookup_one_len(9)"
name: "lookup_one_len"
section: "9"
letter: "l"
url: "/docs/linux/man/9-lookup_one_len/"
---

lookup_one_len - filesystem helper to lookup single pathname component

<h2>Synopsis</h2>

<pre><code>struct dentry *lookup_one_len(const char *name, struct dentry *base, int len);</code></pre>

<h2>Arguments</h2>

<i>name</i>
<dl><dd><dd>pathname component to lookup</dl>
 

 <i>base</i>
<dl><dd>base directory to lookup from</dl>
 

 <i>len</i>
<dl><dd>maximum length <i>len</i> should be interpreted to</dl>

<h2>Description</h2>

Note that this routine is purely a helper for filesystem usage and should not be called by generic code. 

 The caller must hold base-&gt;i_mutex.

<h2>Copyright</h2>


