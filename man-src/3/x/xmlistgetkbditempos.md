---
title: "xmlistgetkbditempos(3)"
name: "xmlistgetkbditempos"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistgetkbditempos/"
description: "XmListGetKbdItemPos — A List function that returns the position of the item at the location cursor"
---

<p><code>XmListGetKbdItemPos</code> &#8212; A List function that returns the position of the item at the location cursor</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>int XmListGetKbdItemPos</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmListGetKbdItemPos</code> returns the position of the list item at the location cursor.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List widget</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the position of the current keyboard item. A value of 1 indicates that the location cursor is at the first item of the list; a value of 2 indicates that it is at the second item; and so on. A value of 0 (zero) indicates the List widget is empty.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
