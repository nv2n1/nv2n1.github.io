---
title: "z8530_read_port(9)"
name: "z8530_read_port"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_read_port/"
description: "z8530_read_port – Architecture specific interface function"
---

<p>z8530_read_port &#8211; Architecture specific interface function</p>
<h2>Synopsis</h2>
<pre><code>int z8530_read_port(unsigned long p);</code></pre>
<h2>Arguments</h2>
<p><i>p</i></p>
<dl>
<dd>
<dd>port to read</dl>
<h2>Description</h2>
<p>Provided port access methods. The Comtrol SV11 requires no delays between accesses and uses PC I/O. Some drivers may need a 5uS delay </p>
<p> In the longer term this should become an architecture specific section so that this can become a generic driver interface for all platforms. For now we only handle PC I/O ports with or without the dread 5uS sanity delay. </p>
<p> The caller must hold sufficient locks to avoid violating the horrible 5uS delay rule.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
