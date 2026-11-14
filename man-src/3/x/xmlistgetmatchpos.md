---
title: "xmlistgetmatchpos(3)"
name: "xmlistgetmatchpos"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistgetmatchpos/"
description: "XmListGetMatchPos — A List function that returns all instances of an item in the list"
---

<p><code>XmListGetMatchPos</code> &#8212; A List function that returns all instances of an item in the list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>Boolean XmListGetMatchPos</code>(
<code>Widget widget</code>,
<code>XmString item</code>,
<code>int **position_list</code>,
<code>int *position_count</code>);</pre>
<h2>Description</h2>
<p><code>XmListGetMatchPos</code> is a Boolean function that returns an array of positions where a specified item is found in a List.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List widget.</p>
<dt><i>item</i></p>
<dd>Specifies the item to search for.</p>
<dt><i>position_list</i></p>
<dd>Returns an array of positions at which the item occurs in the List. The position of the first item in the list is 1; the position of the second item is 2; and so on. When the return value is True, <code>XmListGetMatchPos</code> allocates memory for this array. The caller is responsible for freeing this memory. The caller can recover the allocated memory by calling <code>XtFree</code>.</p>
<dt><i>position_count</i></p>
<dd>Returns the number of elements in the <i>position_list</i>.</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Return</h2>
<p>Returns True if the specified item is present in the list, and False if it is not.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
