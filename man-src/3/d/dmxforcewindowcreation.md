---
title: "dmxforcewindowcreation(3)"
name: "dmxforcewindowcreation"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dmxforcewindowcreation/"
description: "DMXForceWindowCreation – force immediate back-end window creation"
---

<p>DMXForceWindowCreation &#8211; force immediate back-end window creation</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/X11/extensions/dmxext.h">X11/extensions/dmxext.h</a>&gt;</code> </p>
<pre><code>Bool DMXForceWindowCreation(Display </code><i>*dpy</i><code>,</code>
<code> Window </code><i>window</i><code>);</code></pre>
<h2>Description</h2>
<p>When using the lazy window creation optimization, windows are not created on the back-end X servers until they are required. <code>DMXForceWindowCreation()</code> forces the immediate creation of the window requested.</p>
<h2>Return Value</h2>
<p><code>DMXForceWindowCreation()</code> returns <code>True</code> unless there is a protocol error. <code>DMXForceWindwoCreation()</code> can generate <code>BadWindow</code> errors.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dmx/">DMX</a></code>(3), <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1)</p>
