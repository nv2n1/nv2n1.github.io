---
title: "struct_usb_os_desc_table(9)"
name: "struct_usb_os_desc_table"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_os_desc_table/"
description: "struct_usb_os_desc_table – describes OS descriptors associated with one interface of a usb_function"
---

<p>struct_usb_os_desc_table &#8211; describes OS descriptors associated with one interface of a usb_function</p>
<h2>Synopsis</h2>
<pre><code>struct usb_os_desc_table {
    int if_id;
    struct usb_os_desc *os_desc;
};</code></pre>
<h2>Members</h2>
<p>if_id</p>
<dl>
<dd>Interface id</dl>
<p> os_desc</p>
<dl>
<dd>&quot;Extended Compatibility ID&#8221; and &#8220;Extended Properties&quot; of the interface</dl>
<h2>Description</h2>
<p>Each interface can have at most one &#8220;Extended Compatibility ID&#8221; and a number of &#8220;Extended Properties&#8221;.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
