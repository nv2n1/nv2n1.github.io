---
title: "usb_ep_align(9)"
name: "usb_ep_align"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_ep_align/"
description: "usb_ep_align – returns len aligned to ep’s maxpacketsize."
---

<p>usb_ep_align &#8211; returns <i>len</i> aligned to ep&#8217;s maxpacketsize.</p>
<h2>Synopsis</h2>
<pre><code>size_t usb_ep_align(struct usb_ep *ep, size_t len);</code></pre>
<h2>Arguments</h2>
<p><i>ep</i></p>
<dl>
<dd>
<dd>the endpoint whose maxpacketsize is used to align <i>len</i></dl>
<p> <i>len</i></p>
<dl>
<dd>buffer size&#8217;s length to align to <i>ep</i>&#8216;s maxpacketsize</dl>
<h2>Description</h2>
<p>This helper is used to align buffer&#8217;s size to an ep&#8217;s maxpacketsize.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
