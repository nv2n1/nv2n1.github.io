---
title: "xmlistreplaceitemsunselected(3)"
name: "xmlistreplaceitemsunselected"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistreplaceitemsunselected/"
description: "XmListReplaceItemsUnselected — A List function that replaces items in a list"
---

<p><code>XmListReplaceItemsUnselected</code> &#8212; A List function that replaces items in a list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>void XmListReplaceItemsUnselected</code>(
<code>Widget widget</code>,
<code>XmString *old_items</code>,
<code>int item_count</code>,
<code>XmString *new_items</code>);</pre>
<h2>Description</h2>
<p><code>XmListReplaceItemsUnselected</code> replaces each specified item in the list with a corresponding new item. The replacement items remain unselected, even if they currently appear in the <code>XmNselectedItems</code> list.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List widget to replace items in.</p>
<dt><i>old_items</i></p>
<dd>Specifies a pointer to the list items to be replaced.</p>
<dt><i>item_count</i></p>
<dd>Specifies the number of elements in <i>old_items</i> and <i>new_items</i>. This number must be nonnegative.</p>
<dt><i>new_items</i></p>
<dd>Specifies a pointer to the replacement items. Every occurrence of each element of <i>old_items</i> is replaced with the corresponding element from <i>new_items</i>. That is, the first element of <i>old_items</i> is replaced with the first element of <i>new_items</i>. The second element of <i>old_items</i> is replaced with the second element of <i>new_items</i>, and so on until <i>item_count</i> is reached. If an element in <i>old_items</i> does not exist in the list, the corresponding entry in <i>new_items</i> is skipped.</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
