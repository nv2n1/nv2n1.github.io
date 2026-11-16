---
title: "dpmsgettimeouts(3)"
name: "dpmsgettimeouts"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpmsgettimeouts/"
description: "DPMSGetTimeouts – retrieves the timeout values used by the X server for DPMS timings"
---

<p>DPMSGetTimeouts &#8211; retrieves the timeout values used by the X server for DPMS timings </p>
<h2>Synopsis</h2>
<pre><code>cc</code> [ <i>flag</i> ... ] <i>file</i> ... -<code>lXext</code> [ <i>library</i> ... ]
#include &lt;X11/extensions/dpms.h&gt;
<dl COMPACT><dt><code>Bool DPMSGetTimeouts</code>
(
</dt><dd>Display *<i>display</i>,
</dd><dd>CARD16 *<i>standby</i>,
</dd><dd>CARD16 *<i>suspend</i>,
</dd><dd>CARD16 *<i>off</i>
);
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dd></dl></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></dt>
<dd>
</dd><dd>Specifies the connection to the X server</dd>
<dt><i>standby</i></dt>
<dd>Specifies the current standby timeout in seconds</dd>
<dt><i>suspend</i></dt>
<dd>Specifies the current suspend timeout in seconds</dd>
<dt><i>off</i></dt>
<dd>Specifies the current off timeout in seconds</dd></dl>
<h2>Description</h2>
<p>The <i>DPMSGetTimeouts</i> function retrieves the timeout values used by the X server for DPMS timings. </p>
<p> The value <i>standby</i> is the amount of time of inactivity in seconds before standby mode is invoked. A value of zero indicates that this mode has been disabled. </p>
<p> The value <i>suspend</i> is the amount of time of inactivity in seconds before the second level of power savings is invoked. A value of zero indicates that this mode has been disabled. </p>
<p> The value <i>off</i> is the amount of time of inactivity in seconds before the third and final level of power savings is invoked. A value of zero indicates that this mode has been disabled.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>TRUE</dt>
<dd>The <i>DPMSGetTimeouts</i> function returns TRUE when values are returned.</dd>
<dt>FALSE</dt>
<dd>The <i>DPMSGetTimeouts</i> function returns FALSE when no values returned.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dpmscapable/">DPMSCapable</a></code>(3), <code><a href="/docs/linux/man/3-dpmsinfo/">DPMSInfo</a></code>(3), <code><a href="/docs/linux/man/3-dpmssettimeouts/">DPMSSetTimeouts</a></code>(3)</p>
