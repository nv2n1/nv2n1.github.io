---
title: "xmmultilistunselectitem(3)"
name: "xmmultilistunselectitem"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmmultilistunselectitem/"
description: "XmMultiListUnselectItem — An MultiList function that deselects the specified item of the list"
---

<p><code>XmMultiListUnselectItem</code> &#8212; An MultiList function that deselects the specified item of the list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/MultiList.h&gt;
<code>void XmMultiListUnselectItem</code>(
<code>Widget widget</code>,
<code>XmMultiListRowInfo *row_info</code>);</pre>
<h2>Description</h2>
<p><code>XmMultiListUnselectItem</code> unselects the row designated by row_info of the passed MultiList widget.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the MultiList from whose list an item is unselected.</p>
<dt><i>row_info</i></p>
<dd>Specified the pointer to the row which is to be unselected.</dl>
<p> For a complete definition of MultiList and its associated resources, see <code><a href="/docs/linux/man/3-xmmultilist/">XmMultiList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmmultilist/">XmMultiList</a></code>(3).</p>
