---
title: "ipmidetectd(5)"
name: "ipmidetectd"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ipmidetectd/"
description: "ipmidetectd.conf – ipmidetectd configuration file"
---

<p>ipmidetectd.conf &#8211; ipmidetectd configuration file</p>
<h2>Description</h2>
<p>The <code>ipmidetectd</code> configuration file configures the <code>ipmidetectd</code> daemon. The default configuration file loaded is /etc/ipmidetectd.conf. The configuration options that can be specified in the configuration file are listed below. Each configuration option must be listed on a separate line. Arguments for an option are separated by any amount of whitespace. Multiple arguments are also separated by whitespace. Comments can be marked by using the pound sign (&quot;#&quot;) character, and lines can be continued on the next using backslash (&quot;\&quot;). </p>
<h2>Ipmidetectd Configuration Options</h2>
<dl>
<dt>
<dt><i>ipmiping_period num</i></p>
<dd>
<dd>Specify the period time in milliseconds that IPMI pings should be regularly sent out. Default is 15000.</p>
<dt><i>ipmidetectd_server_port port</i></p>
<dd>Specify the alternate default port the ipmidetectd server should listen for requests off of. Default is 9225.</p>
<dt><i>host string</i></p>
<dd>Specify a host or IP address the ipmidetectd daemon whould send IPMI pings to. Can be specified as many times as necessary. Can accept host ranges as input. See HOSTRANGED SUPPORT <code><a href="/docs/linux/man/8-ipmidetect/">ipmidetect</a>(8)</code> for information on ranged formats.</dl>
<h2>Files</h2>
<p>/etc/ipmidetectd.conf</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2007-2008 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2007 The Regents of the University of California.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipmidetectd/">ipmidetectd</a>(8), <a href="/docs/linux/man/8-ipmidetect/">ipmidetect</a>(8) <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>
