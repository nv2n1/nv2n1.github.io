---
title: "usb_control_msg(9)"
name: "usb_control_msg"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_control_msg/"
description: "usb_control_msg – Builds a control urb, sends it off and waits for completion"
---

<p>usb_control_msg &#8211; Builds a control urb, sends it off and waits for completion</p>
<h2>Synopsis</h2>
<pre><code>int usb_control_msg(struct usb_device *dev, unsigned int pipe, __u8 request, __u8 requesttype, __u16 value, __u16 index, void *data, __u16 size, int timeout);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>pointer to the usb device to send the message to</dl>
<p> <i>pipe</i></p>
<dl>
<dd>endpoint &#8220;pipe&#8221; to send the message to</dl>
<p> <i>request</i></p>
<dl>
<dd>USB message request value</dl>
<p> <i>requesttype</i></p>
<dl>
<dd>USB message request type value</dl>
<p> <i>value</i></p>
<dl>
<dd>USB message value</dl>
<p> <i>index</i></p>
<dl>
<dd>USB message index value</dl>
<p> <i>data</i></p>
<dl>
<dd>pointer to the data to send</dl>
<p> <i>size</i></p>
<dl>
<dd>length in bytes of the data to send</dl>
<p> <i>timeout</i></p>
<dl>
<dd>time in msecs to wait for the message to complete before timing out (if 0 the wait is forever)</dl>
<h2>Context</h2>
<p>!in_interrupt ()</p>
<h2>Description</h2>
<p>This function sends a simple control message to a specified endpoint and waits for the message to complete, or timeout. </p>
<p> Don&#8217;t use this function from within an interrupt context, like a bottom half handler. If you need an asynchronous message, or need to send a message from within interrupt context, use <code>usb_submit_urb</code>. If a thread in your driver uses this call, make sure your <code>disconnect</code> method can wait for it to complete. Since you don&#8217;t have a handle on the URB used, you can&#8217;t cancel the request.</p>
<h2>Return</h2>
<p>If successful, the number of bytes transferred. Otherwise, a negative error number.</p>
<h2>Copyright</h2>
