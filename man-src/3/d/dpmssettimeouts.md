---
title: "dpmssettimeouts(3)"
name: "dpmssettimeouts"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpmssettimeouts/"
description: "DPMSSetTimeouts – permits applications to set the timeout values used by the X server for DPMS timings"
---

<p>DPMSSetTimeouts &#8211; permits applications to set the timeout values used by the X server for DPMS timings </p>
<h2>Synopsis</h2>
<pre><code>cc</code> [ <i>flag</i> ... ] <i>file</i> ... -<code>lXext</code> [ <i>library</i> ... ]
#include &lt;X11/extensions/dpms.h&gt;
<dl COMPACT><dt><code>Status DPMSSetTimeouts</code>
(
<dd>Display *<i>display</i>,
<dd>CARD16 <i>standby</i>,
<dd>CARD16 <i>suspend</i>,
<dd>CARD16 <i>off</i>
);
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>
<dd>Specifies the connection to the X server</p>
<dt><i>standby</i></p>
<dd>Specifies the new standby timeout in seconds</p>
<dt><i>suspend</i></p>
<dd>Specifies the new suspend timeout in seconds</p>
<dt><i>off</i></p>
<dd>Specifies the new off timeout in seconds</dl>
<h2>Description</h2>
<p>The DPMSSetTimeouts function permits applications to set the timeout values used by the X server for Display Power Management Signaling (DPMS) timings. </p>
<p> The value <i>standby</i> is the amount of inactivity time, in seconds, before standby mode is invoked. The actual effects of this mode are dependent on the characteristics of the monitor and frame buffer card. Standby mode is implemented by shutting off the horizontal sync signal, and pulsing the vertical sync signal. Standby mode provides the quickest monitor recovery time. Note also that many monitors implement this mode identical to suspend mode. A value of zero disables the standby mode. </p>
<p> The value <i>suspend</i> is the amount of time of inactivity, in seconds, before the second level of power savings is invoked. Suspend mode&#8217;s physical and electrical characteristics are implementation defined. For DPMS compliant hardware, setting the suspend mode is implemented by pulsing the horizontal sync signal and shutting off the vertical sync signal. In general, suspend mode recovery is considered to be slower than standby mode, but faster than off mode. However it may vary from monitor to monitor. As noted above, many monitors implement this mode identical to the standby mode. A value of zero disables this mode. </p>
<p> The value <i>off</i> is the amount of time of inactivity, in seconds, before the third and final level of power savings is invoked. Off mode&#8217;s physical and electrical characteristics are implementation defined. In DPMS compliant hardware, it is implemented by shutting off both horizontal and vertical sync signals, resulting in powering down of the monitor. Recovery time is implementation dependent. Usually the recovery time is very close to the power-up time of the monitor. A value of zero disables this mode. </p>
<p> Chronologically, <i>standby</i> mode occurs before or simultaneously with <i>suspend</i> mode, and <i>suspend</i> mode must occur before or simultaneously with <i>off</i> mode. Therefore, non-zero mode timeout values must be greater than or equal to the timeout values of earlier modes. If inconsistent values are supplied, a BadValue error will result.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>TRUE</p>
<dd>The <i>DPMSSetTimeouts</i> function returns TRUE when the function has succeeded.</dl>
<h2>Errors</h2>
<dl COMPACT>
<dt><font SIZE="-1">BadValue</font></p>
<dd>An argument is out of range.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dpmscapable/">DPMSCapable</a></code>(3), <code><a href="/docs/linux/man/3-dpmsinfo/">DPMSInfo</a></code>(3), <code><a href="/docs/linux/man/3-dpmsgettimeouts/">DPMSGetTimeouts</a></code>(3)</p>
