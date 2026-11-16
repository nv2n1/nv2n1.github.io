---
title: "snd_printdd(9)"
name: "snd_printdd"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_printdd/"
description: "snd_printdd – debug printk"
---

<p>snd_printdd &#8211; debug printk</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>snd_printdd(</code><i>format</i><code>, </code><i>&#8230;</i><code>);</code></dt></dl>
<h2>Arguments</h2>
<p><i>format</i></p>
<dl>
<dd>
</dd><dd>format string</dd></dl>
<p> <i>&#8230;</i></p>
<dl>
<dd>variable arguments</dd></dl>
<h2>Description</h2>
<p>Works like <code>snd_printk</code> for debugging purposes. Ignored when CONFIG_SND_DEBUG_VERBOSE is not set.</p>
<h2>Copyright</h2>
