---
title: "mdiobus_write(9)"
name: "mdiobus_write"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mdiobus_write/"
---

mdiobus_write - Convenience function for writing a given MII mgmt register

<h2>Synopsis</h2>

<pre><code>int mdiobus_write(struct mii_bus *bus, int addr, u32 regnum, u16 val);</code></pre>

<h2>Arguments</h2>

<i>bus</i>
<dl><dd><dd>the mii_bus struct</dl>
 

 <i>addr</i>
<dl><dd>the phy address</dl>
 

 <i>regnum</i>
<dl><dd>register number to write</dl>
 

 <i>val</i>
<dl><dd>value to write to <i>regnum</i></dl>

<h2>Note</h2>

MUST NOT be called from interrupt context, because the bus read/write functions may wait for an interrupt to conclude the operation.

<h2>Copyright</h2>


