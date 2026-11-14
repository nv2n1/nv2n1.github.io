---
title: "usb_enable_autosuspend(9)"
name: "usb_enable_autosuspend"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_enable_autosuspend/"
---

usb_enable_autosuspend - allow a USB device to be autosuspended

<h2>Synopsis</h2>

<pre><code>void usb_enable_autosuspend(struct usb_device *udev);</code></pre>

<h2>Arguments</h2>

<i>udev</i>
<dl><dd><dd>the USB device which may be autosuspended</dl>

<h2>Description</h2>

This routine allows <i>udev</i> to be autosuspended. An autosuspend won't take place until the autosuspend_delay has elapsed and all the other necessary conditions are satisfied. 

 The caller must hold <i>udev</i>'s device lock.

<h2>Copyright</h2>


