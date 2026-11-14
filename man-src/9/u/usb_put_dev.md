---
title: "usb_put_dev(9)"
name: "usb_put_dev"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_put_dev/"
---

usb_put_dev - release a use of the usb device structure

<h2>Synopsis</h2>

<pre><code>void usb_put_dev(struct usb_device *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device that's been disconnected</dl>

<h2>Description</h2>

Must be called when a user of a device is finished with it. When the last user of the device calls this function, the memory of the device is freed.

<h2>Copyright</h2>


