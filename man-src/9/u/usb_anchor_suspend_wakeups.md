---
title: "usb_anchor_suspend_wakeups(9)"
name: "usb_anchor_suspend_wakeups"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_anchor_suspend_wakeups/"
---

usb_anchor_suspend_wakeups -

<h2>Synopsis</h2>

<pre><code>void usb_anchor_suspend_wakeups(struct usb_anchor *anchor);</code></pre>

<h2>Arguments</h2>

<i>anchor</i>
<dl><dd><dd>the anchor you want to suspend wakeups on</dl>

<h2>Description</h2>

Call this to stop the last urb being unanchored from waking up any usb_wait_anchor_empty_timeout waiters. This is used in the hcd urb give- back path to delay waking up until after the completion handler has run.

<h2>Copyright</h2>


