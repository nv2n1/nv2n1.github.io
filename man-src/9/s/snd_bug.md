---
title: "snd_bug(9)"
name: "snd_bug"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_bug/"
description: "snd_BUG – give a BUG warning message and stack trace"
---

<p>snd_BUG &#8211; give a BUG warning message and stack trace</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>snd_BUG(void);</code></dl>
<h2>Arguments</h2>
<dd>None</p>
<h2>Description</h2>
<p>Calls <code>WARN</code> if CONFIG_SND_DEBUG is set. Ignored when CONFIG_SND_DEBUG is not set.</p>
<h2>Copyright</h2>
