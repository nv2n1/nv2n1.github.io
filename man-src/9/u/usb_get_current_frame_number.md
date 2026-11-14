---
title: "usb_get_current_frame_number(9)"
name: "usb_get_current_frame_number"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_get_current_frame_number/"
---

usb_get_current_frame_number - return current bus frame number

<h2>Synopsis</h2>

<pre><code>int usb_get_current_frame_number(struct usb_device *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>the device whose bus is being queried</dl>

<h2>Return</h2>

The current frame number for the USB host controller used with the given USB device. This can be used when scheduling isochronous requests.

<h2>Note</h2>

Different kinds of host controller have different "scheduling horizons". While one type might support scheduling only 32 frames into the future, others could support scheduling up to 1024 frames into the future.

<h2>Copyright</h2>


