---
title: "xtcancelselectionrequest(3)"
name: "xtcancelselectionrequest"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtcancelselectionrequest/"
description: "XtCreateSelectionRequest, XtSendSelectionRequest, XtCancelSelectionRequest – bundle multiple selection conversion requests into a single request using MULTIPLE target"
---

<p>XtCreateSelectionRequest, XtSendSelectionRequest, XtCancelSelectionRequest &#8211; bundle multiple selection conversion requests into a single request using MULTIPLE target </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtCreateSelectionRequest(Widget <i>requestor</i>, Atom <i>selection</i>);</p>
<dd>void XtSendSelectionRequest(Widget <i>requestor</i>, Atom <i>selection</i>, Time <i>time</i>);</p>
<dd>void XtCancelSelectionRequest(Widget <i>requestor</i>, Atom <i>selection</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>requestor</i></p>
<dd>Specifies the widget making the request. Must be of class Core or a subclass thereof.</p>
<dt><i>selection</i></p>
<dd>Specifies the particular selection desired.</p>
<dt><i>time</i></p>
<dd>Specifies the timestamp to be used in making the request.</dl>
<h2>Description</h2>
<p>When <code>XtCreateSelectionRequest</code> is called, subsequent calls to <code>XtGetSelectionValue</code> and <code>XtGetSelectionValueIncremental</code> with the requestor and selection as specified to <code>XtCreateSelectionRequest</code> will be bundled into a single selection conversion request with multiple targets. The request is actually initiated by calling <code>XtSendSelectionRequest</code>. </p>
<p> When <code>XtSendSelectionRequest</code> is called with a value of <i>requestor</i> and <i>selection</i> matching a previous call to <code>XtCreateSelectionRequest</code>, a selection conversion request is actually sent to the selection owner. If a single target request is queued, that request is made. If multiple targets are queued they are bundled into a single request with the target MULTIPLE using the specified timestamp. As the conversions are made, the callbacks associated with each <code>XtGetSelectionValue</code> and <code>XtGetSelectionValueIncremental</code> are invoked in turn. </p>
<p> Multi-threaded applications should lock the application context before calling <code>XtCreateSelectionRequest</code> and release the lock after calling <code>XtSendSelectionRequest</code> to ensure that the thread assembling the request is safe from interference by another thread assembling a different request naming the same widget and selection. </p>
<p> When <code>XtCancelSelectionRequest</code> is called, any requests queued since the last call to <code>XtCreateSelectionRequest</code> are cleaned up. Subsequent calls to <code>XtGetSelectionValue</code>, <code>XtGetSelectionValues</code>, <code>XtGetSelectionValueIncremental</code>, and <code>XtGetSelectionValuesIncremental</code> will not be deferred.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
