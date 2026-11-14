---
title: "xmmultilistselectitems(3)"
name: "xmmultilistselectitems"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmmultilistselectitems/"
description: "XmMultiListSelectItems — A MultiList function that selects items in the list by matching column entries"
---

<p><code>XmMultiListSelectItems</code> &#8212; A MultiList function that selects items in the list by matching column entries</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/MultiList.h&gt;
<code>void XmMultiListSelectItems</code>(
<code>Widget widget</code>,
<code>XmString item</code>,
<code>int column</code>,
<code>Boolean notify</code>);</pre>
<h2>Description</h2>
<p><code>XmMultiListSelectItems</code> highlights rows in the list where column number <i>column</i> matches <i>item</i>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the MultiList widget from whose list an item is selected.</p>
<dt><i>item</i></p>
<dd>Specifies XmString to use as selection key.</p>
<dt><i>column</i></p>
<dd>Specifies a column number (starting from 0) to match, or XmANY_COLUMN for looking for any column.</p>
<dt><i>notify</i></p>
<dd>Specifies a Boolean value that when TRUE invokes the selection callback for the current mode. From an application interface view, calling this function with <i>notify</i> True is indistinguishable from a user-initiated selection action. When <i>notify</i> is FALSE, no callbacks are called.</dl>
<p> For a complete definition of MultiList and its associated resources, see <code><a href="/docs/linux/man/3-xmmultilist/">XmMultiList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmmultilist/">XmMultiList</a></code>(3) and <code><a href="/docs/linux/man/3-xmmultilistgetselectrows/">XmMultiListGetSelectRows</a></code>(3).</p>
