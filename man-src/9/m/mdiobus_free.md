---
title: "mdiobus_free(9)"
name: "mdiobus_free"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mdiobus_free/"
---

mdiobus_free - free a struct mii_bus

<h2>Synopsis</h2>

<pre><code>void mdiobus_free(struct mii_bus *bus);</code></pre>

<h2>Arguments</h2>

<i>bus</i>
<dl><dd><dd>mii_bus to free</dl>

<h2>Description</h2>

This function releases the reference to the underlying device object in the mii_bus. If this is the last reference, the mii_bus will be freed.

<h2>Copyright</h2>


