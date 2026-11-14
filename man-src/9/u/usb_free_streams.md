---
title: "usb_free_streams(9)"
name: "usb_free_streams"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_free_streams/"
---

usb_free_streams - free bulk endpoint stream IDs.

<h2>Synopsis</h2>

<pre><code>int usb_free_streams(struct usb_interface *interface, struct usb_host_endpoint **eps, unsigned int num_eps, gfp_t mem_flags);</code></pre>

<h2>Arguments</h2>

<i>interface</i>
<dl><dd><dd>alternate setting that includes all endpoints.</dl>
 

 <i>eps</i>
<dl><dd>array of endpoints to remove streams from.</dl>
 

 <i>num_eps</i>
<dl><dd>number of endpoints in the array.</dl>
 

 <i>mem_flags</i>
<dl><dd>flags hcd should use to allocate memory.</dl>

<h2>Description</h2>

Reverts a group of bulk endpoints back to not using stream IDs. Can fail if we are given bad arguments, or HCD is broken.

<h2>Return</h2>

0 on success. On failure, a negative error code.

<h2>Copyright</h2>


