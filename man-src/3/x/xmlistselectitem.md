---
title: "xmlistselectitem(3)"
name: "xmlistselectitem"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistselectitem/"
description: "XmListSelectItem — A List function that selects an item in the list"
---

<p><code>XmListSelectItem</code> &#8212; A List function that selects an item in the list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>void XmListSelectItem</code>(
<code>Widget widget</code>,
<code>XmString item</code>,
<code>Boolean notify</code>);</pre>
<h2>Description</h2>
<p><code>XmListSelectItem</code> highlights and adds to the selected list the first item in the list that matches <i>item</i>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List widget from whose list an item is selected.</p>
<dt><i>item</i></p>
<dd>Specifies the item to be selected in the List widget. If <i>item</i> appears more than once in the List, only the first occurrence is matched.</p>
<dt><i>notify</i></p>
<dd>Specifies a Boolean value that when TRUE invokes the selection callback for the current mode. From an application interface view, calling this function with <i>notify</i> True is indistinguishable from a user-initiated selection action. When <i>notify</i> is FALSE, no callbacks are called.</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3) and <code><a href="/docs/linux/man/3-xmlistselectpos/">XmListSelectPos</a></code>(3).</p>
