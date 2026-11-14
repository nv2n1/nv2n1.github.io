---
title: "dmxchangedesktopattributes(3)"
name: "dmxchangedesktopattributes"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dmxchangedesktopattributes/"
description: "DMXChangeDesktopAttributes – change global bounding box"
---

<p>DMXChangeDesktopAttributes &#8211; change global bounding box</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/X11/extensions/dmxext.h">X11/extensions/dmxext.h</a>&gt;</code> </p>
<pre><code>int DMXChangeDesktopAttributes(Display </code><i>*dpy</i><code>,</code>
<code> unsigned int </code><i>mask</i><code>,</code>
<code> DMXDesktopAttributes </code><i>*attr</i><code>);</code></pre>
<h2>Description</h2>
<p><code>DMXChangeDesktopAttributes()</code> resizes the bounding box of the whole screen when using the Xinerama extension. Otherwise, it has no effect on the screen layout. An attribute mask is placed in <i>mask</i> and the attributes to change are placed in <i>attr</i>. </p>
<p> The values that are used to compute <i>mask</i> are as follows: </p>
<pre>DMXDesktopWidth
DMXDesktopHeight
DMXDesktopShiftX
DMXDesktopShiftY</pre>
<p>The <code>DMXDesktopAttributes</code> structure is: </p>
<pre>typedef struct {
 unsigned int width;
 unsigned int height;
 int shiftX;
 int shiftY;
} DMXDesktopAttributes;</pre>
<p><i>width and height</i> specify the new width and height for the bounding box. <i>shiftX and shiftY</i> specify where the Xinerama origin will be placed with respect to the origin of the new bounding box. This allows the left and upper edges of the bounding box to be changed without changing the visual position of the windows on the desktop. If <i>width or height</i> is not specified, the current values will be used. If <i>shiftX or shiftY</i> is not specified, 0 will be used. </p>
<p> All coordinants are in the global DMX coordinant system. If Xinerama is not active, an error will be generated.</p>
<h2>Return Value</h2>
<p><code>DMXChangeDesktopAttributes()</code> will return 0 on success, <code>DmxBadXinerama</code> if Xinerama is not active, <code>DmxBadValue</code> if the size of the bounding box is too large, and <code>DmxBadReply</code> if there was a protocol error. </p>
<p> <code>DMXChangeDesktopAttributes()</code> can generate <code>BadLength</code> (if the request is malformed, which should never happen when using this library interface), and <code>BadValue</code> (if any values are out of range).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dmxgetdesktopattributes/">DMXGetDesktopAttributes</a></code>(3), <code><a href="/docs/linux/man/3-dmx/">DMX</a></code>(3), <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1)</p>
