---
title: "disable_hardirq(9)"
name: "disable_hardirq"
section: "9"
letter: "d"
url: "/docs/linux/man/9-disable_hardirq/"
description: "disable_hardirq – disables an irq and waits for hardirq completion"
---

<p>disable_hardirq &#8211; disables an irq and waits for hardirq completion</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool disable_hardirq(unsigned int&nbsp;<wbr></code><i>irq</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>irq</i></p>
<dl>
<dd>
<dd>Interrupt to disable</dl>
<h2>Description</h2>
<p>Disable the selected interrupt line. Enables and Disables are nested. This function waits for any pending hard IRQ handlers for this interrupt to complete before returning. If you use this function while holding a resource the hard IRQ handler may need you will deadlock. </p>
<p> When used to optimistically disable an interrupt from atomic context the return value must be checked.</p>
<h2>Return</h2>
<p>false if a threaded handler is active. </p>
<p> This function may be called &#8211; with care &#8211; from IRQ context.</p>
<h2>Copyright</h2>
