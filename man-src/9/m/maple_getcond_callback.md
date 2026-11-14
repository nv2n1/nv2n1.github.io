---
title: "maple_getcond_callback(9)"
name: "maple_getcond_callback"
section: "9"
letter: "m"
url: "/docs/linux/man/9-maple_getcond_callback/"
description: "maple_getcond_callback – setup handling MAPLE_COMMAND_GETCOND"
---

<p>maple_getcond_callback &#8211; setup handling MAPLE_COMMAND_GETCOND</p>
<h2>Synopsis</h2>
<pre><code>void maple_getcond_callback(struct maple_device *dev, void (*callback)(struct mapleq *mq), unsigned long interval, unsigned long function);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device responding</dl>
<p> <i>callback</i></p>
<dl>
<dd>handler callback</dl>
<p> <i>interval</i></p>
<dl>
<dd>interval in jiffies between callbacks</dl>
<p> <i>function</i></p>
<dl>
<dd>the function code for the device</dl>
<h2>Author</h2>
<p><code>Paul Mundt</code> &lt;lethal [at] linux-sh.org&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
