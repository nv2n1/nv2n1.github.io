---
title: "phy_start_interrupts(9)"
name: "phy_start_interrupts"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_start_interrupts/"
---

phy_start_interrupts - request and enable interrupts for a PHY device

<h2>Synopsis</h2>

<pre><code>int phy_start_interrupts(struct phy_device *phydev);</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>target phy_device struct</dl>

<h2>Description</h2>

Request the interrupt for the given PHY. If this fails, then we set irq to PHY_POLL. Otherwise, we enable the interrupts in the PHY. This should only be called with a valid IRQ number. Returns 0 on success or &lt; 0 on error.

<h2>Copyright</h2>


