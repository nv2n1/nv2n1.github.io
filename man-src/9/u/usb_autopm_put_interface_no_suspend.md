---
title: "usb_autopm_put_interface_no_suspend(9)"
name: "usb_autopm_put_interface_no_suspend"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_autopm_put_interface_no_suspend/"
---

usb_autopm_put_interface_no_suspend - decrement a USB interface's PM-usage counter

<h2>Synopsis</h2>

<pre><code>void usb_autopm_put_interface_no_suspend(struct usb_interface *intf);</code></pre>

<h2>Arguments</h2>

<i>intf</i>
<dl><dd><dd>the usb_interface whose counter should be decremented</dl>

<h2>Description</h2>

This routine decrements <i>intf</i>'s usage counter but does not carry out an autosuspend. 

 This routine can run in atomic context.

<h2>Copyright</h2>


