---
title: "xevieend(3)"
name: "xevieend"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xevieend/"
description: "Xevie – X Event Interception Extension (XEvIE)"
---

<p>Xevie &#8211; X Event Interception Extension (XEvIE) </p>
<h2>Syntax</h2>
<p>#include &lt;<a href="file:/usr/include/X11/extensions/Xevie.h">X11/extensions/Xevie.h</a>&gt; </p>
<pre>Status XevieQueryVersion (Display *<i>dpy</i>,
 int *<i>major_versionp</i>,
 int *<i>minor_versionp</i>);
Status XevieStart (Display *<i>dpy</i>);
Status XevieSelectInput (Display *<i>dpy</i>,
 long <i>event_mask</i>);
Status XevieSendEvent (Display *<i>dpy</i>,
 XEvent *<i>event</i>,
 char *fIdataType);
Status XevieEnd (Display *<i>dpy</i>);</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>event_mask</i></p>
<dd>Specifies the mask of events to redirect.</p>
<dt><i>datatype</i></p>
<dd>XEVIE_MODIFIED or XEVIE_UNMODIFIED &#8211; whether the Xevie client has changed or synthesised this event. </p>
</dl>
<h2>Description</h2>
<p><code>X Event Interception Extension (XEvIE) </code> is designed for users who need to intercept all the Keyboard and Mouse events. Programs can determine which events should be forwarded to other clients and modify the events if necessary. </p>
<h2>Functions</h2>
<p><code>XevieQueryVersion</code> The XevieQueryVersion function returns the major and minor protocol version numbers supported by the server. XevieQueryVersion returns True if success, otherwise, it returns False. </p>
<p> <code>XevieStart</code> The XevieStart function requests that the X server enable the XEvIE extension. Once XEvIE is successfully enabled, all the XevieSelectInput specified events will be sent to the client which has enabled XEvIE. If XKB or AccessX is enabled, the events that are sent to the XEvIE clients are XKB/AccessX processed (filtered) ones. </p>
<p> <code>XevieSendEvent</code> Events are sent back to the X server through XevieSendEvent. </p>
<p> <code>XevieEnd</code> The XevieEnd function requests that the X server disables the XEvIE extension. Once XEvIE is disabled successfully, the X server stops sending events to the XEvIE client. </p>
<p> <code>XevieSelectInput</code> The XevieSelectInput function requests that the X server reports the keyboard and pointer events associated with the specified event mask. By default, X will report KeyPress, KeyRelease, ButtonPress, ButtonRelease and MotionNotify events. </p>
<h2>Restrictions</h2>
<p><code>Xevie</code> will remain upward compatible after the current 1.0 release.</p>
<h2>Authors</h2>
<p>Derek Wang and Stuart Kreitman, Sun Microsystems, Inc.</p>
