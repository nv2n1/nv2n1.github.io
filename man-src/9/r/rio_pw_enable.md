---
title: "rio_pw_enable(9)"
name: "rio_pw_enable"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_pw_enable/"
description: "rio_pw_enable – Enables/disables port-write handling by a master port"
---

<p>rio_pw_enable &#8211; Enables/disables port-write handling by a master port</p>
<h2>Synopsis</h2>
<pre><code>void rio_pw_enable(struct rio_mport *mport, int enable);</code></pre>
<h2>Arguments</h2>
<p><i>mport</i></p>
<dl>
<dd>
<dd>Master port associated with port-write handling</dl>
<p> <i>enable</i></p>
<dl>
<dd>1=enable, 0=disable</dl>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
