---
title: "dpmsenable(3)"
name: "dpmsenable"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpmsenable/"
description: "DPMSEnable – enables DPMS on the specified display"
---

<p>DPMSEnable &#8211; enables DPMS on the specified display </p>
<h2>Synopsis</h2>
<pre><code>cc</code> [ <i>flag</i> ... ] <i>file</i> ... -<code>lXext</code> [ <i>library</i> ... ]
#include &lt;X11/extensions/dpms.h&gt;
<dl COMPACT><dt><code>Status DPMSEnable</code> ( Display *<i>display</i> );
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>
<dd>Specifies the connection to the X server</dl>
<h2>Description</h2>
<p>The <i>DPMSEnable</i> function enables Display Power Management Signaling (DPMS) on the specified <i>display.</i> When DPMS is enabled, DPMS will use the currently saved timeout values. It will trigger the appropriate DPMS power level based on the timeout values. Refer to <i>DPMSSetTimeouts.</i> All physical screens are affected by <i>DPMSEnable</i> at the same time. </p>
<p> If <i>DPMSEnable</i> is invoked on a display which has DPMS already enabled, or on a display which does not support DPMS, no change is made and no error is returned.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>TRUE</p>
<dd>The <i>DPMSEnable</i> function always returns TRUE.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dpmscapable/">DPMSCapable</a></code>(3), <code><a href="/docs/linux/man/3-dpmsdisable/">DPMSDisable</a></code>(3), <code><a href="/docs/linux/man/3-dpmsgettimeouts/">DPMSGetTimeouts</a></code>(3), <code><a href="/docs/linux/man/3-dpmssettimeouts/">DPMSSetTimeouts</a></code>(3)</p>
