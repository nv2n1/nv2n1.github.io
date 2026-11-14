---
title: "ipc_free(9)"
name: "ipc_free"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ipc_free/"
description: "ipc_free – free ipc space"
---

<p>ipc_free &#8211; free ipc space</p>
<h2>Synopsis</h2>
<pre><code>void ipc_free(void *ptr);</code></pre>
<h2>Arguments</h2>
<p><i>ptr</i></p>
<dl>
<dd>
<dd>pointer returned by ipc_alloc</dl>
<h2>Description</h2>
<p>Free a block created with <code>ipc_alloc</code>.</p>
<h2>Copyright</h2>
