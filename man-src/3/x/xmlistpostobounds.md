---
title: "xmlistpostobounds(3)"
name: "xmlistpostobounds"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistpostobounds/"
description: "XmListPosToBounds — A List function that returns the bounding box of an item at a specified position in a list"
---

<p><code>XmListPosToBounds</code> &#8212; A List function that returns the bounding box of an item at a specified position in a list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>Boolean XmListPosToBounds</code>(
<code>Widget widget</code>,
<code>int position</code>,
<code>Position *x</code>,
<code>Position *y</code>,
<code>Dimension *width</code>,
<code>Dimension *height</code>);</pre>
<h2>Description</h2>
<p><code>XmListPosToBounds</code> returns the coordinates of an item within a list and the dimensions of its bounding box. The function returns the associated x and y-coordinates of the upper left corner of the bounding box relative to the upper left corner of the List widget, as well as the width and the height of the box. The caller can pass a NULL value for the <i>x</i>, <i>y</i>, <i>width</i>, or <i>height</i> parameters to indicate that the return value for that parameter is not requested.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List widget.</p>
<dt><i>position</i></p>
<dd>Specifies the position of the specified item. A value of 1 indicates the first item in the list; a value of 2 indicates the second item; and so on. A value of 0 (zero) specifies the last item in the list.</p>
<dt><i>x</i></p>
<dd>Specifies a pointer to the returned x-coordinate of the item.</p>
<dt><i>y</i></p>
<dd>Specifies the pointer to the returned y-coordinate of the item.</p>
<dt><i>width</i></p>
<dd>Specifies the pointer to the returned width of the item.</p>
<dt><i>height</i></p>
<dd>Specifies the pointer to the returned height of the item.</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Return</h2>
<p>If the item at the specified position is not visible, returns False, and the returned values (if any) are undefined. Otherwise, this function returns True.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3) and <code><a href="/docs/linux/man/3-xmlistytopos/">XmListYToPos</a></code>(3).</p>
