---
title: "z8530_write_port(9)"
name: "z8530_write_port"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_write_port/"
description: "z8530_write_port – Architecture specific interface function"
---

<p>z8530_write_port &#8211; Architecture specific interface function</p>
<h2>Synopsis</h2>
<pre><code>void z8530_write_port(unsigned long p, u8 d);</code></pre>
<h2>Arguments</h2>
<p><i>p</i></p>
<dl>
<dd>
<dd>port to write</dl>
<p> <i>d</i></p>
<dl>
<dd>value to write</dl>
<h2>Description</h2>
<p>Write a value to a port with delays if need be. Note that the caller must hold locks to avoid read/writes from other contexts violating the 5uS rule </p>
<p> In the longer term this should become an architecture specific section so that this can become a generic driver interface for all platforms. For now we only handle PC I/O ports with or without the dread 5uS sanity delay.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
