---
title: "usb_autopm_put_interface(9)"
name: "usb_autopm_put_interface"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_autopm_put_interface/"
description: "usb_autopm_put_interface – decrement a USB interface’s PM-usage counter"
---

<p>usb_autopm_put_interface &#8211; decrement a USB interface&#8217;s PM-usage counter</p>
<h2>Synopsis</h2>
<pre><code>void usb_autopm_put_interface(struct usb_interface *intf);</code></pre>
<h2>Arguments</h2>
<p><i>intf</i></p>
<dl>
<dd>
<dd>the usb_interface whose counter should be decremented</dl>
<h2>Description</h2>
<p>This routine should be called by an interface driver when it is finished using <i>intf</i> and wants to allow it to autosuspend. A typical example would be a character-device driver when its device file is closed. </p>
<p> The routine decrements <i>intf</i>&#8216;s usage counter. When the counter reaches 0, a delayed autosuspend request for <i>intf</i>&#8216;s device is attempted. The attempt may fail (see <code>autosuspend_check</code>). </p>
<p> This routine can run only in process context.</p>
<h2>Copyright</h2>
