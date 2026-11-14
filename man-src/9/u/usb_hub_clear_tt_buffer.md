---
title: "usb_hub_clear_tt_buffer(9)"
name: "usb_hub_clear_tt_buffer"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_hub_clear_tt_buffer/"
---

usb_hub_clear_tt_buffer - clear control/bulk TT state in high speed hub

<h2>Synopsis</h2>

<pre><code>int usb_hub_clear_tt_buffer(struct urb *urb);</code></pre>

<h2>Arguments</h2>

<i>urb</i>
<dl><dd><dd>an URB associated with the failed or incomplete split transaction</dl>

<h2>Description</h2>

High speed HCDs use this to tell the hub driver that some split control or bulk transaction failed in a way that requires clearing internal state of a transaction translator. This is normally detected (and reported) from interrupt context. 

 It may not be possible for that hub to handle additional full (or low) speed transactions until that state is fully cleared out.

<h2>Return</h2>

0 if successful. A negative error code otherwise.

<h2>Copyright</h2>


