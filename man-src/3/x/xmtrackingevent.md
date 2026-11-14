---
title: "xmtrackingevent(3)"
name: "xmtrackingevent"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtrackingevent/"
description: "XmTrackingEvent — A Toolkit function that provides a modal interaction"
---

<p><code>XmTrackingEvent</code> &#8212; A Toolkit function that provides a modal interaction</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Widget XmTrackingEvent</code>(
<code>Widget widget</code>,
<code>Cursor cursor</code>,
<code>Boolean confine_to</code>,
<code>XEvent *event_return</code>);</pre>
<h2>Description</h2>
<p><code>XmTrackingEvent</code> provides a modal interface for selection of a component. It is intended to support context help. The function calls the <code>XmUpdateDisplay</code> function. <code>XmTrackingEvent</code> then grabs the pointer and discards succeeding events until <code>BSelect</code> is released or a key is pressed and then released. The function then returns the widget or gadget that contains the pointer when <code>BSelect</code> is released or a key is released, and ungrabs the pointer.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the widget ID of a widget to use as the basis of the modal interaction. That is, the widget within which the interaction must occur, usually a top-level shell.</p>
<dt><i>cursor</i></p>
<dd>Specifies the cursor to be used for the pointer during the interaction. This is a standard X cursor name.</p>
<dt><i>confine_to</i></p>
<dd>Specifies whether or not the cursor should be confined to <i>widget</i>.</p>
<dt><i>event_return</i></p>
<dd>Returns the ButtonRelease or KeyRelease event that causes the function to return.</dl>
<h2>Return</h2>
<p>Returns the widget or gadget that contains the pointer when <code>BSelect</code> is released or a key is released. If no widget or gadget contains the pointer, the function returns NULL.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtrackinglocate/">XmTrackingLocate</a></code>(3).</p>
