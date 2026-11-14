---
title: "mdiobus_release(9)"
name: "mdiobus_release"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mdiobus_release/"
---

mdiobus_release - mii_bus device release callback

<h2>Synopsis</h2>

<pre><code>void mdiobus_release(struct device *d);</code></pre>

<h2>Arguments</h2>

<i>d</i>
<dl><dd><dd>the target struct device that contains the mii_bus</dl>

<h2>Description</h2>

called when the last reference to an mii_bus is dropped, to free the underlying memory.

<h2>Copyright</h2>


