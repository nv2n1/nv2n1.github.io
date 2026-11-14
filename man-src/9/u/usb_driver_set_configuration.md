---
title: "usb_driver_set_configuration(9)"
name: "usb_driver_set_configuration"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_driver_set_configuration/"
---

usb_driver_set_configuration - Provide a way for drivers to change device configurations

<h2>Synopsis</h2>

<pre><code>int usb_driver_set_configuration(struct usb_device *udev, int config);</code></pre>

<h2>Arguments</h2>

<i>udev</i>
<dl><dd><dd>the device whose configuration is being updated</dl>
 

 <i>config</i>
<dl><dd>the configuration being chosen.</dl>

<h2>Context</h2>

In process context, must be able to sleep

<h2>Description</h2>

Device interface drivers are not allowed to change device configurations. This is because changing configurations will destroy the interface the driver is bound to and create new ones; it would be like a floppy-disk driver telling the computer to replace the floppy-disk drive with a tape drive! 

 Still, in certain specialized circumstances the need may arise. This routine gets around the normal restrictions by using a work thread to submit the change-config request.

<h2>Return</h2>

0 if the request was successfully queued, error code otherwise. The caller has no way to know whether the queued request will eventually succeed.

<h2>Copyright</h2>


