---
title: "rio_destid_next(9)"
name: "rio_destid_next"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_destid_next/"
description: "rio_destid_next – return next destID in use"
---

<p>rio_destid_next &#8211; return next destID in use</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u16 rio_destid_next(struct rio_net&nbsp;<wbr>*&nbsp;<wbr></code><i>net</i><code>, u16&nbsp;<wbr></code><i>from</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>net</i></p>
<dl>
<dd>
<dd>RIO network</dl>
<p> <i>from</i></p>
<dl>
<dd>destination ID from which search shall continue</dl>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
