---
title: "xmmultilistdeselectrow(3)"
name: "xmmultilistdeselectrow"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmmultilistdeselectrow/"
description: "XmMultiListDeselectRow — A MultiList function that deselects a row in the list"
---

<p><code>XmMultiListDeselectRow</code> &#8212; A MultiList function that deselects a row in the list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/MultiList.h&gt;
<code>void XmMultiListDeselectRow</code>(
<code>Widget widget</code>,
<code>XmString row</code>);</pre>
<h2>Description</h2>
<p><code>XmMultiListDeselectRow</code> unhighlights the specified row in the MultiList widget.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the MultiList widget from whose list an item is deselected.</p>
<dt><i>row</i></p>
<dd>Specifies the row number (starting from 0) to be deselected in the MultiList widget.</dl>
<p> For a complete definition of MultiList and its associated resources, see <code><a href="/docs/linux/man/3-xmmultilist/">XmMultiList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmmultilist/">XmMultiList</a></code>(3).</p>
