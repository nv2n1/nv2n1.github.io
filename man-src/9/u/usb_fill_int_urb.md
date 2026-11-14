---
title: "usb_fill_int_urb(9)"
name: "usb_fill_int_urb"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_fill_int_urb/"
---

usb_fill_int_urb - macro to help initialize a interrupt urb

<h2>Synopsis</h2>

<pre><code>void usb_fill_int_urb(struct urb *urb, struct usb_device *dev, unsigned int pipe, void *transfer_buffer, int buffer_length, usb_complete_t complete_fn, void *context, int interval);</code></pre>

<h2>Arguments</h2>

<i>urb</i>
<dl><dd><dd>pointer to the urb to initialize.</dl>
 

 <i>dev</i>
<dl><dd>pointer to the struct usb_device for this urb.</dl>
 

 <i>pipe</i>
<dl><dd>the endpoint pipe</dl>
 

 <i>transfer_buffer</i>
<dl><dd>pointer to the transfer buffer</dl>
 

 <i>buffer_length</i>
<dl><dd>length of the transfer buffer</dl>
 

 <i>complete_fn</i>
<dl><dd>pointer to the usb_complete_t function</dl>
 

 <i>context</i>
<dl><dd>what to set the urb context to.</dl>
 

 <i>interval</i>
<dl><dd>what to set the urb interval to, encoded like the endpoint descriptor's bInterval value.</dl>

<h2>Description</h2>

Initializes a interrupt urb with the proper information needed to submit it to a device. 

 Note that High Speed and SuperSpeed(+) interrupt endpoints use a logarithmic encoding of the endpoint interval, and express polling intervals in microframes (eight per millisecond) rather than in frames (one per millisecond). 

 Wireless USB also uses the logarithmic encoding, but specifies it in units of 128us instead of 125us. For Wireless USB devices, the interval is passed through to the host controller, rather than being translated into microframe units.

<h2>Copyright</h2>


