---
title: "xmlistupdateselectedlist(3)"
name: "xmlistupdateselectedlist"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistupdateselectedlist/"
description: "XmListUpdateSelectedList — A List function that updates the XmNselectedItems resource"
---

<p><code>XmListUpdateSelectedList</code> &#8212; A List function that updates the XmNselectedItems resource</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>void XmListUpdateSelectedList</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmListUpdateSelectedList</code> frees the contents of the current <code>XmNselectedItems</code> list. The routine traverses the <code>XmNitems</code> list and adds each currently selected item to the <code>XmNselectedItems</code> list. For each selected item, there is a corresponding entry in the updated <code>XmNselectedItems</code> list.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List widget to update</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
