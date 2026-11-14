---
title: "usb_gadget_get_string(9)"
name: "usb_gadget_get_string"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_gadget_get_string/"
description: "usb_gadget_get_string – fill out a string descriptor"
---

<p>usb_gadget_get_string &#8211; fill out a string descriptor</p>
<h2>Synopsis</h2>
<pre><code>int usb_gadget_get_string(struct usb_gadget_strings *table, int id, u8 *buf);</code></pre>
<h2>Arguments</h2>
<p><i>table</i></p>
<dl>
<dd>
<dd>of c strings encoded using UTF-8</dl>
<p> <i>id</i></p>
<dl>
<dd>string id, from low byte of wValue in get string descriptor</dl>
<p> <i>buf</i></p>
<dl>
<dd>at least 256 bytes, must be 16-bit aligned</dl>
<h2>Description</h2>
<p>Finds the UTF-8 string matching the ID, and converts it into a string descriptor in utf16-le. Returns length of descriptor (always even) or negative errno </p>
<p> If your driver needs stings in multiple languages, you&#8217;ll probably &#8220;switch (wIndex) { &#8230; }&#8221; in your ep0 string descriptor logic, using this routine after choosing which set of UTF-8 strings to use. Note that US-ASCII is a strict subset of UTF-8; any string bytes with the eighth bit set will be multibyte UTF-8 characters, not ISO-8859/1 characters (which are also widely used in C strings).</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
