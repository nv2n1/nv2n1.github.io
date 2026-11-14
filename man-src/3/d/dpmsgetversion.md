---
title: "dpmsgetversion(3)"
name: "dpmsgetversion"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpmsgetversion/"
description: "DPMSGetVersion – returns the version of the DPMS extension implemented by the X server"
---

<p>DPMSGetVersion &#8211; returns the version of the DPMS extension implemented by the X server </p>
<h2>Synopsis</h2>
<pre><code>cc</code> [ <i>flag</i> ... ] <i>file</i> ... -<code>lXext</code> [ <i>library</i> ... ]
#include &lt;X11/extensions/dpms.h&gt;
<dl COMPACT><dt><code>Status DPMSGetVersion</code>
(
<dd>Display *<i>display</i>,
<dd>int *<i>major_version</i>,
<dd>int *<i>minor_version</i>
);
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>
<dd>Specifies the connection to the X server</p>
<dt><i>major_version</i></p>
<dd>Specifies the return location for the extension major version</p>
<dt><i>minor_version</i></p>
<dd>Specifies the return location for the extension minor version</dl>
<h2>Description</h2>
<p>The <i>DPMSGetVersion</i> function returns the version of the Display Power Management Signaling (DPMS) extension implemented by the X server. It returns a major and minor version number. The major version number will be incremented for protocol incompatible changes, and the minor version number will be incremented for small, upward compatible changes.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>TRUE</p>
<dd>The <i>DPMSGetVersion</i> function returns TRUE when the extension is supported and values are returned.</p>
<dt>FALSE</p>
<dd>The <i>DPMSGetVersion</i> function returns FALSE when the extension is not supported.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dpmscapable/">DPMSCapable</a></code>(3), <code><a href="/docs/linux/man/3-dpmsqueryextension/">DPMSQueryExtension</a></code>(3)</p>
