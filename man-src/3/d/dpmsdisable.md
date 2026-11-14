---
title: "dpmsdisable(3)"
name: "dpmsdisable"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpmsdisable/"
description: "DPMSDisable – disables DPMS on the specified display"
---

<p>DPMSDisable &#8211; disables DPMS on the specified display </p>
<h2>Synopsis</h2>
<pre><code>cc</code> [ <i>flag</i> ... ] <i>file</i> ... -<code>lXext</code> [ <i>library</i> ... ]
#include &lt;X11/extensions/dpms.h&gt;
<dl COMPACT><dt><code>Status DPMSDisable</code> ( Display <i>*display</i> );
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>
<dd>Specifies the connection to the X server</dl>
<h2>Description</h2>
<p>The <i>DPMSDisable</i> function disables Display Power Management Signaling (DPMS) on the specified display. When disabled, DPMS sets the display to DPMSModeOn. If <i>DPMSDisable</i> is invoked on a display with DPMS already disabled or on a display which does not support DPMS, no change is made and no error is returned.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>TRUE</p>
<dd>The <i>DPMSDisable</i> function always returns TRUE.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dpmscapable/">DPMSCapable</a></code>(3), <code><a href="/docs/linux/man/3-dpmsenable/">DPMSEnable</a></code>(3)</p>
