---
title: "mdiobus_read_nested(9)"
name: "mdiobus_read_nested"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mdiobus_read_nested/"
description: "mdiobus_read_nested – Nested version of the mdiobus_read function"
---

<p>mdiobus_read_nested &#8211; Nested version of the mdiobus_read function</p>
<h2>Synopsis</h2>
<pre><code>int mdiobus_read_nested(struct mii_bus *bus, int addr, u32 regnum);</code></pre>
<h2>Arguments</h2>
<p><i>bus</i></p>
<dl>
<dd>
<dd>the mii_bus struct</dl>
<p> <i>addr</i></p>
<dl>
<dd>the phy address</dl>
<p> <i>regnum</i></p>
<dl>
<dd>register number to read</dl>
<h2>Description</h2>
<p>In case of nested MDIO bus access avoid lockdep false positives by using <code>mutex_lock_nested</code>.</p>
<h2>Note</h2>
<p>MUST NOT be called from interrupt context, because the bus read/write functions may wait for an interrupt to conclude the operation.</p>
<h2>Copyright</h2>
