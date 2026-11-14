---
title: "usb_autopm_get_interface_no_resume(9)"
name: "usb_autopm_get_interface_no_resume"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_autopm_get_interface_no_resume/"
---

usb_autopm_get_interface_no_resume - increment a USB interface's PM-usage counter

<h2>Synopsis</h2>

<pre><code>void usb_autopm_get_interface_no_resume(struct usb_interface *intf);</code></pre>

<h2>Arguments</h2>

<i>intf</i>
<dl><dd><dd>the usb_interface whose counter should be incremented</dl>

<h2>Description</h2>

This routine increments <i>intf</i>'s usage counter but does not carry out an autoresume. 

 This routine can run in atomic context.

<h2>Copyright</h2>


