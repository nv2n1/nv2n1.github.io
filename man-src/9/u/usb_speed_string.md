---
title: "usb_speed_string(9)"
name: "usb_speed_string"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_speed_string/"
---

usb_speed_string - Returns human readable-name of the speed.

<h2>Synopsis</h2>

<pre><code>const char *usb_speed_string(enum usb_device_speed speed);</code></pre>

<h2>Arguments</h2>

<i>speed</i>
<dl><dd><dd>The speed to return human-readable name for. If it's not any of the speeds defined in usb_device_speed enum, string for USB_SPEED_UNKNOWN will be returned.</dl>

<h2>Copyright</h2>


