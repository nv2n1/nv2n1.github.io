---
title: "struct_usb_gadget_strings(9)"
name: "struct_usb_gadget_strings"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_gadget_strings/"
description: "struct_usb_gadget_strings – a set of USB strings in a given language"
---

<p>struct_usb_gadget_strings &#8211; a set of USB strings in a given language</p>
<h2>Synopsis</h2>
<pre><code>struct usb_gadget_strings {
    u16 language;
    struct usb_string *strings;
};</code></pre>
<h2>Members</h2>
<p>language</p>
<dl>
<dd>identifies the strings&#8217; language (0x0409 for en-us)</dl>
<p> strings</p>
<dl>
<dd>array of strings with their ids</dl>
<h2>Description</h2>
<p>If you&#8217;re using <code>usb_gadget_get_string</code>, use this to wrap all the strings for a given language.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
