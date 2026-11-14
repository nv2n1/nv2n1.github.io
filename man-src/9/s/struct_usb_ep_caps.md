---
title: "struct_usb_ep_caps(9)"
name: "struct_usb_ep_caps"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_ep_caps/"
description: "struct_usb_ep_caps – endpoint capabilities description"
---

<p>struct_usb_ep_caps &#8211; endpoint capabilities description</p>
<h2>Synopsis</h2>
<pre><code>struct usb_ep_caps {
    unsigned type_control : 1;
    unsigned type_iso : 1;
    unsigned type_bulk : 1;
    unsigned type_int : 1;
    unsigned dir_in : 1;
    unsigned dir_out : 1;
};</code></pre>
<h2>Members</h2>
<p>type_control</p>
<dl>
<dd>Endpoint supports control type (reserved for ep0).</dl>
<p> type_iso</p>
<dl>
<dd>Endpoint supports isochronous transfers.</dl>
<p> type_bulk</p>
<dl>
<dd>Endpoint supports bulk transfers.</dl>
<p> type_int</p>
<dl>
<dd>Endpoint supports interrupt transfers.</dl>
<p> dir_in</p>
<dl>
<dd>Endpoint supports IN direction.</dl>
<p> dir_out</p>
<dl>
<dd>Endpoint supports OUT direction.</dl>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
