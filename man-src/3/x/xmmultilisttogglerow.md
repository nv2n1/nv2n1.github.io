---
title: "xmmultilisttogglerow(3)"
name: "xmmultilisttogglerow"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmmultilisttogglerow/"
description: "XmMultiListToggleRow — An MultiList function that toggles the selection state of a specified row"
---

<p><code>XmMultiListToggleRow</code> &#8212; An MultiList function that toggles the selection state of a specified row</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/MultiList.h&gt;
<code>void XmMultiListToggleRow</code>(
<code>Widget widget</code>,
<code>short row</code>);</pre>
<h2>Description</h2>
<p><code>XmMultiListToggleRow</code> toggles the selection state of a row designated by row argument of the passed MultiList widget.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the MultiList from whose list an item is unselected.</p>
<dt><i>row</i></p>
<dd>Specified the number of row to toggle.</dl>
<p> For a complete definition of MultiList and its associated resources, see <code><a href="/docs/linux/man/3-xmmultilist/">XmMultiList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmmultilist/">XmMultiList</a></code>(3).</p>
