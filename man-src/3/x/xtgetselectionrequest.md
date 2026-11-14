---
title: "xtgetselectionrequest(3)"
name: "xtgetselectionrequest"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtgetselectionrequest/"
description: "XtGetSelectionRequest – retrieve the event that triggered the XtConvertSelectionProc"
---

<p>XtGetSelectionRequest &#8211; retrieve the event that triggered the XtConvertSelectionProc </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>XSelectionRequestEvent* XtGetSelectionRequest(Widget <i>w</i>, Atom <i>selection</i>, XtRequestId <i>request_id</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>w</i></p>
<dd>Specifies the widget.</p>
<dt><i>selection</i></p>
<dd>Specifies the selection being processed.</p>
<dt><i>request_id</i></p>
<dd>Specifies the requestor id in the case of incremental selections, or NULL in the case of atomic transfers.</dl>
<h2>Description</h2>
<p><code>XtGetSelectionRequest</code> may only be called from within an <code>XtConvertSelectionProc</code> procedure and returns a pointer to the <code>SelectionRequest</code> event that caused the conversion procedure to be invoked. <i>Request_id</i> specifies a unique id for the individual request in the case that multiple incremental transfers are outstanding. For atomic transfers, <i>request_id</i> must be specified as NULL. If no <code>SelectionRequest</code> event is being processed for the specified <i>widget</i>, <i>selection</i>, and <i>request_id</i>, <code>XtGetSelectionRequest</code> returns NULL.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
