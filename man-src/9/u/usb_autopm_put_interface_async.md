---
title: "usb_autopm_put_interface_async(9)"
name: "usb_autopm_put_interface_async"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_autopm_put_interface_async/"
description: "usb_autopm_put_interface_async – decrement a USB interface’s PM-usage counter"
---

<p>usb_autopm_put_interface_async &#8211; decrement a USB interface&#8217;s PM-usage counter</p>
<h2>Synopsis</h2>
<pre><code>void usb_autopm_put_interface_async(struct usb_interface *intf);</code></pre>
<h2>Arguments</h2>
<p><i>intf</i></p>
<dl>
<dd>
<dd>the usb_interface whose counter should be decremented</dl>
<h2>Description</h2>
<p>This routine does much the same thing as <code>usb_autopm_put_interface</code>: It decrements <i>intf</i>&#8216;s usage counter and schedules a delayed autosuspend request if the counter is &lt;= 0. The difference is that it does not perform any synchronization; callers should hold a private lock and handle all synchronization issues themselves. </p>
<p> Typically a driver would call this routine during an URB&#8217;s completion handler, if no more URBs were pending. </p>
<p> This routine can run in atomic context.</p>
<h2>Copyright</h2>
