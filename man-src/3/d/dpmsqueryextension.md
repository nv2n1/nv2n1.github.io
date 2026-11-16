---
title: "dpmsqueryextension(3)"
name: "dpmsqueryextension"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpmsqueryextension/"
description: "DPMSQueryExtension – queries the X server to determine the availability of the DPMS Extension"
---

<p>DPMSQueryExtension &#8211; queries the X server to determine the availability of the DPMS Extension </p>
<h2>Synopsis</h2>
<pre><code>cc</code> [ <i>flag</i> ... ] <i>file</i> ... -<code>lXext</code> [ <i>library</i> ... ]
#include &lt;X11/extensions/dpms.h&gt;
<dl COMPACT><dt><code>Bool DPMSQueryExtension</code>
(
</dt><dd>Display <i>*display</i>,
</dd><dd>int <i>*event_base</i>,
</dd><dd>int <i>*error_base</i>
);
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dd></dl></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></dt>
<dd>
</dd><dd>Specifies the connection to the X server</dd>
<dt><i>event_base</i></dt>
<dd>Specifies the return location for the assigned base event</dd>
<dt><i>error_base</i></dt>
<dd>Specifies the return location for the assigned base error</dd></dl>
<h2>Description</h2>
<p>The <i>DPMSQueryExtension</i> function queries the X server to determine the availability of the Display Power Management Signaling (DPMS) Extension. If the extension is available, it returns TRUE, and the <i>event_base</i> and <i>error_base</i> are set to the base event and error numbers, respectively. Otherwise, the return value is FALSE, and the values of <i>event_base</i> and <i>error_base</i> are undefined.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>TRUE</dt>
<dd>The <i>DPMSQueryExtension</i> function returns TRUE if the extension is available, and <i>event_base</i> and <i>error_base</i> are set to the base event number and base error number for the extension, respectively.</dd>
<dt>FALSE</dt>
<dd>The <i>DPMSQueryExtension</i> function returns FALSE if extension is not available, and the values of <i>event_base</i> and <i>error_base</i> are undefined.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dpmsgetversion/">DPMSGetVersion</a></code>(3)</p>
