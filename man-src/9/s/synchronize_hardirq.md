---
title: "synchronize_hardirq(9)"
name: "synchronize_hardirq"
section: "9"
letter: "s"
url: "/docs/linux/man/9-synchronize_hardirq/"
description: "synchronize_hardirq – wait for pending hard IRQ handlers (on other CPUs)"
---

<p>synchronize_hardirq &#8211; wait for pending hard IRQ handlers (on other CPUs)</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool synchronize_hardirq(unsigned int&nbsp;<wbr></code><i>irq</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>irq</i></p>
<dl>
<dd>
<dd>interrupt number to wait for</dl>
<h2>Description</h2>
<p>This function waits for any pending hard IRQ handlers for this interrupt to complete before returning. If you use this function while holding a resource the IRQ handler may need you will deadlock. It does not take associated threaded handlers into account. </p>
<p> Do not use this for shutdown scenarios where you must be sure that all parts (hardirq and threaded handler) have completed.</p>
<h2>Return</h2>
<p>false if a threaded handler is active. </p>
<p> This function may be called &#8211; with care &#8211; from IRQ context.</p>
<h2>Copyright</h2>
