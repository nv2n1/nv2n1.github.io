---
title: "usb_autopm_get_interface(9)"
name: "usb_autopm_get_interface"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_autopm_get_interface/"
description: "usb_autopm_get_interface – increment a USB interface’s PM-usage counter"
---

<p>usb_autopm_get_interface &#8211; increment a USB interface&#8217;s PM-usage counter</p>
<h2>Synopsis</h2>
<pre><code>int usb_autopm_get_interface(struct usb_interface *intf);</code></pre>
<h2>Arguments</h2>
<p><i>intf</i></p>
<dl>
<dd>
<dd>the usb_interface whose counter should be incremented</dl>
<h2>Description</h2>
<p>This routine should be called by an interface driver when it wants to use <i>intf</i> and needs to guarantee that it is not suspended. In addition, the routine prevents <i>intf</i> from being autosuspended subsequently. (Note that this will not prevent suspend events originating in the PM core.) This prevention will persist until <code>usb_autopm_put_interface</code> is called or <i>intf</i> is unbound. A typical example would be a character-device driver when its device file is opened. </p>
<p> <i>intf</i>&#8216;s usage counter is incremented to prevent subsequent autosuspends. However if the autoresume fails then the counter is re-decremented. </p>
<p> This routine can run only in process context.</p>
<h2>Return</h2>
<p>0 on success.</p>
<h2>Copyright</h2>
