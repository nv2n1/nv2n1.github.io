---
title: "rio_enum_mport(9)"
name: "rio_enum_mport"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_enum_mport/"
description: "rio_enum_mport – Start enumeration through a master port"
---

<p>rio_enum_mport &#8211; Start enumeration through a master port</p>
<h2>Synopsis</h2>
<pre><code>int rio_enum_mport(struct rio_mport *mport, u32 flags);</code></pre>
<h2>Arguments</h2>
<p><i>mport</i></p>
<dl>
<dd>
<dd>Master port to send transactions</dl>
<p> <i>flags</i></p>
<dl>
<dd>Enumeration control flags</dl>
<h2>Description</h2>
<p>Starts the enumeration process. If somebody has enumerated our master port device, then give up. If not and we have an active link, then start recursive peer enumeration. Returns <code>0</code> if enumeration succeeds or <code>-EBUSY</code> if enumeration fails.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
