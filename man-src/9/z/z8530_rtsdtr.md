---
title: "z8530_rtsdtr(9)"
name: "z8530_rtsdtr"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_rtsdtr/"
description: "z8530_rtsdtr – Control the outgoing DTS/RTS line"
---

<p>z8530_rtsdtr &#8211; Control the outgoing DTS/RTS line</p>
<h2>Synopsis</h2>
<pre><code>void z8530_rtsdtr(struct z8530_channel *c, int set);</code></pre>
<h2>Arguments</h2>
<p><i>c</i></p>
<dl>
<dd>
<dd>The Z8530 channel to control;</dl>
<p> <i>set</i></p>
<dl>
<dd>1 to set, 0 to clear</dl>
<h2>Description</h2>
<p>Sets or clears DTR/RTS on the requested line. All locking is handled by the caller. For now we assume all boards use the actual RTS/DTR on the chip. Apparently one or two don&#8217;t. We&#8217;ll scream about them later.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
