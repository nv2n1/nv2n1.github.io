---
title: "usb_free_urb(9)"
name: "usb_free_urb"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_free_urb/"
---

usb_free_urb - frees the memory used by a urb when all users of it are finished

<h2>Synopsis</h2>

<pre><code>void usb_free_urb(struct urb *urb);</code></pre>

<h2>Arguments</h2>

<i>urb</i>
<dl><dd><dd>pointer to the urb to free, may be NULL</dl>

<h2>Description</h2>

Must be called when a user of a urb is finished with it. When the last user of the urb calls this function, the memory of the urb is freed.

<h2>Note</h2>

The transfer buffer associated with the urb is not freed unless the URB_FREE_BUFFER transfer flag is set.

<h2>Copyright</h2>


