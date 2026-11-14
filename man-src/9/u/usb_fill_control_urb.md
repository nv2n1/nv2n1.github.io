---
title: "usb_fill_control_urb(9)"
name: "usb_fill_control_urb"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_fill_control_urb/"
---

usb_fill_control_urb - initializes a control urb

<h2>Synopsis</h2>

<pre><code>void usb_fill_control_urb(struct urb *urb, struct usb_device *dev, unsigned int pipe, unsigned char *setup_packet, void *transfer_buffer, int buffer_length, usb_complete_t complete_fn, void *context);</code></pre>

<h2>Arguments</h2>

<i>urb</i>
<dl><dd><dd>pointer to the urb to initialize.</dl>
 

 <i>dev</i>
<dl><dd>pointer to the struct usb_device for this urb.</dl>
 

 <i>pipe</i>
<dl><dd>the endpoint pipe</dl>
 

 <i>setup_packet</i>
<dl><dd>pointer to the setup_packet buffer</dl>
 

 <i>transfer_buffer</i>
<dl><dd>pointer to the transfer buffer</dl>
 

 <i>buffer_length</i>
<dl><dd>length of the transfer buffer</dl>
 

 <i>complete_fn</i>
<dl><dd>pointer to the usb_complete_t function</dl>
 

 <i>context</i>
<dl><dd>what to set the urb context to.</dl>

<h2>Description</h2>

Initializes a control urb with the proper information needed to submit it to a device.

<h2>Copyright</h2>


