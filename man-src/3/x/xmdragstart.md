---
title: "xmdragstart(3)"
name: "xmdragstart"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdragstart/"
description: "XmDragStart — A Drag and Drop function that initiates a drag and drop transaction"
---

<p><code>XmDragStart</code> &#8212; A Drag and Drop function that initiates a drag and drop transaction</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DragDrop.h&gt;
<code>Widget XmDragStart</code>(
<code>Widget widget</code>,
<code>XEvent *event</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmDragStart</code> initiates a drag operation. This routine returns the DragContext widget that it initializes for the associated drag transaction. The toolkit is responsible for freeing the DragContext when the drag and drop transaction is complete.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the smallest widget and/or gadget that encloses the source elements selected for a drag operation.</p>
<dt><i>event</i></p>
<dd>Specifies the <code>XEvent</code> that triggered the drag operation. This event must be a ButtonPress event.</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list. Any <code>XmDragContext</code> resources not specified in the argument list are obtained from the resource database or are set to their default values.</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> For a complete definition of DragContext and its associated resources, see <code><a href="/docs/linux/man/3-xmdragcontext/">XmDragContext</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the ID of the DragContext widget that controls this drag and drop transaction. Returns NULL if the drag cannot be initiated.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdragcancel/">XmDragCancel</a></code>(3) and <code><a href="/docs/linux/man/3-xmdragcontext/">XmDragContext</a></code>(3).</p>
