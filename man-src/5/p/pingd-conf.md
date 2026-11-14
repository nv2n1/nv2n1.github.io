---
title: "pingd-conf(5)"
name: "pingd-conf"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pingd-conf/"
description: "pingd.conf – pingd configuration file"
---

<p>pingd.conf &#8211; pingd configuration file</p>
<h2>Description</h2>
<p>The <code>pingd</code> configuration file configures the <code>pingd</code> daemon. The default configuration file loaded is /etc/pingd.conf. The configuration options that can be specified in the configuration file are listed below. Each configuration option must be listed on a separate line. Arguments for an option are separated by any amount of whitespace. Multiple arguments are also separated by whitespace. Comments can be marked by using the pound sign (&quot;#&quot;) character, and lines can be continued on the next using backslash (&quot;\&quot;). </p>
<h2>Pingd Configuration Options</h2>
<dl>
<dt>
<dt><i>ping_period num</i></p>
<dd>
<dd>Specify the period time in milliseconds that ICMP pings should be regularly sent out. Default is 15000.</p>
<dt><i>pingd_server_port port</i></p>
<dd>Specify the alternate default port the pingd server should listen for requests off of. Default is 9125.</p>
<dt><i>host string</i></p>
<dd>Specify a host the pingd daemon whould regularly ping. Can be specified as many times as necessary.</dl>
<h2>Files</h2>
<p>/etc/pingd.conf</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-pingd/">pingd</a>(8) </p>
