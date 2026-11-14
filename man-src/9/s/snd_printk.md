---
title: "snd_printk(9)"
name: "snd_printk"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_printk/"
description: "snd_printk – printk wrapper"
---

<p>snd_printk &#8211; printk wrapper</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>snd_printk(</code><i>fmt</i><code>, </code><i>&#8230;</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>fmt</i></p>
<dl>
<dd>
<dd>format string</dl>
<p> <i>&#8230;</i></p>
<dl>
<dd>variable arguments</dl>
<h2>Description</h2>
<p>Works like <code>printk</code> but prints the file and the line of the caller when configured with CONFIG_SND_VERBOSE_PRINTK.</p>
<h2>Copyright</h2>
