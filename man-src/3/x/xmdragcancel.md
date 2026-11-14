---
title: "xmdragcancel(3)"
name: "xmdragcancel"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdragcancel/"
description: "XmDragCancel — A Drag and Drop function that terminates a drag transaction"
---

<p><code>XmDragCancel</code> &#8212; A Drag and Drop function that terminates a drag transaction</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DragDrop.h&gt;
<code>void XmDragCancel</code>(
<code>Widget dragcontext</code>);</pre>
<h2>Description</h2>
<p><code>XmDragCancel</code> terminates a drag operation and cancels any pending actions of the specified DragContext. This routine can only be called by the initiator client.</p>
<dl COMPACT>
<dt><i>dragcontext</i></p>
<dd>Specifies the ID of the DragContext widget associated with the drag and drop transaction to be terminated</dl>
<p> For a complete definition of DragContext and its associated resources, see <code><a href="/docs/linux/man/3-xmdragcontext/">XmDragContext</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdragcontext/">XmDragContext</a></code>(3) and <code><a href="/docs/linux/man/3-xmdragstart/">XmDragStart</a></code>(3).</p>
