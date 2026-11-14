---
title: "xmlistposselected(3)"
name: "xmlistposselected"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistposselected/"
description: "XmListPosSelected — A List function that determines if the list item at a specified position is selected"
---

<p><code>XmListPosSelected</code> &#8212; A List function that determines if the list item at a specified position is selected</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>Boolean XmListPosSelected</code>(
<code>Widget widget</code>,
<code>int position</code>);</pre>
<h2>Description</h2>
<p><code>XmPosSelected</code> determines if the list item at the specified position is selected or not.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List widget</p>
<dt><i>position</i></p>
<dd>Specifies the position of the list item. A value of 1 indicates the first item in the list; a value of 2 indicates the second item; and so on. A value of 0 (zero) specifies the last item in the list.</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Return</h2>
<p>Returns True if the list item is selected; otherwise, returns False if the item is not selected or the specified position is invalid.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
