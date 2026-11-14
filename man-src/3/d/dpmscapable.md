---
title: "dpmscapable(3)"
name: "dpmscapable"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpmscapable/"
description: "DPMSCapable – returns the DPMS capability of the X server"
---

<p>DPMSCapable &#8211; returns the DPMS capability of the X server </p>
<h2>Synopsis</h2>
<pre><code>cc</code> [ <i>flag</i> ... ] <i>file</i> ... -<code>lXext</code> [ <i>library</i> ... ]
#include &lt;X11/extensions/dpms.h&gt;
<dl COMPACT><dt><code>Bool DPMSCapable</code> ( Display *<i>display</i> );
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>
<dd>Specifies the connection to the X server</dl>
<h2>Description</h2>
<p>The <i>DPMSCapable</i> function returns the Display Power Management Signaling (DPMS) capability of the X server, either TRUE (capable of DPMS) or FALSE (incapable of DPMS).</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>DPMSCapable</i> function returns True if the X server is capable of DPMS.</p>
<dt>False</p>
<dd>The <i>DPMSCapable</i> function returns True if the X server is incapable of DPMS. </p>
</dl>
