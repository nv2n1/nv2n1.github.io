---
title: "xmlistdeselectitem(3)"
name: "xmlistdeselectitem"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistdeselectitem/"
description: "XmListDeselectItem — A List function that deselects the specified item from the selected list"
---

<p><code>XmListDeselectItem</code> &#8212; A List function that deselects the specified item from the selected list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>void XmListDeselectItem</code>(
<code>Widget widget</code>,
<code>XmString item</code>);</pre>
<h2>Description</h2>
<p><code>XmListDeselectItem</code> unhighlights and removes from the selected list the first item in the list that matches <i>item</i>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List from whose list an item is deselected.</p>
<dt><i>item</i></p>
<dd>Specifies the item to be deselected from the list. If <i>item</i> appears more than once in the List, only the first occurrence is matched.</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
