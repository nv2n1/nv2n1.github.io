---
title: "mdiobus_read(9)"
name: "mdiobus_read"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mdiobus_read/"
---

mdiobus_read - Convenience function for reading a given MII mgmt register

<h2>Synopsis</h2>

<pre><code>int mdiobus_read(struct mii_bus *bus, int addr, u32 regnum);</code></pre>

<h2>Arguments</h2>

<i>bus</i>
<dl><dd><dd>the mii_bus struct</dl>
 

 <i>addr</i>
<dl><dd>the phy address</dl>
 

 <i>regnum</i>
<dl><dd>register number to read</dl>

<h2>Note</h2>

MUST NOT be called from interrupt context, because the bus read/write functions may wait for an interrupt to conclude the operation.

<h2>Copyright</h2>


