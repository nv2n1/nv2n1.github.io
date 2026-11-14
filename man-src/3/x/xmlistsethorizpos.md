---
title: "xmlistsethorizpos(3)"
name: "xmlistsethorizpos"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistsethorizpos/"
description: "XmListSetHorizPos — A List function that scrolls to the specified position in the list"
---

<p><code>XmListSetHorizPos</code> &#8212; A List function that scrolls to the specified position in the list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>void XmListSetHorizPos</code>(
<code>Widget widget</code>,
<code>int position</code>);</pre>
<h2>Description</h2>
<p><code>XmListSetHorizPos</code> sets the <code>XmNvalue</code> resource of the horizontal ScrollBar to the specified position and updates the visible portion of the list with the new value if the List widget&#8217;s <code>XmNlistSizePolicy</code> is set to <code>XmCONSTANT</code> or <code>XmRESIZE_IF_POSSIBLE</code> and the horizontal ScrollBar is currently visible. This is equivalent to moving the horizontal ScrollBar to the specified position.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List widget</p>
<dt><i>position</i></p>
<dd>Specifies the horizontal position</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
