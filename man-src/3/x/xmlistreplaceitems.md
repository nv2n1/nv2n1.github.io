---
title: "xmlistreplaceitems(3)"
name: "xmlistreplaceitems"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistreplaceitems/"
description: "XmListReplaceItems — A List function that replaces the specified elements in the list"
---

<p><code>XmListReplaceItems</code> &#8212; A List function that replaces the specified elements in the list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>void XmListReplaceItems</code>(
<code>Widget widget</code>,
<code>XmString *old_items</code>,
<code>int item_count</code>,
<code>XmString *new_items</code>);</pre>
<h2>Description</h2>
<p><code>XmListReplaceItems</code> replaces each specified item of the list with a corresponding new item. When the items are inserted into the list, they are compared with the current <code>XmNselectedItems</code> list. If any of the new items matches an item on the selected list, it appears selected.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List widget.</p>
<dt><i>old_items</i></p>
<dd>Specifies the items to be replaced.</p>
<dt><i>item_count</i></p>
<dd>Specifies the number of items in <i>old_items</i> and <i>new_items</i>. This number must be nonnegative.</p>
<dt><i>new_items</i></p>
<dd>Specifies the replacement items.</dl>
<p> Every occurrence of each element of <i>old_items</i> is replaced with the corresponding element from <i>new_items</i>. That is, the first element of <i>old_items</i> is replaced with the first element of <i>new_items</i>. The second element of <i>old_items</i> is replaced with the second element of <i>new_items</i>, and so on until <i>item_count</i> is reached. </p>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
