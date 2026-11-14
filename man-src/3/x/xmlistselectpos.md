---
title: "xmlistselectpos(3)"
name: "xmlistselectpos"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistselectpos/"
description: "XmListSelectPos — A List function that selects an item at a specified position in the list"
---

<p><code>XmListSelectPos</code> &#8212; A List function that selects an item at a specified position in the list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>void XmListSelectPos</code>(
<code>Widget widget</code>,
<code>int position</code>,
<code>Boolean notify</code>);</pre>
<h2>Description</h2>
<p><code>XmListSelectPos</code> highlights a List item at the specified position and adds it to the list of selected items.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List widget.</p>
<dt><i>position</i></p>
<dd>Specifies the position of the item to be selected. A value of 1 indicates that the first item in the list is selected; a value of 2 indicates that the second item is selected; and so on. A value of 0 (zero) indicates that the last item in the list is selected.</p>
<dt><i>notify</i></p>
<dd>Specifies a Boolean value that when TRUE invokes the selection callback for the current mode. From an application interface view, calling this function with <i>notify</i> True is indistinguishable from a user-initiated selection action. When <i>notify</i> is FALSE, no callbacks are called.</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3) and <code><a href="/docs/linux/man/3-xmlistselectitem/">XmListSelectItem</a></code>(3).</p>
