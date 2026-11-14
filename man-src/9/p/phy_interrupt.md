---
title: "phy_interrupt(9)"
name: "phy_interrupt"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_interrupt/"
description: "phy_interrupt – PHY interrupt handler"
---

<p>phy_interrupt &#8211; PHY interrupt handler</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>irqreturn_t phy_interrupt(int&nbsp;<wbr></code><i>irq</i><code>, void&nbsp;<wbr>*&nbsp;<wbr></code><i>phy_dat</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>irq</i></p>
<dl>
<dd>
<dd>interrupt line</dl>
<p> <i>phy_dat</i></p>
<dl>
<dd>phy_device pointer</dl>
<h2>Description</h2>
<p>When a PHY interrupt occurs, the handler disables interrupts, and schedules a work task to clear the interrupt.</p>
<h2>Copyright</h2>
