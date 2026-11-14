---
title: "dmxremoveinput(3)"
name: "dmxremoveinput"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dmxremoveinput/"
description: "DMXRemoveInput – detach an input"
---

<p>DMXRemoveInput &#8211; detach an input</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/X11/extensions/dmxext.h">X11/extensions/dmxext.h</a>&gt;</code> </p>
<pre><code>Bool DMXRemoveInput(Display </code><i>*dpy</i><code>,</code>
<code> int </code><i>id</i><code>);</code></pre>
<h2>Description</h2>
<p><code>DMXRemoveInput()</code> detaches the input device with <i>id</i>, and all associated inputs (e.g., if the <i>id</i> is a backend mouse, and a keyboard is also attached to the backend, then both devices will be detached).</p>
<h2>Return Value</h2>
<p><code>DMXRemoveInput()</code> returns <code>True</code> unless there is a protocol error. </p>
<p> <code>DMXRemoveInput()</code> can generate <code>BadValue</code> (if the <i>id</i> is not valid) and <code>BadAccess</code> (if the input has already been detached).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dmxaddinput/">DMXAddInput</a></code>(3), <code><a href="/docs/linux/man/3-dmx/">DMX</a></code>(3), <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1)</p>
