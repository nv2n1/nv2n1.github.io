---
title: "xmlistadditem(3)"
name: "xmlistadditem"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistadditem/"
description: "XmListAddItem — A List function that adds an item to the list"
---

<p><code>XmListAddItem</code> &#8212; A List function that adds an item to the list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>void XmListAddItem</code>(
<code>Widget widget</code>,
<code>XmString item</code>,
<code>int position</code>);</pre>
<h2>Description</h2>
<p><code>XmListAddItem</code> adds an item to the list at the given position. When the item is inserted into the list, it is compared with the current <code>XmNselectedItems</code> list. If the new item matches an item on the selected list, it appears selected.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List to which an item is added.</p>
<dt><i>item</i></p>
<dd>Specifies the item to be added to the list.</p>
<dt><i>position</i></p>
<dd>Specifies the position of the new item in the list. A value of 1 makes the new item the first item in the list; a value of 2 makes it the second item; and so on. A value of 0 (zero) makes the new item the last item in the list.</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
