---
title: "dmxgetwindowattributes(3)"
name: "dmxgetwindowattributes"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dmxgetwindowattributes/"
description: "DMXGetWindowAttributes – determine back-end window attributes"
---

<p>DMXGetWindowAttributes &#8211; determine back-end window attributes</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/X11/extensions/dmxext.h">X11/extensions/dmxext.h</a>&gt;</code> </p>
<pre><code>Bool DMXGetWindowAttributes(Display </code><i>*dpy</i><code>,</code>
<code> Window </code><i>window</i><code>,</code>
<code> int </code><i>*screen_count</i><code>,</code>
<code> int </code><i>available_count</i><code>,</code>
<code> DMXWindowAttributes </code><i>*attr</i><code>);</code></pre>
<h2>Description</h2>
<p>When calling <code>DMXGetWindowAttributes()</code>, <i>window</i> specifies the window ID of a window on the <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1) server and <i>available_count</i> specifies the length of <i>attr.</i> </p>
<p> The number of screens for which information is available will be returned in <i>screen_count</i> and information about those screen will be returned in <i>attr</i>. If <i>screen_count</i> is less than <i>available_count</i>, then information for all of the screens will be returned. Otherwise, information for the first <i>available_count</i> screens will be returned. </p>
<p> The <i>DMXWindowAttributes</i> structure is: </p>
<pre>typedef struct {
 int screen;
 Window window;
 XRectangle pos, vis;
} DMXWindowAttributes;</pre>
<p>For each back-end X server that displays a portion of <i>window</i>, this structure contains the physical <i>screen</i> containing that portion, the <i>window</i> ID on the back-end X server of the window containing that portion, the position and dimensions of the window on the back-end (<i>pos</i>, in screen coordinates), and the visible area of the window on the back-end (<i>vis</i>, in window-relative coordinates &#8212; all zeros if the window is not visible on the backend). </p>
<p> To obtain more information about the physical screen use the <code><a href="/docs/linux/man/3-dmxgetscreenattributes/">DMXGetScreenAttributes</a></code>(3) call. </p>
<p> Note that DMX allows multiple back-end windows to overlap in their view of the DMX logical window. Further, a logical window does not have to be completely covered by back-end windows &#8212; there may be gaps. </p>
<p> As an example, consider a 500&#215;500 window that spans the top two 1024&#215;768 back-end displays (A and B) of a 2048&#215;1536 DMX display composed of 4 1024&#215;768 back-end displays arranged in a cube: </p>
<pre> A B
 C D</pre>
<p>In this case, the DMXGetWindowAttributes call would return the following information for the 500&#215;500 window: </p>
<pre>display A: 500x500 window at 1024-250,0 (relative to back end)
 with 250x500 visible at 0,0 (relative to window origin)
display B: 500x500 window at -250,0 (relative to back end)
 with 250x500 visible at 250,0 (relative to window origin)
display C: 500x500 window at 1024-250,-768 with 0x0 visible at 0,0
display D: 500x500 window at -250,-768 with 0x0 visible at 0,0</pre>
<h2>Return Value</h2>
<p><code>DMXGetWindowAttributes()</code> returns <code>True</code> unless there is a protocol error. </p>
<p> <code>DMXGetWindowAttributes()</code> can generate <code>BadWindow</code> and <code>BadAlloc</code> errors.</p>
<h2>Notes</h2>
<p>Because this call transports a great deal of information over the wire, please call <code><a href="/docs/linux/man/3-dmxgetscreencount/">DMXGetScreenCount</a></code>(3) first, and make sure <i>attr</i> is sufficiently large. </p>
<p> On a particular back-end server, it is possible that the associated window has not yet been mapped because the <code><a href="/docs/linux/man/3-xmapwindow/">XMapWindow</a></code>(3) call that will eventually map the window had been buffered by Xlib&#8217;s normal buffering system. To avoid this race condition, please call <code><a href="/docs/linux/man/3-dmxsync/">DMXSync</a></code>(3) before communicating directly with the back-end X server.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dmxgetscreencount/">DMXGetScreenCount</a></code>(3), <code><a href="/docs/linux/man/3-dmxsync/">DMXSync</a></code>(3), <code><a href="/docs/linux/man/3-dmxgetscreenattributes/">DMXGetScreenAttributes</a></code>(3), <code><a href="/docs/linux/man/3-dmx/">DMX</a></code>(3), <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1)</p>
