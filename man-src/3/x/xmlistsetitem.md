---
title: "xmlistsetitem(3)"
name: "xmlistsetitem"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistsetitem/"
description: "XmListSetItem — A List function that makes an existing item the first visible item in the list"
---

<p><code>XmListSetItem</code> &#8212; A List function that makes an existing item the first visible item in the list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>void XmListSetItem</code>(
<code>Widget widget</code>,
<code>XmString item</code>);</pre>
<h2>Description</h2>
<p><code>XmListSetItem</code> makes the first item in the list that matches <i>item</i> the first visible item in the list.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List widget from whose list an item is made the first visible</p>
<dt><i>item</i></p>
<dd>Specifies the item</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
