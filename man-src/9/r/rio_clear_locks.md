---
title: "rio_clear_locks(9)"
name: "rio_clear_locks"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_clear_locks/"
description: "rio_clear_locks – Release all host locks and signal enumeration complete"
---

<p>rio_clear_locks &#8211; Release all host locks and signal enumeration complete</p>
<h2>Synopsis</h2>
<pre><code>int rio_clear_locks(struct rio_net *net);</code></pre>
<h2>Arguments</h2>
<p><i>net</i></p>
<dl>
<dd>
<dd>RIO network to run on</dl>
<h2>Description</h2>
<p>Marks the component tag CSR on each device with the enumeration complete flag. When complete, it then release the host locks on each device. Returns 0 on success or <code>-EINVAL</code> on failure.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
