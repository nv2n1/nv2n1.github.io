---
title: "maple_driver_register(9)"
name: "maple_driver_register"
section: "9"
letter: "m"
url: "/docs/linux/man/9-maple_driver_register/"
description: "maple_driver_register – register a maple driver"
---

<p>maple_driver_register &#8211; register a maple driver</p>
<h2>Synopsis</h2>
<pre><code>int maple_driver_register(struct maple_driver *drv);</code></pre>
<h2>Arguments</h2>
<p><i>drv</i></p>
<dl>
<dd>
<dd>maple driver to be registered.</dl>
<h2>Description</h2>
<p>Registers the passed in <i>drv</i>, while updating the bus type. Devices with matching function IDs will be automatically probed.</p>
<h2>Author</h2>
<p><code>Paul Mundt</code> &lt;lethal [at] linux-sh.org&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
