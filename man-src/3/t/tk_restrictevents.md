---
title: "tk_restrictevents(3)"
name: "tk_restrictevents"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_restrictevents/"
description: "Tk_RestrictEvents – filter and selectively delay X events"
---

<p>Tk_RestrictEvents &#8211; filter and selectively delay X events </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Tk_RestrictProc *
<code>Tk_RestrictEvents</code>(<i>proc, clientData, prevClientDataPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_RestrictProc <i>*proc</i> (in) Predicate procedure to call to filter incoming X events. NULL means do not restrict events at all.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary argument to pass to <i>proc</i>.</p>
<dd>ClientData <i>*prevClientDataPtr</i> (out) Pointer to place to save argument to previous restrict procedure. </p>
</dl>
<h2>Description</h2>
<p>This procedure is useful in certain situations where applications are only prepared to receive certain X events. After <code>Tk_RestrictEvents</code> is called, <code>Tk_DoOneEvent</code> (and hence <code>Tk_MainLoop</code>) will filter X input events through <i>proc</i>. <i>Proc</i> indicates whether a given event is to be processed immediately, deferred until some later time (e.g. when the event restriction is lifted), or discarded. <i>Proc</i> is a procedure with arguments and result that match the type <code>Tk_RestrictProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef Tk_RestrictAction Tk_RestrictProc(
 ClientData <i>clientData</i>,
 XEvent *<i>eventPtr</i>);</pre>
</dl>
<p> The <i>clientData</i> argument is a copy of the <i>clientData</i> passed to <code>Tk_RestrictEvents</code>; it may be used to provide <i>proc</i> with information it needs to filter events. The <i>eventPtr</i> points to an event under consideration. <i>Proc</i> returns a restrict action (enumerated type <code>Tk_RestrictAction</code>) that indicates what <code>Tk_DoOneEvent</code> should do with the event. If the return value is <code>TK_PROCESS_EVENT</code>, then the event will be handled immediately. If the return value is <code>TK_DEFER_EVENT</code>, then the event will be left on the event queue for later processing. If the return value is <code>TK_DISCARD_EVENT</code>, then the event will be removed from the event queue and discarded without being processed. </p>
<p> <code>Tk_RestrictEvents</code> uses its return value and <i>prevClientDataPtr</i> to return information about the current event restriction procedure (a NULL return value means there are currently no restrictions). These values may be used to restore the previous restriction state when there is no longer any need for the current restriction. </p>
<p> There are very few places where <code>Tk_RestrictEvents</code> is needed. In most cases, the best way to restrict events is by changing the bindings with the <code>bind</code> Tcl command or by calling <code>Tk_CreateEventHandler</code> and <code>Tk_DeleteEventHandler</code> from C. The main place where <code>Tk_RestrictEvents</code> must be used is when performing synchronous actions (for example, if you need to wait for a particular event to occur on a particular window but you do not want to invoke any handlers for any other events). The &#8220;obvious&#8221; solution in these situations is to call <code>XNextEvent</code> or <code>XWindowEvent</code>, but these procedures cannot be used because Tk keeps its own event queue that is separate from the X event queue. Instead, call <code>Tk_RestrictEvents</code> to set up a filter, then call <code>Tk_DoOneEvent</code> to retrieve the desired event(s).</p>
<h2>Keywords</h2>
<p>delay, event, filter, restriction</p>
