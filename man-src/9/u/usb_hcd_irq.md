---
title: "usb_hcd_irq(9)"
name: "usb_hcd_irq"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_hcd_irq/"
description: "usb_hcd_irq – hook IRQs to HCD framework (bus glue)"
---

<p>usb_hcd_irq &#8211; hook IRQs to HCD framework (bus glue)</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>irqreturn_t usb_hcd_irq(int&nbsp;<wbr></code><i>irq</i><code>, void&nbsp;<wbr>*&nbsp;<wbr></code><i>__hcd</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>irq</i></p>
<dl>
<dd>
<dd>the IRQ being raised</dl>
<p> <i>__hcd</i></p>
<dl>
<dd>pointer to the HCD whose IRQ is being signaled</dl>
<h2>Description</h2>
<p>If the controller isn&#8217;t HALTed, calls the driver&#8217;s irq handler. Checks whether the controller is now dead.</p>
<h2>Return</h2>
<p><code>IRQ_HANDLED</code> if the IRQ was handled. <code>IRQ_NONE</code> otherwise.</p>
<h2>Copyright</h2>
