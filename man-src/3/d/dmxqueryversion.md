---
title: "dmxqueryversion(3)"
name: "dmxqueryversion"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dmxqueryversion/"
description: "DMXQueryVersion – determine DMX extension version"
---

<p>DMXQueryVersion &#8211; determine DMX extension version</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/X11/extensions/dmxext.h">X11/extensions/dmxext.h</a>&gt;</code> </p>
<pre><code>Bool DMXQueryVersion(Display </code><i>*dpy</i><code>,</code>
<code> int </code><i>*major_version</i><code>,</code>
<code> int </code><i>*minor_version</i><code>,</code>
<code> int </code><i>*patch_version</i><code>);</code></pre>
<h2>Description</h2>
<p><code>DMXQueryVersion()</code> returns version information about the DMX protocol extension. </p>
<p> Any incompatible changes to the protocol will be indicated by a change in <i>major_version</i>. Small, upward-compatible changes will be indicated by a change in <i>minor_version</i>. In general, <i>patch_version</i> is for informational purposes and will encode the date of the last protocol revision (e.g., 20040604).</p>
<h2>Return Value</h2>
<p>If the DMX protocol extension is available, <i>major_version</i>, <i>minor_version</i>, and <i>patch_version</i> will be set, and <code>True</code> will be returned. Otherwise, <code>False</code> will be returned.</p>
<h2>Notes</h2>
<p>At the time of this writing, the DMX protocol is at version 2.2. </p>
<p> Version 2.2 was the final development version, and code supporting this version was submitted to upstream X server repositories in the summer of 2004. </p>
<p> Version 1.5 was the last of the 1.x series, which was used for development before screen and input addition and removal were supported. Version 2.0 and 2.1 were development versions that partially supported screen and input addition and removal. </p>
<p> Since we do not expect development versions to be widely used, we recommend that any software that uses the DMX protocol extension to support only versions 2.2 and above (although they should detect earlier versions and either reduce functionality or fail gracefully).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dmxqueryextension/">DMXQueryExtension</a></code>(3), <code><a href="/docs/linux/man/3-dmx/">DMX</a></code>(3), <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1)</p>
