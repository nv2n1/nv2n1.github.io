---
title: "xfilterevent(3)"
name: "xfilterevent"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xfilterevent/"
description: "XFilterEvent – filter X events for an input method"
---

<p>XFilterEvent &#8211; filter X events for an input method </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Bool XFilterEvent(XEvent *<i>event</i>, Window <i>w</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>event</i></p>
<dd>Specifies the event to filter.</p>
<dt><i>w</i></p>
<dd>Specifies the window for which the filter is to be applied.</dl>
<h2>Description</h2>
<p>If the window argument is <code>None</code>, <code>XFilterEvent</code> applies the filter to the window specified in the <code>XEvent</code> structure. The window argument is provided so that layers above Xlib that do event redirection can indicate to which window an event has been redirected. </p>
<p> If <code>XFilterEvent</code> returns <code>True</code>, then some input method has filtered the event, and the client should discard the event. If <code>XFilterEvent</code> returns <code>False</code>, then the client should continue processing the event. </p>
<p> If a grab has occurred in the client and <code>XFilterEvent</code> returns <code>True</code>, the client should ungrab the keyboard.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xnextevent/">XNextEvent</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
