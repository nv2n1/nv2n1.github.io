---
title: "snd_printd(9)"
name: "snd_printd"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_printd/"
description: "snd_printd – debug printk"
---

<p>snd_printd &#8211; debug printk</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>snd_printd(</code><i>fmt</i><code>, </code><i>&#8230;</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>fmt</i></p>
<dl>
<dd>
<dd>format string</dl>
<p> <i>&#8230;</i></p>
<dl>
<dd>variable arguments</dl>
<h2>Description</h2>
<p>Works like <code>snd_printk</code> for debugging purposes. Ignored when CONFIG_SND_DEBUG is not set.</p>
<h2>Copyright</h2>
