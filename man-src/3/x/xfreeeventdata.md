---
title: "xfreeeventdata(3)"
name: "xfreeeventdata"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xfreeeventdata/"
description: "XGetEventData, XFreeEventData, XGenericEventCookie – retrieve and free additional event data through cookies."
---

<p>XGetEventData, XFreeEventData, XGenericEventCookie &#8211; retrieve and free additional event data through cookies. </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Bool XGetEventData(Display *<i>display</i>, XGenericEventCookie *<i>cookie</i>);</p>
<dd>void XFreeEventData(Display *<i>display</i>, XGenericEventCookie *<i>cookie</i>);</p>
<dt></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>
<dd>Specifies the connection to the X server.</p>
<dt><i>cookie</i></p>
<dd>Specifies the cookie to free or retrieve the data for. </p>
</dl>
<h2>Structures</h2>
<p>typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int type;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long serial;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Bool send_event;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Display&nbsp;*display;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int extension;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int evtype;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int cookie;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;*data; } XGenericEventCookie; </p>
<h2>Description</h2>
<p>Some extension <code>XGenericEvents</code> require additional memory to store information. For these events, the library returns a <code>XGenericEventCookie</code> with a token (&#8216;cookie&#8217;) unique to this event. The <code>XGenericEventCookie</code>&#8216;s data pointer is undefined until <code>XGetEventData</code> is called. </p>
<p> The <code>XGetEventData</code> function retrieves this extra data for the given cookie. No round-trip to the server is required. If the cookie is invalid or the event is not an event handled by cookie handlers, <code>False</code> is returned. If <code>XGetEventData</code> returns <code>True</code>, the cookie&#8217;s data pointer points to the memory containing the event information. A client must call <code>XFreeEventData</code> to free this memory. <code>XGetEventData</code> returns <code>False</code> for multiple calls for the same event cookie. </p>
<p> The <code>XFreeEventData</code> function frees the data associated with a cookie. A client must call <code>XFreeEventData</code> for each cookie claimed with <code>XGetEventData</code>. </p>
<h2>Example Code</h2>
<p>XEvent event; XGenericEventCookie *cookie = &amp;ev; </p>
<p> XNextEvent(display, &amp;event); if (XGetEventData(display, cookie)) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_cookie_event(cookie-&gt;data); } else<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_event(&amp;event); } XFreeEventData(display, cookie); </p>
<h2>Notes</h2>
<p>A cookie is defined as unclaimed if it has been returned to the client through <code>XNextEvent</code> but its data has not been retrieved via <code>XGetEventData</code>. Subsequent calls to <code>XNextEvent</code> may free memory associated with unclaimed cookies. Multi-threaded X clients must ensure that <code>XGetEventData</code> is called before the next call to <code>XNextEvent</code>. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xnextevent/">XNextEvent</a>(3),<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
