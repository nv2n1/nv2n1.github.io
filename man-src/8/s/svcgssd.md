---
title: "svcgssd(8)"
name: "svcgssd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-svcgssd/"
description: "rpc.svcgssd – server-side rpcsec_gss daemon"
---

<p>rpc.svcgssd &#8211; server-side rpcsec_gss daemon</p>
<h2>Synopsis</h2>
<p><code>rpc.svcgssd [-n] [-v] [-r] [-i] [-f] [-p principal]</code></p>
<h2>Description</h2>
<p>The rpcsec_gss protocol gives a means of using the gss-api generic security api to provide security for protocols using rpc (in particular, nfs). Before exchanging any rpc requests using rpcsec_gss, the rpc client must first establish a security context with the rpc server. The linux kernel&#8217;s implementation of rpcsec_gss depends on the userspace daemon <code>rpc.svcgssd</code> to handle context establishment on the rpc server. The daemon uses files in the proc filesystem to communicate with the kernel. </p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></p>
<dd>Runs <code>rpc.svcgssd</code> in the foreground and sends output to stderr (as opposed to syslogd)</p>
<dt><code>-v</code></p>
<dd>Increases the verbosity of the output (can be specified multiple times).</p>
<dt><code>-r</code></p>
<dd>If the rpcsec_gss library supports setting debug level, increases the verbosity of the output (can be specified multiple times).</p>
<dt><code>-i</code></p>
<dd>If the nfsidmap library supports setting debug level, increases the verbosity of the output (can be specified multiple times).</p>
<dt><code>-p</code></p>
<dd>Use <i>principal</i> instead of the default nfs/<i>FQDN</i>@<i>REALM</i>.</p>
<dt><code>-n</code></p>
<dd>Use the system default credentials (host/<i>FQDN</i>@<i>REALM</i>) rather than the default nfs/<i>FQDN</i>@<i>REALM</i>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rpc-gssd/">rpc.gssd</a>(8),</code></p>
<h2>Authors</h2>
<p>Dug Song &lt;dugsong [at] umich.edu&gt;<br />
 Andy Adamson &lt;andros [at] umich.edu&gt;<br />
 Marius Aamodt Eriksen &lt;marius [at] umich.edu&gt;<br />
 J. Bruce Fields &lt;bfields [at] umich.edu&gt;</p>
