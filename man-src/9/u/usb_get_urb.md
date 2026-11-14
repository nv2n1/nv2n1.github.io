---
title: "usb_get_urb(9)"
name: "usb_get_urb"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_get_urb/"
---

usb_get_urb - increments the reference count of the urb

<h2>Synopsis</h2>

<pre><code>struct urb *usb_get_urb(struct urb *urb);</code></pre>

<h2>Arguments</h2>

<i>urb</i>
<dl><dd><dd>pointer to the urb to modify, may be NULL</dl>

<h2>Description</h2>

This must be called whenever a urb is transferred from a device driver to a host controller driver. This allows proper reference counting to happen for urbs.

<h2>Return</h2>

A pointer to the urb with the incremented reference counter.

<h2>Copyright</h2>


