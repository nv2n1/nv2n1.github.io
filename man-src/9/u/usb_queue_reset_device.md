---
title: "usb_queue_reset_device(9)"
name: "usb_queue_reset_device"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_queue_reset_device/"
description: "usb_queue_reset_device – Reset a USB device from an atomic context"
---

<p>usb_queue_reset_device &#8211; Reset a USB device from an atomic context</p>
<h2>Synopsis</h2>
<pre><code>void usb_queue_reset_device(struct usb_interface *iface);</code></pre>
<h2>Arguments</h2>
<p><i>iface</i></p>
<dl>
<dd>
<dd>USB interface belonging to the device to reset</dl>
<h2>Description</h2>
<p>This function can be used to reset a USB device from an atomic context, where <code>usb_reset_device</code> won&#8217;t work (as it blocks). </p>
<p> Doing a reset via this method is functionally equivalent to calling <code>usb_reset_device</code>, except for the fact that it is delayed to a workqueue. This means that any drivers bound to other interfaces might be unbound, as well as users from usbfs in user space. </p>
<p> Corner cases: </p>
<p> &#8211; Scheduling two resets at the same time from two different drivers attached to two different interfaces of the same device is possible; depending on how the driver attached to each interface handles -&gt;<code>pre_reset</code>, the second reset might happen or not. </p>
<p> &#8211; If the reset is delayed so long that the interface is unbound from its driver, the reset will be skipped. </p>
<p> &#8211; This function can be called during .<code>probe</code>. It can also be called during .<code>disconnect</code>, but doing so is pointless because the reset will not occur. If you really want to reset the device during .<code>disconnect</code>, call <code>usb_reset_device</code> directly &#8212; but watch out for nested unbinding issues!</p>
<h2>Copyright</h2>
