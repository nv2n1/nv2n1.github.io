---
title: "rio_set_port_lockout(9)"
name: "rio_set_port_lockout"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_set_port_lockout/"
description: "rio_set_port_lockout – Sets/clears LOCKOUT bit (RIO EM 1.3) for a switch port."
---

<p>rio_set_port_lockout &#8211; Sets/clears LOCKOUT bit (RIO EM 1.3) for a switch port.</p>
<h2>Synopsis</h2>
<pre><code>int rio_set_port_lockout(struct rio_dev *rdev, u32 pnum, int lock);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>Pointer to RIO device control structure</dl>
<p> <i>pnum</i></p>
<dl>
<dd>Switch port number to set LOCKOUT bit</dl>
<p> <i>lock</i></p>
<dl>
<dd>Operation : set (=1) or clear (=0)</dl>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
