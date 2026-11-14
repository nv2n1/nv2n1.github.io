---
title: "dmxsync(3)"
name: "dmxsync"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dmxsync/"
description: "DMXSync – flush protocol requests between Xdmx and back-end X servers"
---

<p>DMXSync &#8211; flush protocol requests between Xdmx and back-end X servers</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/X11/extensions/dmxext.h">X11/extensions/dmxext.h</a>&gt;</code> </p>
<pre><code>Bool DMXSync(Display </code><i>*dpy</i><code>);</code></pre>
<h2>Description</h2>
<p><code>DMXSync()</code> flushes all pending protocol requests between the <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1) server and each back-end X server. It is used by clients that talk directly to back-end X servers to ensure that all pending <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1) requests have reached all back-end servers and have been processed by those servers.</p>
<h2>Return Value</h2>
<p><code>DMXSync()</code> returns <code>True</code> unless there is a protocol error.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dmx/">DMX</a></code>(3), <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1)</p>
