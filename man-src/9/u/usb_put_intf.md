---
title: "usb_put_intf(9)"
name: "usb_put_intf"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_put_intf/"
---

usb_put_intf - release a use of the usb interface structure

<h2>Synopsis</h2>

<pre><code>void usb_put_intf(struct usb_interface *intf);</code></pre>

<h2>Arguments</h2>

<i>intf</i>
<dl><dd><dd>interface that's been decremented</dl>

<h2>Description</h2>

Must be called when a user of an interface is finished with it. When the last user of the interface calls this function, the memory of the interface is freed.

<h2>Copyright</h2>


