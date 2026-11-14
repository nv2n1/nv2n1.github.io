---
title: "usb_alloc_streams(9)"
name: "usb_alloc_streams"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_alloc_streams/"
---

usb_alloc_streams - allocate bulk endpoint stream IDs.

<h2>Synopsis</h2>

<pre><code>int usb_alloc_streams(struct usb_interface *interface, struct usb_host_endpoint **eps, unsigned int num_eps, unsigned int num_streams, gfp_t mem_flags);</code></pre>

<h2>Arguments</h2>

<i>interface</i>
<dl><dd><dd>alternate setting that includes all endpoints.</dl>
 

 <i>eps</i>
<dl><dd>array of endpoints that need streams.</dl>
 

 <i>num_eps</i>
<dl><dd>number of endpoints in the array.</dl>
 

 <i>num_streams</i>
<dl><dd>number of streams to allocate.</dl>
 

 <i>mem_flags</i>
<dl><dd>flags hcd should use to allocate memory.</dl>

<h2>Description</h2>

Sets up a group of bulk endpoints to have <i>num_streams</i> stream IDs available. Drivers may queue multiple transfers to different stream IDs, which may complete in a different order than they were queued.

<h2>Return</h2>

On success, the number of allocated streams. On failure, a negative error code.

<h2>Copyright</h2>


