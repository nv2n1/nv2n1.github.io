---
title: "dmxgetinputcount(3)"
name: "dmxgetinputcount"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dmxgetinputcount/"
description: "DMXGetInputCount – determine number of input devices"
---

<p>DMXGetInputCount &#8211; determine number of input devices</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/X11/extensions/dmxext.h">X11/extensions/dmxext.h</a>&gt;</code> </p>
<pre><code>Bool DMXGetInputCount(Display </code><i>*dpy</i><code>,</code>
<code> int </code><i>*input_count</i><code>);</code></pre>
<h2>Description</h2>
<p><code>DMXGetInputCount()</code> returns the number of input devices connected to the <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1) server in <i>input_count</i>. This number is the same as that returned by <code><a href="/docs/linux/man/3-xlistinputdevices/">XListInputDevices</a></code>(3), but is available even when the XInput extension is not supported.</p>
<h2>Return Value</h2>
<p><code>DMXGetInputCount()</code> returns <code>True</code> unless there is a protocol error.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dmxgetinputattributes/">DMXGetInputAttributes</a></code>(3), <code><a href="/docs/linux/man/3-xlistinputdevices/">XListInputDevices</a></code>(3), <code><a href="/docs/linux/man/3-dmx/">DMX</a></code>(3), <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1)</p>
