---
title: "dmxgetdesktopattributes(3)"
name: "dmxgetdesktopattributes"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dmxgetdesktopattributes/"
description: "DMXGetDesktopAttributes – determine global bounding box"
---

<p>DMXGetDesktopAttributes &#8211; determine global bounding box</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/X11/extensions/dmxext.h">X11/extensions/dmxext.h</a>&gt;</code> </p>
<pre><code>Bool DMXGetDesktopAttributes(Display </code><i>*dpy</i><code>,</code>
<code> DMXDesktopAttributes </code><i>*attr</i><code>);</code></pre>
<h2>Description</h2>
<p><code>DMXGetDesktopAttributes()</code> returns information about the desktop in <code>DMXDesktopAttributes</code>: </p>
<pre>typedef struct {
 unsigned int width;
 unsigned int height;
 int shiftX;
 int shiftY;
} DMXDesktopAttributes;</pre>
<p>The size of the global bounding box is given in <i>width</i>, and <i>height</i>. The <i>shiftX</i> and <i>shiftY</i> values will always be 0. The global bounding box is computed whether or not Xinerama is active, but it is only useful when using Xinerama. </p>
<p> The global bounding box used by <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1) may be larger than the Xinerama screen size because of information in the configuration file.</p>
<h2>Return Value</h2>
<p><code>DMXGetDesktopAttributes()</code> returns <code>True</code> unless there is a protocol error.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dmxchangedesktopattributes/">DMXChangeDesktopAttributes</a></code>(3), <code><a href="/docs/linux/man/3-dmx/">DMX</a></code>(3), <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1)</p>
