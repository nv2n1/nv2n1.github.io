---
title: "xmlistitemexists(3)"
name: "xmlistitemexists"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistitemexists/"
description: "XmListItemExists — A List function that checks if a specified item is in the list"
---

<p><code>XmListItemExists</code> &#8212; A List function that checks if a specified item is in the list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>Boolean XmListItemExists</code>(
<code>Widget widget</code>,
<code>XmString item</code>);</pre>
<h2>Description</h2>
<p><code>XmListItemExists</code> is a Boolean function that checks if a specified item is present in the list.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List widget</p>
<dt><i>item</i></p>
<dd>Specifies the item whose presence is checked</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Return</h2>
<p>Returns True if the specified item is present in the list.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
