---
title: "xmmultilistselectrow(3)"
name: "xmmultilistselectrow"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmmultilistselectrow/"
description: "XmMultiListSelectRow — A MultiList function that selects a row in the list"
---

<p><code>XmMultiListSelectRow</code> &#8212; A MultiList function that selects a row in the list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/MultiList.h&gt;
<code>void XmMultiListSelectRow</code>(
<code>Widget widget</code>,
<code>XmString row</code>,
<code>Boolean notify</code>);</pre>
<h2>Description</h2>
<p><code>XmMultiListSelectRow</code> highlights the specified row in the MultiList widget.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the MultiList widget from whose list an item is selected.</p>
<dt><i>row</i></p>
<dd>Specifies the row number (starting from 0) to be selected in the MultiList widget.</p>
<dt><i>notify</i></p>
<dd>Specifies a Boolean value that when TRUE invokes the selection callback for the current mode. From an application interface view, calling this function with <i>notify</i> True is indistinguishable from a user-initiated selection action. When <i>notify</i> is FALSE, no callbacks are called.</dl>
<p> For a complete definition of MultiList and its associated resources, see <code><a href="/docs/linux/man/3-xmmultilist/">XmMultiList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmmultilist/">XmMultiList</a></code>(3).</p>
