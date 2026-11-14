---
title: "xmlistreplaceitemsposunselected(3)"
name: "xmlistreplaceitemsposunselected"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistreplaceitemsposunselected/"
description: "XmListReplaceItemsPosUnselected — A List function that replaces items in a list without selecting the replacement items"
---

<p><code>XmListReplaceItemsPosUnselected</code> &#8212; A List function that replaces items in a list without selecting the replacement items</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>void XmListReplaceItemsPosUnselected</code>(
<code>Widget widget</code>,
<code>XmString *new_items</code>,
<code>int item_count</code>,
<code>int position</code>);</pre>
<h2>Description</h2>
<p><code>XmListReplaceItemsPosUnselected</code> replaces the specified number of items in the list with new items, starting at the given position. The replacement items remain unselected, even if they currently appear in the <code>XmNselectedItems</code> list.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List widget to replace items in.</p>
<dt><i>new_items</i></p>
<dd>Specifies a pointer to the replacement items.</p>
<dt><i>item_count</i></p>
<dd>Specifies the number of elements in <i>new_items</i> and the number of items in the list to replace. This number must be nonnegative.</p>
<dt><i>position</i></p>
<dd>Specifies the position of the first item in the list to be replaced. A value of 1 indicates that the first item replaced is the first item in the list; a value of 2 indicates that it is the second item; and so on.</p>
<dd>Beginning with the item specified in <i>position</i>, <i>item_count</i> items in the list are replaced with the corresponding elements from <i>new_items</i>. That is, the item at <i>position</i> is replaced with the first element of <i>new_items</i>; the item after <i>position</i> is replaced with the second element of <i>new_items</i>; and so on, until <i>item_count</i> is reached.</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
