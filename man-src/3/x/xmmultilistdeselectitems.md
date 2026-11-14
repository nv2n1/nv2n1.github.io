---
title: "xmmultilistdeselectitems(3)"
name: "xmmultilistdeselectitems"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmmultilistdeselectitems/"
description: "XmMultiListDeselectItems — A MultiList function that deselects items in the list by matching column entries"
---

<p><code>XmMultiListDeselectItems</code> &#8212; A MultiList function that deselects items in the list by matching column entries</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/MultiList.h&gt;
<code>void XmMultiListDeselectItems</code>(
<code>Widget widget</code>,
<code>XmString item</code>,
<code>int column</code>);</pre>
<h2>Description</h2>
<p><code>XmMultiListDeselectItems</code> unhighlights rows in the list where column number <i>column</i> matches <i>item</i>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the MultiList widget from whose list an item is selected.</p>
<dt><i>item</i></p>
<dd>Specifies XmString to use as selection key.</p>
<dt><i>column</i></p>
<dd>Specifies a column number (starting from 0) to match, or XmANY_COLUMN for looking for any column.</dl>
<p> For a complete definition of MultiList and its associated resources, see <code><a href="/docs/linux/man/3-xmmultilist/">XmMultiList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmmultilist/">XmMultiList</a></code>(3).</p>
