---
title: "usb_root_hub_lost_power(9)"
name: "usb_root_hub_lost_power"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_root_hub_lost_power/"
---

usb_root_hub_lost_power - called by HCD if the root hub lost Vbus power

<h2>Synopsis</h2>

<pre><code>void usb_root_hub_lost_power(struct usb_device *rhdev);</code></pre>

<h2>Arguments</h2>

<i>rhdev</i>
<dl><dd><dd>struct usb_device for the root hub</dl>

<h2>Description</h2>

The USB host controller driver calls this function when its root hub is resumed and Vbus power has been interrupted or the controller has been reset. The routine marks <i>rhdev</i> as having lost power. When the hub driver is resumed it will take notice and carry out power-session recovery for all the "USB-PERSIST"-enabled child devices; the others will be disconnected.

<h2>Copyright</h2>


