---
title: "usb_for_each_dev(9)"
name: "usb_for_each_dev"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_for_each_dev/"
---

usb_for_each_dev - iterate over all USB devices in the system

<h2>Synopsis</h2>

<pre><code>int usb_for_each_dev(void *data, int (*fn)(struct usb_device *, void *));</code></pre>

<h2>Arguments</h2>

<i>data</i>
<dl><dd><dd>data pointer that will be handed to the callback function</dl>
 

 <i>fn</i>
<dl><dd>callback function to be called for each USB device</dl>

<h2>Description</h2>

Iterate over all USB devices and call <i>fn</i> for each, passing it <i>data</i>. If it returns anything other than 0, we break the iteration prematurely and return that value.

<h2>Copyright</h2>


