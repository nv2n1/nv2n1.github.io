---
title: "rio_enum_host(9)"
name: "rio_enum_host"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_enum_host/"
description: "rio_enum_host – Set host lock and initialize host destination ID"
---

<p>rio_enum_host &#8211; Set host lock and initialize host destination ID</p>
<h2>Synopsis</h2>
<pre><code>int rio_enum_host(struct rio_mport *port);</code></pre>
<h2>Arguments</h2>
<p><i>port</i></p>
<dl>
<dd>
<dd>Master port to issue transaction</dl>
<h2>Description</h2>
<p>Sets the local host master port lock and destination ID register with the host device ID value. The host device ID value is provided by the platform. Returns <code>0</code> on success or <code>-1</code> on failure.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
