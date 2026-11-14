---
title: "xmlistitempos(3)"
name: "xmlistitempos"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistitempos/"
description: "XmListItemPos — A List function that returns the position of an item in the list"
---

<p><code>XmListItemPos</code> &#8212; A List function that returns the position of an item in the list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>int XmListItemPos</code>(
<code>Widget widget</code>,
<code>XmString item</code>);</pre>
<h2>Description</h2>
<p><code>XmListItemPos</code> returns the position of the first instance of the specified item in a list.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List widget</p>
<dt><i>item</i></p>
<dd>Specifies the item whose position is returned</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the position in the list of the first instance of the specified item. The position of the first item in the list is 1; the position of the second item is 2; and so on. This function returns 0 (zero) if the item is not found.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
