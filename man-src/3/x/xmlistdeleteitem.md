---
title: "xmlistdeleteitem(3)"
name: "xmlistdeleteitem"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistdeleteitem/"
description: "XmListDeleteItem — A List function that deletes an item from the list"
---

<p><code>XmListDeleteItem</code> &#8212; A List function that deletes an item from the list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>void XmListDeleteItem</code>(
<code>Widget widget</code>,
<code>XmString item</code>);</pre>
<h2>Description</h2>
<p><code>XmListDeleteItem</code> deletes the first item in the list that matches <i>item</i>. A warning message appears if the item does not exist.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List from whose list an item is deleted.</p>
<dt><i>item</i></p>
<dd>Specifies the text of the item to be deleted from the list. If <i>item</i> appears more than once in the List, only the first occurrence is matched.</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
