---
title: "usb_alloc_urb(9)"
name: "usb_alloc_urb"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_alloc_urb/"
description: "usb_alloc_urb – creates a new urb for a USB driver to use"
---

<p>usb_alloc_urb &#8211; creates a new urb for a USB driver to use</p>
<h2>Synopsis</h2>
<pre><code>struct urb *usb_alloc_urb(int iso_packets, gfp_t mem_flags);</code></pre>
<h2>Arguments</h2>
<p><i>iso_packets</i></p>
<dl>
<dd>
<dd>number of iso packets for this urb</dl>
<p> <i>mem_flags</i></p>
<dl>
<dd>the type of memory to allocate, see <code>kmalloc</code> for a list of valid options for this.</dl>
<h2>Description</h2>
<p>Creates an urb for the USB driver to use, initializes a few internal structures, increments the usage counter, and returns a pointer to it. </p>
<p> If the driver want to use this urb for interrupt, control, or bulk endpoints, pass &#8216;0&#8217; as the number of iso packets. </p>
<p> The driver must call <code>usb_free_urb</code> when it is finished with the urb.</p>
<h2>Return</h2>
<p>A pointer to the new urb, or <code>NULL</code> if no memory is available.</p>
<h2>Copyright</h2>
