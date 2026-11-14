---
title: "xmmultilistgetselectedrowarray(3)"
name: "xmmultilistgetselectedrowarray"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmmultilistgetselectedrowarray/"
description: "XmMultiListGetSelectedRowArray — an MultiList function that returns an array of integers which are selected row numbers."
---

<p><code>XmMultiListGetSelectedRowArray</code> &#8212; an MultiList function that returns an array of integers which are selected row numbers.</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/MultiList.h&gt;
<code>int * XmMultiListGetSelectedRowArray</code>(
<code>Widget widget</code>,
<code>int * num_rows</code>);</pre>
<h2>Description</h2>
<p>This routine creates an array of integers which are selected row numbers in the MultiList widget.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the MultiList widget.</p>
<dt><i>num_rows</i></p>
<dd>Specifies pointer to the integer indicates number of returned row numbers.</dl>
<p> For a complete definition of MultiList and its associated resources, see <code><a href="/docs/linux/man/3-xmmultilist/">XmMultiList</a></code>(3).</p>
<h2>Return</h2>
<p>The <code>int *</code> returned by this function contains a selected rows numbers array. The calling routine is responsible for freeing the returned pointer with XtFree(). The function will return NULL if no elements are selected.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmmultilist/">XmMultiList</a></code>(3).</p>
