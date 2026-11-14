---
title: "xmlistadditemsunselected(3)"
name: "xmlistadditemsunselected"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistadditemsunselected/"
description: "XmListAddItemsUnselected — A List function that adds items to a list"
---

<p><code>XmListAddItemsUnselected</code> &#8212; A List function that adds items to a list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>void XmListAddItemsUnselected</code>(
<code>Widget widget</code>,
<code>XmString *items</code>,
<code>int item_count</code>,
<code>int position</code>);</pre>
<h2>Description</h2>
<p><code>XmListAddItemsUnselected</code> adds the specified items to the list at the given position. The inserted items remain unselected, even if they currently appear in the <code>XmNselectedItems</code> list.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List widget to add items to.</p>
<dt><i>items</i></p>
<dd>Specifies a pointer to the items to be added to the list.</p>
<dt><i>item_count</i></p>
<dd>Specifies the number of elements in <i>items</i>. This number must be nonnegative.</p>
<dt><i>position</i></p>
<dd>Specifies the position of the first new item in the list. A value of 1 makes the first new item the first item in the list; a value of 2 makes it the second item; and so on. A value of 0 (zero) makes the first new item follow the last item of the list.</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
