---
title: "dpmsforcelevel(3)"
name: "dpmsforcelevel"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpmsforcelevel/"
description: "DPMSForceLevel – forces a DPMS capable display into the specified power level"
---

<p>DPMSForceLevel &#8211; forces a DPMS capable display into the specified power level </p>
<h2>Synopsis</h2>
<pre><code>cc</code> [ <i>flag</i> ... ] <i>file</i> ... -<code>lXext</code> [ <i>library</i> ... ]
#include &lt;X11/extensions/dpms.h&gt;
<dl COMPACT><dt><code>Status DPMSForceLevel</code> ( Display <i>*display</i>, CARD16 <i>level</i> );
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt></dl></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></dt>
<dd>
</dd><dd>Specifies the connection to the X server</dd>
<dt><i>level</i></dt>
<dd>Specifies the level to force power to</dd></dl>
<h2>Description</h2>
<p>The <i>DPMSForceLevel</i> function forces a DPMS capable display into the specified power level. The <i>level</i> must be one of following four states: DPMSModeOn, DPMSModeStandby, DPMSModeSuspend, or DPMSModeOff. Values other than these will result in a BadValue error. If DPMS is disabled on the display, trying to set the power level on the display will result in a BadMatch protocol error.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>TRUE</dt>
<dd>The <i>DPMSForceLevel</i> function always returns TRUE.</dd></dl>
<h2>Errors</h2>
<dl COMPACT>
<dt>BadValue</dt>
<dd>A level other than DPMSModeOn, DPMSModeStandby, DPMSModeSuspend, or DPMSModeOff was specified.</dd>
<dt>BadMatch</dt>
<dd>DPMS is disabled on the specified display.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dpmscapable/">DPMSCapable</a></code>(3), <code><a href="/docs/linux/man/3-dpmsinfo/">DPMSInfo</a></code>(3), <code><a href="/docs/linux/man/3-dpmsgettimeouts/">DPMSGetTimeouts</a></code>(3), <code><a href="/docs/linux/man/3-dpmssettimeouts/">DPMSSetTimeouts</a></code>(3)</p>
