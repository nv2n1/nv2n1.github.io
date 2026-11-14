---
title: "ipsec_pf_key(8)"
name: "ipsec_pf_key"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec_pf_key/"
description: "ipsec_pf_key – shows pfkey messages emitted by the kernel when using the KLIPS or MAST stack."
---

<p>ipsec_pf_key &#8211; shows pfkey messages emitted by the kernel when using the KLIPS or MAST stack.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pf_key</code> &#8211;ah &#8211;esp &#8211;ipip &#8211;ipcomp &#8211;daemon <i>filehmac-md5-96</i> | <i>hmac-sha1-96</i></dl>
<h2>Stack</h2>
<dd>Note that pf_key is only supported on the KLIPS and MAST stacks. It is not supported on any other stack.</p>
<h2>Description</h2>
<p><code>pf_key</code> is a program to open a PF_KEY socket and print all messages that are received from it. With no options, it will register itself to receive key requests for AH, ESP, IPIP and IPCOMP security associations. If given more specific options, then it will listen only to those protocols which are listed. </p>
<p> If the messages are recognized, the messages will be decoded. </p>
<p> If the option <code>&#8211;daemon</code> is provided, then after doing the registrations, the program will fork into the background. The provided file will be opened and the process ID of the background process will be written to it. This option is present to present race conditions in regression testing.</p>
<h2>Files</h2>
<p>/proc/net/pf_key</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pf_key/">pf_key</a></code>(5), <code><a href="/docs/linux/man/8-ipsec/">ipsec</a></code>(8), <code><a href="/docs/linux/man/5-ipsec_eroute/">ipsec_eroute</a></code>(5), <code><a href="/docs/linux/man/5-ipsec_spi/">ipsec_spi</a></code>(5), <code><a href="/docs/linux/man/5-ipsec_spigrp/">ipsec_spigrp</a></code>(5), <code><a href="/docs/linux/man/5-ipsec_klipsdebug/">ipsec_klipsdebug</a></code>(5), <code><a href="/docs/linux/man/8-ipsec_tncfg/">ipsec_tncfg</a></code>(8), <code><a href="/docs/linux/man/5-ipsec_version/">ipsec_version</a></code>(5)</p>
<h2>History</h2>
<p>Written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org/">http://www.freeswan.org/</a></code>m[]&gt; by Michael Richardson &lt;mcr [at] freeswan.org&gt;</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
