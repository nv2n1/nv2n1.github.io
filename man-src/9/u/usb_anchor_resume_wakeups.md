---
title: "usb_anchor_resume_wakeups(9)"
name: "usb_anchor_resume_wakeups"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_anchor_resume_wakeups/"
---

usb_anchor_resume_wakeups -

<h2>Synopsis</h2>

<pre><code>void usb_anchor_resume_wakeups(struct usb_anchor *anchor);</code></pre>

<h2>Arguments</h2>

<i>anchor</i>
<dl><dd><dd>the anchor you want to resume wakeups on</dl>

<h2>Description</h2>

Allow usb_wait_anchor_empty_timeout waiters to be woken up again, and wake up any current waiters if the anchor is empty.

<h2>Copyright</h2>


