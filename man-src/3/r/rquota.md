---
title: "rquota(3)"
name: "rquota"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rquota/"
description: "rquota – implement quotas on remote machines"
---

<p>rquota &#8211; implement quotas on remote machines</p>
<h2>Protocol</h2>
<p><code>/usr/include/rpcsvc/rquota.x</code></p>
<h2>Description</h2>
<p> The <code>rquota()</code> protocol inquires about quotas on remote machines. It is used in conjunction with <font SIZE="-1">NFS</font>, since <font SIZE="-1">NFS</font> itself does not implement quotas.</p>
<h2>Programming</h2>
<p><code>#include &lt;rpcsvc/rquota.h&gt;</code> </p>
<p> The following <font SIZE="-1">XDR</font> routines are available in <code>librpcsvc</code>: </p>
<pre><code>xdr_getquota_arg</code>
<code>xdr_getquota_rslt</code>
<code>xdr_rquota</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-quota/">quota</a></code>(1), <code><a href="/docs/linux/man/2-quotactl/">quotactl</a></code>(2) </p>
