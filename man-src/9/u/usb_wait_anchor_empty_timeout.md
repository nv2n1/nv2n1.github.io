---
title: "usb_wait_anchor_empty_timeout(9)"
name: "usb_wait_anchor_empty_timeout"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_wait_anchor_empty_timeout/"
---

usb_wait_anchor_empty_timeout - wait for an anchor to be unused

<h2>Synopsis</h2>

<pre><code>int usb_wait_anchor_empty_timeout(struct usb_anchor *anchor, unsigned int timeout);</code></pre>

<h2>Arguments</h2>

<i>anchor</i>
<dl><dd><dd>the anchor you want to become unused</dl>
 

 <i>timeout</i>
<dl><dd>how long you are willing to wait in milliseconds</dl>

<h2>Description</h2>

Call this is you want to be sure all an anchor's URBs have finished

<h2>Return</h2>

Non-zero if the anchor became unused. Zero on timeout.

<h2>Copyright</h2>


