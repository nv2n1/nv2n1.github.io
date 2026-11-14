---
title: "struct_usb_string(9)"
name: "struct_usb_string"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_string/"
description: "struct_usb_string – wraps a C string and its USB id"
---

<p>struct_usb_string &#8211; wraps a C string and its USB id</p>
<h2>Synopsis</h2>
<pre><code>struct usb_string {
    u8 id;
    const char *s;
};</code></pre>
<h2>Members</h2>
<p>id</p>
<dl>
<dd>the (nonzero) ID for this string</dl>
<p> s</p>
<dl>
<dd>the string, in UTF-8 encoding</dl>
<h2>Description</h2>
<p>If you&#8217;re using <code>usb_gadget_get_string</code>, use this to wrap a string together with its ID.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
