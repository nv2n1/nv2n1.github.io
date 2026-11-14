---
title: "xmlistdeletepos(3)"
name: "xmlistdeletepos"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistdeletepos/"
description: "XmListDeletePos — A List function that deletes an item from a list at a specified position"
---

<p><code>XmListDeletePos</code> &#8212; A List function that deletes an item from a list at a specified position</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>void XmListDeletePos</code>(
<code>Widget widget</code>,
<code>int position</code>);</pre>
<h2>Description</h2>
<p><code>XmListDeletePos</code> deletes an item at a specified position. A warning message appears if the position does not exist.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List from which an item is to be deleted.</p>
<dt><i>position</i></p>
<dd>Specifies the position of the item to be deleted. A value of 1 indicates that the first item in the list is deleted; a value of 2 indicates that the second item is deleted; and so on. A value of 0 (zero) indicates that the last item in the list is deleted.</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
