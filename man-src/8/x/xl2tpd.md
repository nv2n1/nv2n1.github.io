---
title: "xl2tpd(8)"
name: "xl2tpd"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xl2tpd/"
description: "xl2tpd – Layer 2 Tunnelling Protocol Daemon"
---

<p>xl2tpd &#8211; Layer 2 Tunnelling Protocol Daemon</p>
<h2>Description</h2>
<p>A Layer 2 Tunneling Protocol VPN client/daemon for Linux and other POSIX-based OSs. Based off of L2TPd 0.61 from<br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://www.marko.net/l2tp">http://www.marko.net/l2tp</a>&nbsp;<wbr> and patches collected by Jacco de Leeuw at<br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://www.jacco2.dds.nl/networking/openswan-l2tp.html">http://www.jacco2.dds.nl/networking/openswan-l2tp.html</a> Currently maintained by Xelerance<br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://www.xelerance.com/software/xl2tpd/">http://www.xelerance.com/software/xl2tpd/</a> xl2tpd implements the Layer 2 Tunnelling Protocol, defined by RFC 2661. </p>
<h2>Options</h2>
<dl>
<dt><code>-D</code></p>
<dd>This option prevents xl2tpd from detaching from the terminal and daemonizing. </p>
<dt><code>-l</code></p>
<dd>This option tells xl2tpd to use syslog for logging even when <code>-D</code> was specified. </p>
<dt><code>-c &lt;config file&gt;</code></p>
<dd>Tells xl2tpd to use an alternate config file. Default is /etc/xl2tpd/xl2tpd.conf. Fallback configuration file is /etc/l2tpd/l2tpd.conf </p>
<dt><code>-s &lt;secret file&gt;</code></p>
<dd>Tells xl2tpd to use an alternate &quot;secrets&quot; file. Default is /etc/xl2tpd/l2tp-secrets </p>
<dt><code>-p &lt;pid file&gt;</code></p>
<dd>Tells xl2tpd to use an alternate pid file. Default is /var/run/xl2tpd/xl2tpd.pid </p>
<dt><code>-C &lt;control file&gt;</code></p>
<dd>Tells xl2tpd to use an alternate control file. Default is /var/run/xl2tpd/l2tp-control </p>
</dl>
<h2>Files</h2>
<p>/etc/xl2tpd/xl2tpd.conf /etc/xl2tpd/l2tp-secrets /var/run/xl2tpd/l2tp-control</p>
<h2>Bugs</h2>
<p>Please address bugs and comment to xl2tpd [at] lists.xelerance.com</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-xl2tpd-conf/">xl2tpd.conf</a>(5)</p>
<h2>Authors</h2>
<p>Forked from l2tpd by Xelerance (<a rel="nofollow" href="http://www.xelerance.com/software/xl2tpd/">http://www.xelerance.com/software/xl2tpd/</a> </p>
<p> Michael Richardson &lt;mcr [at] xelerance.com&gt; Paul Wouters &lt;paul [at] xelerance.com&gt; </p>
<p> Many thanks to Jacco de Leeuw &lt;jacco2 [at] dds.nl&gt; for maintaining l2tpd. </p>
<p> Previous development was hosted at sourceforge (<a rel="nofollow" href="http://www.sourceforge.net/projects/l2tpd)">http://www.sourceforge.net/projects/l2tpd)</a> by: </p>
<p> Scott Balmos &lt;sbalmos [at] iglou.com&gt;<br />
 David Stipp &lt;dstipp [at] one.net&gt;<br />
 Jeff McAdams &lt;jeffm [at] iglou.com&gt; </p>
<p> Based off of l2tpd version 0.60<br />
 Copyright (C)1998 Adtran, Inc.<br />
 Mark Spencer &lt;markster [at] marko.net&gt;</p>
