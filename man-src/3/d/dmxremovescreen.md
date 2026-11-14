---
title: "dmxremovescreen(3)"
name: "dmxremovescreen"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dmxremovescreen/"
description: "DMXRemoveScreen – detach a back-end screen"
---

<p>DMXRemoveScreen &#8211; detach a back-end screen</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/X11/extensions/dmxext.h">X11/extensions/dmxext.h</a>&gt;</code> </p>
<pre><code>Bool DMXRemoveScreen(Display </code><i>*dpy</i><code>,</code>
<code> int </code><i>screen</i><code>);</code></pre>
<h2>Description</h2>
<p><code>DMXRemoveScreen()</code> detaches the back-end <i>screen</i> from the <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1) server.</p>
<h2>Return Value</h2>
<p><code>DMXRemoveScreen()</code> returns <code>True</code> on success, and <code>False</code> if there were protocol errors, if the <i>-addremovescreens</i> command-line option was not specified on the <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1) command line, if the value of <i>screen</i> is out of range, or if the back-end screen specified by <i>screen</i> has already been detached.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dmxaddscreen/">DMXAddScreen</a></code>(3), <code><a href="/docs/linux/man/3-dmx/">DMX</a></code>(3), <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1)</p>
