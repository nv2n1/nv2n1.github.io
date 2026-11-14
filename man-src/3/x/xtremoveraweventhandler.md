---
title: "xtremoveraweventhandler(3)"
name: "xtremoveraweventhandler"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtremoveraweventhandler/"
description: "XtAddEventHandler, XtAddRawEventHandler, XtRemoveEventHandler, XtRemoveRawEventHandler, XtInsertEventHandler, XtInsertRawEventHandler – add and remove event handlers"
---

<p>XtAddEventHandler, XtAddRawEventHandler, XtRemoveEventHandler, XtRemoveRawEventHandler, XtInsertEventHandler, XtInsertRawEventHandler &#8211; add and remove event handlers </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtAddEventHandler(Widget <i>w</i>, EventMask <i>event_mask</i>, Boolean <i>nonmaskable</i>, XtEventHandler <i>proc</i>, XtPointer <i>client_data</i>);</p>
<dd>void XtAddRawEventHandler(Widget <i>w</i>, EventMask <i>event_mask</i>, Boolean <i>nonmaskable</i>, XtEventHandler <i>proc</i>, XtPointer <i>client_data</i>);</p>
<dd>void XtRemoveEventHandler(Widget <i>w</i>, EventMask <i>event_mask</i>, Boolean <i>nonmaskable</i>, XtEventHandler <i>proc</i>, XtPointer <i>client_data</i>);</p>
<dd>void XtRemoveRawEventHandler(Widget <i>w</i>, EventMask <i>event_mask</i>, Boolean <i>nonmaskable</i>, XtEventHandler <i>proc</i>, XtPointer <i>client_data</i>);</p>
<dd>void XtInsertEventHandler(Widget <i>w</i>, EventMask <i>event_mask</i>, Boolean <i>nonmaskable</i>, XtEventHandler <i>proc</i>, XtPointer <i>client_data</i>, XtListPosition <i>position</i>);</p>
<dd>void XtInsertRawEventHandler(Widget <i>w</i>, EventMask <i>event_mask</i>, Boolean <i>nonmaskable</i>, XtEventHandler <i>proc</i>, XtPointer <i>client_data</i>, XtListPosition <i>position</i>);</p>
<dd>typedef enum { XtListHead, XtListTail } XtListPosition;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>client_data</i></p>
<dd>Specifies additional data to be passed to the client&#8217;s event handler.</p>
<dt><i>event_mask</i></p>
<dd>Specifies the event mask for which to call or unregister this procedure.</p>
<dt><i>nonmaskable</i></p>
<dd>Specifies a Boolean value that indicates whether this procedure should be called or removed on the nonmaskable events ( <code>GraphicsExpose</code>, <code>NoExpose</code>, <code>SelectionClear</code>, <code>SelectionRequest</code>, <code>SelectionNotify</code>, <code>ClientMessage</code>, and <code>MappingNotify</code>).</p>
<dt><i>proc</i></p>
<dd>Specifies the procedure that is to be added or removed.</p>
<dt><i>w</i></p>
<dd>Specifies the widget for which this event handler is being registered.</p>
<dt><i>position</i></p>
<dd>Specifies when the event handler is to be called relative to other previously registered handlers.</dl>
<h2>Description</h2>
<p>The <code>XtAddEventHandler</code> function registers a procedure with the dispatch mechanism that is to be called when an event that matches the mask occurs on the specified widget. If the procedure is already registered with the same client_data, the specified mask is ORed into the existing mask. If the widget is realized, <code>XtAddEventHandler</code> calls <code>XSelectInput</code>, if necessary. </p>
<p> The <code>XtAddRawEventHandler</code> function is similar to <code>XtAddEventHandler</code> except that it does not affect the widget&#8217;s mask and never causes an <code>XSelectInput</code> for its events. Note that the widget might already have those mask bits set because of other nonraw event handlers registered on it. </p>
<p> The <code>XtRemoveRawEventHandler</code> function stops the specified procedure from receiving the specified events. Because the procedure is a raw event handler, this does not affect the widget&#8217;s mask and never causes a call on <code>XSelectInput</code>. </p>
<p> <code>XtInsertEventHandler</code> is identical to <code>XtAddEventHandler</code> with the additional <i>position</i> argument. If <i>position</i> is <code>XtListHead</code>, the event handler is registered to that it will be called before any event handlers that were previously registered for the same widget. If <i>position</i> is <code>XtListTail</code>, the event handler is registered to be called after any previously registered event handlers. If the procedure is already registered with the same <i>client_data</i> value, the specified mask augments the existing mask and the procedure is repositioned in the list. </p>
<p> <code>XtInsertRawEventHandler</code> is similar to <code>XtInsertEventHandler</code> except that it does not modify the widget&#8217;s event mask and never causes an <code>XSelectInput</code> for the specified events. If the procedure is already registered with the same <i>client_data</i> value, the specified mask augments the existing mask and the procedure is repositioned in the list.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtappnextevent/">XtAppNextEvent</a>(3), <a href="/docs/linux/man/3-xtbuildeventmask/">XtBuildEventMask</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
