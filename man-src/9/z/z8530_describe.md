---
title: "z8530_describe(9)"
name: "z8530_describe"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_describe/"
description: "z8530_describe – Uniformly describe a Z8530 port"
---

<p>z8530_describe &#8211; Uniformly describe a Z8530 port</p>
<h2>Synopsis</h2>
<pre><code>void z8530_describe(struct z8530_dev *dev, char *mapping, unsigned long io);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Z8530 device to describe</dl>
<p> <i>mapping</i></p>
<dl>
<dd>string holding mapping type (eg &#8220;I/O&#8221; or &#8220;Mem&#8221;)</dl>
<p> <i>io</i></p>
<dl>
<dd>the port value in question</dl>
<h2>Description</h2>
<p>Describe a Z8530 in a standard format. We must pass the I/O as the port offset isn&#8217;t predictable. The main reason for this function is to try and get a common format of report.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
