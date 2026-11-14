---
title: "usb_init_urb(9)"
name: "usb_init_urb"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_init_urb/"
description: "usb_init_urb – initializes a urb so that it can be used by a USB driver"
---

<p>usb_init_urb &#8211; initializes a urb so that it can be used by a USB driver</p>
<h2>Synopsis</h2>
<pre><code>void usb_init_urb(struct urb *urb);</code></pre>
<h2>Arguments</h2>
<p><i>urb</i></p>
<dl>
<dd>
<dd>pointer to the urb to initialize</dl>
<h2>Description</h2>
<p>Initializes a urb so that the USB subsystem can use it properly. </p>
<p> If a urb is created with a call to <code>usb_alloc_urb</code> it is not necessary to call this function. Only use this if you allocate the space for a struct urb on your own. If you call this function, be careful when freeing the memory for your urb that it is no longer in use by the USB core. </p>
<p> Only use this function if you _really_ understand what you are doing.</p>
<h2>Copyright</h2>
