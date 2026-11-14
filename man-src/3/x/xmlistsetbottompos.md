---
title: "xmlistsetbottompos(3)"
name: "xmlistsetbottompos"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistsetbottompos/"
description: "XmListSetBottomPos — A List function that makes a specified item the last visible item in the list"
---

<p><code>XmListSetBottomPos</code> &#8212; A List function that makes a specified item the last visible item in the list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>void XmListSetBottomPos</code>(
<code>Widget widget</code>,
<code>int position</code>);</pre>
<h2>Description</h2>
<p><code>XmListSetBottomPos</code> makes the item at the specified position the last visible item in the List.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List widget.</p>
<dt><i>position</i></p>
<dd>Specifies the position of the item to be made the last visible item in the list. A value of 1 indicates that the first item in the list is the last visible item; a value of 2 indicates that the second item is the last visible item; and so on. A value of 0 (zero) indicates that the last item in the list is the last visible item.</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
