---
title: "usb_reset_endpoint(9)"
name: "usb_reset_endpoint"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_reset_endpoint/"
---

usb_reset_endpoint - Reset an endpoint's state.

<h2>Synopsis</h2>

<pre><code>void usb_reset_endpoint(struct usb_device *dev, unsigned int epaddr);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>the device whose endpoint is to be reset</dl>
 

 <i>epaddr</i>
<dl><dd>the endpoint's address. Endpoint number for output, endpoint number + USB_DIR_IN for input</dl>

<h2>Description</h2>

Resets any host-side endpoint state such as the toggle bit, sequence number or current window.

<h2>Copyright</h2>


