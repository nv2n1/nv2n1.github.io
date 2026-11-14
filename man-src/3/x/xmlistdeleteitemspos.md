---
title: "xmlistdeleteitemspos(3)"
name: "xmlistdeleteitemspos"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistdeleteitemspos/"
description: "XmListDeleteItemsPos — A List function that deletes items from the list starting at the given position"
---

<p><code>XmListDeleteItemsPos</code> &#8212; A List function that deletes items from the list starting at the given position</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>void XmListDeleteItemsPos</code>(
<code>Widget widget</code>,
<code>int item_count</code>,
<code>int position</code>);</pre>
<h2>Description</h2>
<p><code>XmListDeleteItemsPos</code> deletes the specified number of items from the list starting at the specified position.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List from whose list an item is deleted.</p>
<dt><i>item_count</i></p>
<dd>Specifies the number of items to be deleted. This number must be nonnegative.</p>
<dt><i>position</i></p>
<dd>Specifies the position in the list of the first item to be deleted. A value of 1 indicates that the first deleted item is the first item in the list; a value of 2 indicates that it is the second item; and so on.</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
