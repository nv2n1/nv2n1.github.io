---
title: "xmlistdeselectpos(3)"
name: "xmlistdeselectpos"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistdeselectpos/"
description: "XmListDeselectPos — A List function that deselects an item at a specified position in the list"
---

<p><code>XmListDeselectPos</code> &#8212; A List function that deselects an item at a specified position in the list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>void XmListDeselectPos</code>(
<code>Widget widget</code>,
<code>int position</code>);</pre>
<h2>Description</h2>
<p><code>XmListDeselectPos</code> unhighlights the item at the specified position and deletes it from the list of selected items.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List widget</p>
<dt><i>position</i></p>
<dd>Specifies the position of the item to be deselected. A value of 1 indicates that the first item in the list is deselected; a value of 2 indicates that the second item is deselected; and so on. A value of 0 (zero) indicates that the last item in the list is deselected.</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
