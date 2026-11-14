---
title: "dmxgetscreencount(3)"
name: "dmxgetscreencount"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dmxgetscreencount/"
description: "DMXGetScreenCount – determine number of back-end screens"
---

<p>DMXGetScreenCount &#8211; determine number of back-end screens</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/X11/extensions/dmxext.h">X11/extensions/dmxext.h</a>&gt;</code> </p>
<pre><code>Bool DMXGetScreenCount(Display </code><i>*dpy</i><code>,</code>
<code> int </code><i>*screen_count</i><code>);</code></pre>
<h2>Description</h2>
<p><code>DMXGetScreenCount()</code> returns the number of back-end screens that a <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1) server controls. Since a DMX screen usually fills all of the available area on a back-end server, there is usually a one-to-one correspondence between DMX screens and backend servers. However, it is also possible for a DMX screen to cover only part of the available area on a back-end server, and for more than one DMX screens to occupy different parts of the visible area on the same back-end server. </p>
<p> A DMX screen may be managed as a regular X screen in the <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1) server or may be joined with other DMX screens using Xinerama.</p>
<h2>Return Value</h2>
<p><code>DMXGetScreenCount()</code> sets <i>screen_count</i> and returns <code>True</code> unless there is a protocol error.</p>
<h2>Notes</h2>
<p>If Xinerama is active, only one logical screen will be available to clients of the <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1) server. However, this call will accurately reflect the number of composite back-end screens that the <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1) server is using.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dmxgetscreenattribtues/">DMXGetScreenAttribtues</a></code>(3), <code><a href="/docs/linux/man/3-dmxchangescreenattributes/">DMXChangeScreenAttributes</a></code>(3), <code><a href="/docs/linux/man/3-dmx/">DMX</a></code>(3), <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1)</p>
