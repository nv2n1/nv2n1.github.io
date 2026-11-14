---
title: "dmxgetscreenattributes(3)"
name: "dmxgetscreenattributes"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dmxgetscreenattributes/"
description: "DMXGetScreenAttributes – determine back-end screen attributes"
---

<p>DMXGetScreenAttributes &#8211; determine back-end screen attributes</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/X11/extensions/dmxext.h">X11/extensions/dmxext.h</a>&gt;</code> </p>
<pre><code>Bool DMXGetScreenAttributes(Display </code><i>*dpy</i><code>,</code>
<code> int </code><i>screen</i><code>,</code>
<code> DMXScreenAttributes </code><i>*attr</i><code>);</code></pre>
<h2>Description</h2>
<p><code>DMXGetScreenAttributes()</code> returns the attributes for the single DMX screen specified in <i>screen</i>. </p>
<p> The <i>DMXScreenAttributes</i> structure is: </p>
<pre>typedef struct {
 char *displayName;
 int logicalScreen;
 unsigned int screenWindowWidth;
 unsigned int screenWindowHeight;
 int screenWindowXoffset;
 int screenWindowYoffset;
 unsigned int rootWindowWidth;
 unsigned int rootWindowHeight;
 int rootWindowXoffset;
 int rootWindowYoffset;
 int rootWindowXorigin;
 int rootWindowYorigin;
} DMXScreenAttributes;</pre>
<p><i>displayName</i> is the name used to open the display, either from the <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1) command-line or from the configuration file. </p>
<p> <i>logicalScreen</i> is the value of the screen that that <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1) server exports to clients. When Xinerama is in use, this value is typically 0 for all values of physicalScreen. If Xinerama is in use, <i>rootWindowXorigin</i> and <i>rootWindowYorigin</i> specify where the physical screen is positioned in the global Xinerama coordinate system. Otherwise, these values are set to 0. </p>
<p> <i>screenWindowWidth</i>, <i>screenWindowHeight</i>, <i>screenWindowXoffset</i>, and <i>screenWindowYoffset</i> are a geometry specification (see <code><a href="//www.systutorials.com/docs/linux/man/7x-X/">X</a></code>(7x)) for the location of the DMX screen on the back-end screen. The coordinant system of the back-end display is used for these values. </p>
<p> <i>rootWindowWidth</i>, <i>rootWindowHeight</i>, <i>rootWindowXoffset</i>, and <i>rootWindowYoffset</i> are a geometry specification (see <code><a href="//www.systutorials.com/docs/linux/man/7x-X/">X</a></code>(7x)) for the location of the root window on the screen window. The coordinant system of the screen window is used. In most cases, the root window will have the same geometry as the DMX screen window, and will occupy the same area of the back-end display. (This would not be the case, for example, if automatic projector alignment is used.)</p>
<h2>Return Value</h2>
<p><code>DMXGetScreenAttributes()</code> returns <code>True</code> unless there is a protocol error. </p>
<p> <code>DMXGetScreenAttributes()</code> can generate <code>BadValue</code> errors.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dmxgetscreencount/">DMXGetScreenCount</a></code>(3), <code><a href="/docs/linux/man/3-dmxchangescreenattributes/">DMXChangeScreenAttributes</a></code>(3), <code><a href="/docs/linux/man/3-dmx/">DMX</a></code>(3), <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1)</p>
