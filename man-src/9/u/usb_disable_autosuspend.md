---
title: "usb_disable_autosuspend(9)"
name: "usb_disable_autosuspend"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_disable_autosuspend/"
---

usb_disable_autosuspend - prevent a USB device from being autosuspended

<h2>Synopsis</h2>

<pre><code>void usb_disable_autosuspend(struct usb_device *udev);</code></pre>

<h2>Arguments</h2>

<i>udev</i>
<dl><dd><dd>the USB device which may not be autosuspended</dl>

<h2>Description</h2>

This routine prevents <i>udev</i> from being autosuspended and wakes it up if it is already autosuspended. 

 The caller must hold <i>udev</i>'s device lock.

<h2>Copyright</h2>


