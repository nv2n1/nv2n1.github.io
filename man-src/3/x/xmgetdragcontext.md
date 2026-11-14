---
title: "xmgetdragcontext(3)"
name: "xmgetdragcontext"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmgetdragcontext/"
description: "XmGetDragContext — A Drag and Drop function that retrieves the DragContext widget ID associated with a timestamp"
---

<p><code>XmGetDragContext</code> &#8212; A Drag and Drop function that retrieves the DragContext widget ID associated with a timestamp</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DragC.h&gt;
<code>Widget XmGetDragContext</code>(
<code>Widget refwidget</code>,
<code>Time timestamp</code>);</pre>
<h2>Description</h2>
<p><code>XmGetDragContext</code> returns the widget ID of the active DragContext associated with a given display and timestamp. A timestamp uniquely identifies which DragContext is active when more than one drag and drop transaction has been initiated on a display. If the specified timestamp matches a timestamp processed between the start and finish of a single drag and drop transaction, the function returns the corresponding DragContext ID.</p>
<dl COMPACT>
<dt><i>refwidget</i></p>
<dd>Specifies the ID of the widget that the routine uses to identify the intended display. The function returns the ID of the DragContext associated with the display value passed by this widget.</p>
<dt><i>timestamp</i></p>
<dd>Specifies a timestamp.</dl>
<p> For a complete definition of DragContext and its associated resources, see <code><a href="/docs/linux/man/3-xmdragcontext/">XmDragContext</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the ID of the DragContext widget that is active for the specified timestamp. Otherwise, returns NULL if no active DragContext is found.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdragcontext/">XmDragContext</a></code>(3).</p>
