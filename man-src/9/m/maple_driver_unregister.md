---
title: "maple_driver_unregister(9)"
name: "maple_driver_unregister"
section: "9"
letter: "m"
url: "/docs/linux/man/9-maple_driver_unregister/"
description: "maple_driver_unregister – unregister a maple driver."
---

<p>maple_driver_unregister &#8211; unregister a maple driver.</p>
<h2>Synopsis</h2>
<pre><code>void maple_driver_unregister(struct maple_driver *drv);</code></pre>
<h2>Arguments</h2>
<p><i>drv</i></p>
<dl>
<dd>
<dd>maple driver to unregister.</dl>
<h2>Description</h2>
<p>Cleans up after <code>maple_driver_register</code>. To be invoked in the exit path of any module drivers.</p>
<h2>Author</h2>
<p><code>Paul Mundt</code> &lt;lethal [at] linux-sh.org&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
