---
title: "xmlistdeletepositions(3)"
name: "xmlistdeletepositions"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistdeletepositions/"
description: "XmListDeletePositions — A List function that deletes items from a list based on an array of positions"
---

<p><code>XmListDeletePositions</code> &#8212; A List function that deletes items from a list based on an array of positions</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>void XmListDeletePositions</code>(
<code>Widget widget</code>,
<code>int *position_list</code>,
<code>int position_count</code>);</pre>
<h2>Description</h2>
<p><code>XmListDeletePositions</code> deletes noncontiguous items from a list. The function deletes all items whose corresponding positions appear in the <i>position_list</i> array. A warning message is displayed if a specified position is invalid; that is, the value is 0, a negative integer, or a number greater than the number of items in the list.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List widget</p>
<dt><i>position_list</i></p>
<dd>Specifies an array of the item positions to be deleted. The position of the first item in the list is 1; the position of the second item is 2; and so on.</p>
<dt><i>position_count</i></p>
<dd>Specifies the number of elements in the <i>position_list</i>.</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
