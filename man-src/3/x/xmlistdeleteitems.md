---
title: "xmlistdeleteitems(3)"
name: "xmlistdeleteitems"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistdeleteitems/"
description: "XmListDeleteItems — A List function that deletes items from the list"
---

<p><code>XmListDeleteItems</code> &#8212; A List function that deletes items from the list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>void XmListDeleteItems</code>(
<code>Widget widget</code>,
<code>XmString *items</code>,
<code>int item_count</code>);</pre>
<h2>Description</h2>
<p><code>XmListDeleteItems</code> deletes the specified items from the list. For each element of <i>items</i>, the first item in the list that matches that element is deleted. A warning message appears if any of the items do not exist.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List from whose list an item is deleted</p>
<dt><i>items</i></p>
<dd>Specifies a pointer to items to be deleted from the list</p>
<dt><i>item_count</i></p>
<dd>Specifies the number of elements in <i>items</i> This number must be nonnegative.</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
