---
title: "xmmultilistmakerowvisible(3)"
name: "xmmultilistmakerowvisible"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmmultilistmakerowvisible/"
description: "XmMultiListMakeRowVisible — A MultiList function that shifts the visible list rows as desired"
---

<p><code>XmMultiListMakeRowVisible</code> &#8212; A MultiList function that shifts the visible list rows as desired</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/MultiList.h&gt;
<code>void XmMultiListMakeRowVisible</code>(
<code>Widget widget</code>,
<code>int row</code>);</pre>
<h2>Description</h2>
<p><code>XmMultiListMakeRowVisible</code> makes specified row visible.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the MultiList widget from whose list an item is selected.</p>
<dt><i>row</i></p>
<dd>Specifies the row number (starting from 0) to be visible in the MultiList widget.</dl>
<p> For a complete definition of MultiList and its associated resources, see <code><a href="/docs/linux/man/3-xmmultilist/">XmMultiList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmmultilist/">XmMultiList</a></code>(3).</p>
