---
title: "usb_autopm_get_interface_async(9)"
name: "usb_autopm_get_interface_async"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_autopm_get_interface_async/"
description: "usb_autopm_get_interface_async – increment a USB interface’s PM-usage counter"
---

<p>usb_autopm_get_interface_async &#8211; increment a USB interface&#8217;s PM-usage counter</p>
<h2>Synopsis</h2>
<pre><code>int usb_autopm_get_interface_async(struct usb_interface *intf);</code></pre>
<h2>Arguments</h2>
<p><i>intf</i></p>
<dl>
<dd>
<dd>the usb_interface whose counter should be incremented</dl>
<h2>Description</h2>
<p>This routine does much the same thing as <code>usb_autopm_get_interface</code>: It increments <i>intf</i>&#8216;s usage counter and queues an autoresume request if the device is suspended. The differences are that it does not perform any synchronization (callers should hold a private lock and handle all synchronization issues themselves), and it does not autoresume the device directly (it only queues a request). After a successful call, the device may not yet be resumed. </p>
<p> This routine can run in atomic context.</p>
<h2>Return</h2>
<p>0 on success. A negative error code otherwise.</p>
<h2>Copyright</h2>
