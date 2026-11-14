---
title: "xmlistreplacepositions(3)"
name: "xmlistreplacepositions"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistreplacepositions/"
description: "XmListReplacePositions — A List function that replaces items in a list based on position"
---

<p><code>XmListReplacePositions</code> &#8212; A List function that replaces items in a list based on position</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>void XmListReplacePositions</code>(
<code>Widget widget</code>,
<code>int *position_list</code>,
<code>XmString *item_list</code>,
<code>int item_count;</code>);</pre>
<h2>Description</h2>
<p><code>XmListReplacePositions</code> replaces noncontiguous items in a list. The item at each position specified in <i>position_list</i> is replaced with the corresponding entry in <i>item_list</i>. When the items are inserted into the list, they are compared with the current <code>XmNselectedItems</code> list. Any of the new items that match items on the selected list appear selected. A warning message is displayed if a specified position is invalid; that is, the value is 0 (zero), a negative integer, or a number greater than the number of items in the list.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List widget.</p>
<dt><i>position_list</i></p>
<dd>Specifies an array of the positions of items to be replaced. The position of the first item in the list is 1; the position of the second item is 2; and so on.</p>
<dt><i>item_list</i></p>
<dd>Specifies an array of the replacement items.</p>
<dt><i>item_count</i></p>
<dd>Specifies the number of elements in <i>position_list</i> and <i>item_list</i>. This number must be nonnegative.</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
