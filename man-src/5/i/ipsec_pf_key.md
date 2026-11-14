---
title: "ipsec_pf_key(5)"
name: "ipsec_pf_key"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ipsec_pf_key/"
description: "ipsec_pf_key – lists PF_KEY sockets registered with KLIPS"
---

<p>ipsec_pf_key &#8211; lists PF_KEY sockets registered with KLIPS</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>cat</code> <i>/proc/net/pf_key</i></dl>
<h2>Stack</h2>
<dd>Note that pf_key is only supported on the KLIPS and MAST stacks. It is not supported on any other stack.</p>
<h2>Description</h2>
<p>/proc/net/pf_key is a read-only file which lists the presently open PF_KEY sockets on the local system and their parameters. </p>
<p> Each line lists one PF_KEY socket. A table entry consists of: </p>
<p> +</p>
<dl>
<dd>sock pointer (sock)</dl>
<p> +</p>
<dl>
<dd>PID of the socket owner (pid)</dl>
<p> +</p>
<dl>
<dd>flag to indicate if the socket is dead (d)</dl>
<p> +</p>
<dl>
<dd>socket wait queue (sleep)</dl>
<p> +</p>
<dl>
<dd>socket pointer (socket)</dl>
<p> +</p>
<dl>
<dd>next socket in chain (next)</dl>
<p> +</p>
<dl>
<dd>previous socket in chain (prev)</dl>
<p> +</p>
<dl>
<dd>last socket error (e)</dl>
<p> +</p>
<dl>
<dd>pointer to destruct routine (destruct)</dl>
<p> +</p>
<dl>
<dd>is this a reused socket (r)</dl>
<p> +</p>
<dl>
<dd>has this socket been zapped (z)</dl>
<p> +</p>
<dl>
<dd>socket family to which this socket belongs (fa)</dl>
<p> +</p>
<dl>
<dd>local port number (n)</dl>
<p> +</p>
<dl>
<dd>protocol version number (p)</dl>
<p> +</p>
<dl>
<dd>Receive queue bytes committed (r)</dl>
<p> +</p>
<dl>
<dd>Transmit queue bytes committed (w)</dl>
<p> +</p>
<dl>
<dd>option memory allocations (o)</dl>
<p> +</p>
<dl>
<dd>size of send buffer in bytes (sndbf)</dl>
<p> +</p>
<dl>
<dd>timestamp in seconds (stamp)</dl>
<p> +</p>
<dl>
<dd>socket flags (Flags)</dl>
<p> +</p>
<dl>
<dd>socket type (Type)</dl>
<p> +</p>
<dl>
<dd>connection state (St)</dl>
<h2>Examples</h2>
<p><code>c3b8c140 3553 0 c0599818 c05997fc 0 0 0 0 1 0 15 0 2 0 0 0 65535 0.103232 00000000 00000003 01</code></p>
<dl>
<dd></dl>
<p> shows that there is one pf_key socket set up that starts at <code>c3b8c140</code>, whose owning process has PID 3553, the socket is not dead, its wait queue is at <code>c0599818</code>, whose owning socket is at <code>c05997fc</code>, with no other sockets in the chain, no errors, no destructor, it is a reused socket which has not been zapped, from protocol family 15 (PF_KEY), local port number 0, protocol socket version 2, no memory allocated to transmit, receive or option queues, a send buffer of almost <code>64kB</code>, a timestamp of 0.103232, no flags set, type 3, in state 1.</p>
<h2>Files</h2>
<p>/proc/net/pf_key</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipsec/">ipsec</a>(8), <a href="/docs/linux/man/5-ipsec_eroute/">ipsec_eroute</a>(5), <a href="/docs/linux/man/5-ipsec_spi/">ipsec_spi</a>(5), <a href="/docs/linux/man/5-ipsec_spigrp/">ipsec_spigrp</a>(5), <a href="/docs/linux/man/5-ipsec_klipsdebug/">ipsec_klipsdebug</a>(5), <a href="/docs/linux/man/8-ipsec_tncfg/">ipsec_tncfg</a>(8), <a href="/docs/linux/man/5-ipsec_version/">ipsec_version</a>(5)</p>
<h2>History</h2>
<p>Written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org/">http://www.freeswan.org/</a></code>m[]&gt; by Richard Guy Briggs.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
