---
title: "dmxqueryextension(3)"
name: "dmxqueryextension"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dmxqueryextension/"
description: "DMXQueryExtension – determine if DMX is available"
---

<p>DMXQueryExtension &#8211; determine if DMX is available</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/X11/extensions/dmxext.h">X11/extensions/dmxext.h</a>&gt;</code> </p>
<pre><code>Bool DMXQueryExtension(Display </code><i>*dpy</i><code>,</code>
<code> int </code><i>*event_basep</i><code>,</code>
<code> int </code><i>*error_basep</i><code>);</code></pre>
<h2>Description</h2>
<p><code>DMXQueryExtension()</code> determines if the DMX protocol extension is available. It will be available if the server is an <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1) server.</p>
<h2>Return Value</h2>
<p>If the DMX protocol extension is available, <i>event_basep</i> and <i>error_basep</i> will be set to the event and error bases, respectively, and <code>True</code> will be returned. Otherwise, <code>False</code> will be returned.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dmxqueryversion/">DMXQueryVersion</a></code>(3), <code><a href="/docs/linux/man/3-dmx/">DMX</a></code>(3), <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1)</p>
