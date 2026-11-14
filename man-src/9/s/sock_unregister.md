---
title: "sock_unregister(9)"
name: "sock_unregister"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sock_unregister/"
---

sock_unregister - remove a protocol handler

<h2>Synopsis</h2>

<pre><code>void sock_unregister(int family);</code></pre>

<h2>Arguments</h2>

<i>family</i>
<dl><dd><dd>protocol family to remove</dl>

<h2>Description</h2>

This function is called by a protocol handler that wants to remove its address family, and have it unlinked from the new socket creation. 

 If protocol handler is a module, then it can use module reference counts to protect against new references. If protocol handler is not a module then it needs to provide its own protection in the ops-&gt;create routine.

<h2>Copyright</h2>


