---
title: "usb_get_from_anchor(9)"
name: "usb_get_from_anchor"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_get_from_anchor/"
description: "usb_get_from_anchor – get an anchor’s oldest urb"
---

<p>usb_get_from_anchor &#8211; get an anchor&#8217;s oldest urb</p>
<h2>Synopsis</h2>
<pre><code>struct urb *usb_get_from_anchor(struct usb_anchor *anchor);</code></pre>
<h2>Arguments</h2>
<p><i>anchor</i></p>
<dl>
<dd>
<dd>the anchor whose urb you want</dl>
<h2>Description</h2>
<p>This will take the oldest urb from an anchor, unanchor and return it</p>
<h2>Return</h2>
<p>The oldest urb from <i>anchor</i>, or <code>NULL</code> if <i>anchor</i> has no urbs associated with it.</p>
<h2>Copyright</h2>
