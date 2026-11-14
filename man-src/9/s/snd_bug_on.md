---
title: "snd_bug_on(9)"
name: "snd_bug_on"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_bug_on/"
description: "snd_BUG_ON – debugging check macro"
---

<p>snd_BUG_ON &#8211; debugging check macro</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>snd_BUG_ON(</code><i>cond</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>cond</i></p>
<dl>
<dd>
<dd>condition to evaluate</dl>
<h2>Description</h2>
<p>Has the same behavior as WARN_ON when CONFIG_SND_DEBUG is set, otherwise just evaluates the conditional and returns the value.</p>
<h2>Copyright</h2>
