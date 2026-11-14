---
title: "usb_remove_hcd(9)"
name: "usb_remove_hcd"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_remove_hcd/"
description: "usb_remove_hcd – shutdown processing for generic HCDs"
---

<p>usb_remove_hcd &#8211; shutdown processing for generic HCDs</p>
<h2>Synopsis</h2>
<pre><code>void usb_remove_hcd(struct usb_hcd *hcd);</code></pre>
<h2>Arguments</h2>
<p><i>hcd</i></p>
<dl>
<dd>
<dd>the usb_hcd structure to remove</dl>
<h2>Context</h2>
<p>!<code>in_interrupt</code></p>
<h2>Description</h2>
<p>Disconnects the root hub, then reverses the effects of <code>usb_add_hcd</code>, invoking the HCD&#8217;s <code>stop</code> method.</p>
<h2>Copyright</h2>
