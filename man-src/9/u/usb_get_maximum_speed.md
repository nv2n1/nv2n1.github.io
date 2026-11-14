---
title: "usb_get_maximum_speed(9)"
name: "usb_get_maximum_speed"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_get_maximum_speed/"
description: "usb_get_maximum_speed – Get maximum requested speed for a given USB controller."
---

<p>usb_get_maximum_speed &#8211; Get maximum requested speed for a given USB controller.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>enum usb_device_speed usb_get_maximum_speed(struct device&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Pointer to the given USB controller device</dl>
<h2>Description</h2>
<p>The function gets the maximum speed string from property &#8220;maximum-speed&#8221;, and returns the corresponding enum usb_device_speed.</p>
<h2>Copyright</h2>
