---
title: "ipsec_klipsdebug(8)"
name: "ipsec_klipsdebug"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec_klipsdebug/"
description: "ipsec_klipsdebug – set KLIPS and MAST debug features and level. Other stacks are not supported."
---

<p>ipsec_klipsdebug &#8211; set KLIPS and MAST debug features and level. Other stacks are not supported.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec</code> <i>klipsdebug</i></p>
<dd><i>ipsec klipsdebug</i> &#8211;set <i>flagname</i></p>
<dd><i>ipsec klipsdebug</i> &#8211;clear <i>flagname</i></p>
<dd><i>ipsec klipsdebug</i> &#8211;all</p>
<dd><i>ipsec klipsdebug</i> &#8211;none</p>
<dd><i>ipsec klipsdebug</i> &#8211;help</p>
<dd><i>ipsec klipsdebug</i> &#8211;version</dl>
<h2>Description</h2>
<p><i>Klipsdebug</i></p>
<dd>sets and clears flags that control various parts of the debugging output of Klips (the kernel portion of FreeS/WAN IPSEC). The form with no additional arguments lists the present contents of /proc/net/ipsec_klipsdebug. The <code>&#8211;set</code> form turns the specified flag on, while the <code>&#8211;clear</code> form turns the specified flag off. The <code>&#8211;all</code> form turns all flags on except verbose, while the <code>&#8211;none</code> form turns all flags off. </p>
<p> The current flag names are: </p>
<p> <code>tunnel</code></p>
<dl>
<dd>tunnelling code</dl>
<p> <code>tunnel-xmit</code></p>
<dl>
<dd>tunnelling transmit only code</dl>
<p> <code>pfkey</code></p>
<dl>
<dd>userspace communication code</dl>
<p> <code>xform</code></p>
<dl>
<dd>transform selection and manipulation code</dl>
<p> <code>eroute</code></p>
<dl>
<dd>eroute table manipulation code</dl>
<p> <code>spi</code></p>
<dl>
<dd>SA table manipulation code</dl>
<p> <code>radij</code></p>
<dl>
<dd>radij tree manipulation code</dl>
<p> <code>esp</code></p>
<dl>
<dd>encryptions transforms code</dl>
<p> <code>ah</code></p>
<dl>
<dd>authentication transforms code <code>rcv</code> receive code</dl>
<p> <code>ipcomp</code></p>
<dl>
<dd>ip compression transforms code</dl>
<p> <code>verbose</code></p>
<dl>
<dd>give even more information, BEWARE: a)this will print authentication and encryption keys in the logs b)this will probably trample the 4k kernel printk buffer giving inaccurate output</dl>
<p> All Klips debug output appears as <code>kernel.info</code> messages to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8). Most systems are set up to log these messages to /var/log/messages. Beware that <code>klipsdebug</code><code>&#8211;all</code> produces a lot of output and the log file will grow quickly. </p>
<p> The file format for /proc/net/ipsec_klipsdebug is discussed in <a href="/docs/linux/man/5-ipsec_klipsdebug/">ipsec_klipsdebug</a>(5).</p>
<h2>Examples</h2>
<p><code>klipsdebug &#8211;all</code></p>
<dl>
<dd>turns on all KLIPS debugging except verbose.</dl>
<p> <code>klipsdebug &#8211;clear tunnel</code></p>
<dl>
<dd>turns off only the <code>tunnel</code> debugging messages.</dl>
<h2>Files</h2>
<p>/proc/net/ipsec_klipsdebug, /usr/local/bin/ipsec</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipsec/">ipsec</a>(8), <a href="/docs/linux/man/8-ipsec_manual/">ipsec_manual</a>(8), <a href="/docs/linux/man/8-ipsec_tncfg/">ipsec_tncfg</a>(8), <a href="/docs/linux/man/8-ipsec_eroute/">ipsec_eroute</a>(8), <a href="/docs/linux/man/8-ipsec_spi/">ipsec_spi</a>(8), <a href="/docs/linux/man/8-ipsec_spigrp/">ipsec_spigrp</a>(8), <a href="/docs/linux/man/5-ipsec_klipsdebug/">ipsec_klipsdebug</a>(5)</p>
<h2>History</h2>
<p>Written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org/">http://www.freeswan.org/</a></code>m[]&gt; by Richard Guy Briggs.</p>
<h2>Bugs</h2>
<p>It really ought to be possible to set or unset selective combinations of flags.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
