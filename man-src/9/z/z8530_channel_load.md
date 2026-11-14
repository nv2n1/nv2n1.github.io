---
title: "z8530_channel_load(9)"
name: "z8530_channel_load"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_channel_load/"
description: "z8530_channel_load – Load channel data"
---

<p>z8530_channel_load &#8211; Load channel data</p>
<h2>Synopsis</h2>
<pre><code>int z8530_channel_load(struct z8530_channel *c, u8 *rtable);</code></pre>
<h2>Arguments</h2>
<p><i>c</i></p>
<dl>
<dd>
<dd>Z8530 channel to configure</dl>
<p> <i>rtable</i></p>
<dl>
<dd>table of register, value pairs FIXME: ioctl to allow user uploaded tables</dl>
<h2>Description</h2>
<p>Load a Z8530 channel up from the system data. We use +16 to indicate the &#8220;prime&#8221; registers. The value 255 terminates the table.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
