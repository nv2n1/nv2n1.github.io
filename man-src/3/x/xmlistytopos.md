---
title: "xmlistytopos(3)"
name: "xmlistytopos"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistytopos/"
description: "XmListYToPos — A List function that returns the position of the item at a specified y-coordinate"
---

<p><code>XmListYToPos</code> &#8212; A List function that returns the position of the item at a specified y-coordinate</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>int XmListYToPos</code>(
<code>Widget widget</code>,
<code>Position y</code>);</pre>
<h2>Description</h2>
<p><code>XmListYToPos</code> returns the position of the item at the given y-coordinate within the list.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List widget</p>
<dt><i>y</i></p>
<dd>Specifies the y-coordinate in the list&#8217;s coordinate system</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the position of the item at the specified y coordinate. A value of 1 indicates the first item in the list; a value of 2 indicates the second item; and so on. A value of 0 (zero) indicates that no item exists at the specified y coordinate.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3) and <code><a href="/docs/linux/man/3-xmlistpostobounds/">XmListPosToBounds</a></code>(3).</p>
