---
title: "powermand(8)"
name: "powermand"
section: "8"
letter: "p"
url: "/docs/linux/man/8-powermand/"
description: "powermand – power control and monitoring daemon"
---

<p>powermand &#8211; power control and monitoring daemon</p>
<h2>Synopsis</h2>
<p><code>powermand</code> <i>[-options]</i> </p>
<h2>Description</h2>
<p><code>powermand</code> provides power management in a data center or compute cluster environment.</p>
<h2>Options</h2>
<dl>
<dt><i>-c, &#8211;conf filename</i></p>
<dd>Override the default location of the powerman configuration file <i>/etc/powerman/powerman.conf.</i></p>
<dt><i>-f, &#8211;foreground</i></p>
<dd>Do not daemonize, and send debugging/error messages to stderr instead of syslog.</p>
<dt><i>-d, &#8211;debug mask</i></p>
<dd>Set mask for debugging output.</p>
<dt><i>-h, &#8211;help</i></p>
<dd>Provide a synopsis of the command options.</p>
<dt><i>-V, &#8211;version</i></p>
<dd>Display the powerman version number and exit. </p>
<p> <code>PowerMan</code> and exit. </p>
</dl>
<h2>Files</h2>
<p>/usr/sbin/powermand<br />
 /etc/powerman/powerman.conf</p>
<h2>Origin</h2>
<p>PowerMan was originally developed by Andrew Uselton on LLNL&#8217;s Linux clusters. This software is open source and distributed under the terms of the GNU GPL.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-powerman/">powerman</a></code>(1), <code><a href="/docs/linux/man/8-powermand/">powermand</a></code>(8), <code><a href="/docs/linux/man/8-httppower/">httppower</a></code>(8), <code><a href="/docs/linux/man/8-plmpower/">plmpower</a></code>(8), <code><a href="/docs/linux/man/8-vpcd/">vpcd</a></code>(8), <code><a href="/docs/linux/man/5-powerman-conf/">powerman.conf</a></code>(5), <code><a href="/docs/linux/man/5-powerman-dev/">powerman.dev</a></code>(5). <code><a rel="nofollow" href="http://code.google.com/p/powerman">http://code.google.com/p/powerman</a></code> </p>
