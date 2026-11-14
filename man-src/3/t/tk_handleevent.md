---
title: "tk_handleevent(3)"
name: "tk_handleevent"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_handleevent/"
description: "Tk_HandleEvent – invoke event handlers for window system events"
---

<p>Tk_HandleEvent &#8211; invoke event handlers for window system events </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_HandleEvent</code>(<i>eventPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>XEvent <i>*eventPtr</i> (in) Pointer to X event to dispatch to relevant handler(s). It is important that all unused fields of the structure be set to zero. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_HandleEvent</code> is a lower-level procedure that deals with window events. It is called by <code>Tcl_ServiceEvent</code> (and indirectly by <code>Tcl_DoOneEvent</code>), and in a few other cases within Tk. It makes callbacks to any window event handlers (created by calls to <code>Tk_CreateEventHandler</code>) that match <i>eventPtr</i> and then returns. In some cases it may be useful for an application to bypass the Tk event queue and call <code>Tk_HandleEvent</code> directly instead of calling <code>Tcl_QueueEvent</code> followed by <code>Tcl_ServiceEvent</code>. </p>
<p> This procedure may be invoked recursively. For example, it is possible to invoke <code>Tk_HandleEvent</code> recursively from a handler called by <code>Tk_HandleEvent</code>. This sort of operation is useful in some modal situations, such as when a notifier has been popped up and an application wishes to wait for the user to click a button in the notifier before doing anything else. </p>
<h2>Keywords</h2>
<p>callback, event, handler, window</p>
