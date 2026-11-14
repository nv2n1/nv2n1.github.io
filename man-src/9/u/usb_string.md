---
title: "usb_string(9)"
name: "usb_string"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_string/"
description: "usb_string – returns UTF-8 version of a string descriptor"
---

<p>usb_string &#8211; returns UTF-8 version of a string descriptor</p>
<h2>Synopsis</h2>
<pre><code>int usb_string(struct usb_device *dev, int index, char *buf, size_t size);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the device whose string descriptor is being retrieved</dl>
<p> <i>index</i></p>
<dl>
<dd>the number of the descriptor</dl>
<p> <i>buf</i></p>
<dl>
<dd>where to put the string</dl>
<p> <i>size</i></p>
<dl>
<dd>how big is &#8220;buf&#8221;?</dl>
<h2>Context</h2>
<p>!in_interrupt ()</p>
<h2>Description</h2>
<p>This converts the UTF-16LE encoded strings returned by devices, from <code>usb_get_string_descriptor</code>, to null-terminated UTF-8 encoded ones that are more usable in most kernel contexts. Note that this function chooses strings in the first language supported by the device. </p>
<p> This call is synchronous, and may not be used in an interrupt context.</p>
<h2>Return</h2>
<p>length of the string (&gt;= 0) or usb_control_msg status (&lt; 0).</p>
<h2>Copyright</h2>
