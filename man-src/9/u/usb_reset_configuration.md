---
title: "usb_reset_configuration(9)"
name: "usb_reset_configuration"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_reset_configuration/"
description: "usb_reset_configuration – lightweight device reset"
---

<p>usb_reset_configuration &#8211; lightweight device reset</p>
<h2>Synopsis</h2>
<pre><code>int usb_reset_configuration(struct usb_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the device whose configuration is being reset</dl>
<h2>Description</h2>
<p>This issues a standard SET_CONFIGURATION request to the device using the current configuration. The effect is to reset most USB-related state in the device, including interface altsettings (reset to zero), endpoint halts (cleared), and endpoint state (only for bulk and interrupt endpoints). Other usbcore state is unchanged, including bindings of usb device drivers to interfaces. </p>
<p> Because this affects multiple interfaces, avoid using this with composite (multi-interface) devices. Instead, the driver for each interface may use <code>usb_set_interface</code> on the interfaces it claims. Be careful though; some devices don&#8217;t support the SET_INTERFACE request, and others won&#8217;t reset all the interface state (notably endpoint state). Resetting the whole configuration would affect other drivers&#8217; interfaces. </p>
<p> The caller must own the device lock.</p>
<h2>Return</h2>
<p>Zero on success, else a negative error code.</p>
<h2>Copyright</h2>
