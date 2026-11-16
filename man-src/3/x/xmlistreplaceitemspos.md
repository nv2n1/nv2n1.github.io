---
title: "xmlistreplaceitemspos(3)"
name: "xmlistreplaceitemspos"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistreplaceitemspos/"
description: "XmListReplaceItemsPos — A List function that replaces the specified elements in the list"
---

<p><code>XmListReplaceItemsPos</code> &#8212; A List function that replaces the specified elements in the list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>void XmListReplaceItemsPos</code>(
<code>Widget widget</code>,
<code>XmString *new_items</code>,
<code>int item_count</code>,
<code>int position</code>);</pre>
<h2>Description</h2>
<p><code>XmListReplaceItemsPos</code> replaces the specified number of items of the List with new items, starting at the specified position in the List. When the items are inserted into the list, they are compared with the current <code>XmNselectedItems</code> list. If any of the new items matches an item on the selected list, it appears selected.</p>
<dl COMPACT>
<dt><i>widget</i></dt>
<dd>Specifies the ID of the List widget.</dd>
<dt><i>new_items</i></dt>
<dd>Specifies the replacement items.</dd>
<dt><i>item_count</i></dt>
<dd>Specifies the number of items in <i>new_items</i> and the number of items in the list to replace. This number must be nonnegative.</dd>
<dt><i>position</i></dt>
<dd>Specifies the position of the first item in the list to be replaced. A value of 1 indicates that the first item replaced is the first item in the list; a value of 2 indicates that it is the second item; and so on.</dd>
<dd>Beginning with the item specified in <i>position</i>, <i>item_count</i> items in the list are replaced with the corresponding elements from <i>new_items</i>. That is, the item at <i>position</i> is replaced with the first element of <i>new_items</i>; the item after <i>position</i> is replaced with the second element of <i>new_items</i>; and so on, until <i>item_count</i> is reached.</dd></dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
