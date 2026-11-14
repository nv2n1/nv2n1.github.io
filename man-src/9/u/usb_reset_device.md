---
title: "usb_reset_device(9)"
name: "usb_reset_device"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_reset_device/"
description: "usb_reset_device – warn interface drivers and perform a USB port reset"
---

<p>usb_reset_device &#8211; warn interface drivers and perform a USB port reset</p>
<h2>Synopsis</h2>
<pre><code>int usb_reset_device(struct usb_device *udev);</code></pre>
<h2>Arguments</h2>
<p><i>udev</i></p>
<dl>
<dd>
<dd>device to reset (not in SUSPENDED or NOTATTACHED state)</dl>
<h2>Description</h2>
<p>Warns all drivers bound to registered interfaces (using their pre_reset method), performs the port reset, and then lets the drivers know that the reset is over (using their post_reset method).</p>
<h2>Return</h2>
<p>The same as for <code>usb_reset_and_verify_device</code>.</p>
<h2>Note</h2>
<p>The caller must own the device lock. For example, it&#8217;s safe to use this from a driver <code>probe</code> routine after downloading new firmware. For calls that might not occur during <code>probe</code>, drivers should lock the device using <code>usb_lock_device_for_reset</code>. </p>
<p> If an interface is currently being probed or disconnected, we assume its driver knows how to handle resets. For all other interfaces, if the driver doesn&#8217;t have pre_reset and post_reset methods then we attempt to unbind it and rebind afterward.</p>
<h2>Copyright</h2>
