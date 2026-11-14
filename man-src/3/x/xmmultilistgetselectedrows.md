---
title: "xmmultilistgetselectedrows(3)"
name: "xmmultilistgetselectedrows"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmmultilistgetselectedrows/"
description: "XmMultiListGetSelectedRows — an MultiList function that returns the rows that currently are selected."
---

<p><code>XmMultiListGetSelectedRows</code> &#8212; an MultiList function that returns the rows that currently are selected.</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/MultiList.h&gt;
<code>XmMultiListRowInfo ** XmMultiListGetSelectedRows</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p>Use this routine to find the rows that currently are selected in an MultiList widget.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the MultiList widget.</dl>
<p> For a complete definition of MultiList and its associated resources, see <code><a href="/docs/linux/man/3-xmmultilist/">XmMultiList</a></code>(3).</p>
<h2>Return</h2>
<p>The XmMultiListRowInfo ** returned by this function contains a NULL terminated array of XmMultiListRowInfo pointers. The calling routine is responsible for freeing the returned pointer with XtFree(). The function will return NULL if no elements are selected.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmmultilist/">XmMultiList</a></code>(3).</p>
