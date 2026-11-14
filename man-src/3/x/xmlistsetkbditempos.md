---
title: "xmlistsetkbditempos(3)"
name: "xmlistsetkbditempos"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistsetkbditempos/"
description: "XmListSetKbdItemPos — A List function that sets the location cursor at a specified position"
---

<p><code>XmListSetKbdItemPos</code> &#8212; A List function that sets the location cursor at a specified position</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>Boolean XmListSetKbdItemPos</code>(
<code>Widget widget</code>,
<code>int position</code>);</pre>
<h2>Description</h2>
<p><code>XmListSetKbdItemPos</code> sets the location cursor at the item specified by <i>position</i>. This function does not determine if the item at the specified position is selected or not.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List widget.</p>
<dt><i>position</i></p>
<dd>Specifies the position of the item at which the location cursor is set. A value of 1 indicates the first item in the list; a value of 2 indicates the second item; and so on. A value of 0 (zero) sets the location cursor at the last item in the list.</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Return</h2>
<p>Returns False if no item exists at the specified position or if the list is empty; otherwise, returns True.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
