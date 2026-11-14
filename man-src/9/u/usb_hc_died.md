---
title: "usb_hc_died(9)"
name: "usb_hc_died"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_hc_died/"
---

usb_hc_died - report abnormal shutdown of a host controller (bus glue)

<h2>Synopsis</h2>

<pre><code>void usb_hc_died(struct usb_hcd *hcd);</code></pre>

<h2>Arguments</h2>

<i>hcd</i>
<dl><dd><dd>pointer to the HCD representing the controller</dl>

<h2>Description</h2>

This is called by bus glue to report a USB host controller that died while operations may still have been pending. It's called automatically by the PCI glue, so only glue for non-PCI busses should need to call it. 

 Only call this function with the primary HCD.

<h2>Copyright</h2>


