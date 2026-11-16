---
title: "dpmsinfo(3)"
name: "dpmsinfo"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpmsinfo/"
description: "DPMSInfo – returns information about the current DPMS state"
---

<p>DPMSInfo &#8211; returns information about the current DPMS state </p>
<h2>Synopsis</h2>
<pre><code>cc</code> [ <i>flag</i> ... ] <i>file</i> ... -<code>lXext</code> [ <i>library</i> ... ]
#include &lt;X11/extensions/dpms.h&gt;
<dl COMPACT><dt><code>Status DPMSInfo</code>
(
</dt><dd>Display <i>*display</i>,
</dd><dd>CARD16 <i>*power_level</i>,
</dd><dd>BOOL <i>*state</i>
);
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dd></dl></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></dt>
<dd>
</dd><dd>Specifies the connection to the X server</dd>
<dt><i>power_level</i></dt>
<dd>Specifies the current power level</dd>
<dt><i>state</i></dt>
<dd>Specifies the current DPMS state</dd></dl>
<h2>Description</h2>
<p>The <i>DPMSInfo</i> function returns information about the current Display Power Management Signaling (DPMS) state. The <i>state</i> return parameter indicates whether or not DPMS is enabled (TRUE) or disabled (FALSE). The <i>power_level</i> return parameter indicates the current power level (one of DPMSModeOn, DPMSModeStandby, DPMSModeSuspend, or DPMSModeOff.)</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>TRUE</dt>
<dd>The <i>DPMSInfo</i> function returns TRUE, if values are returned.</dd>
<dt>FALSE</dt>
<dd>The <i>DPMSInfo</i> function returns FALSE, if no values are returned.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dpmsenable/">DPMSEnable</a></code>(3)</p>
