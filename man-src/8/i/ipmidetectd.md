---
title: "ipmidetectd(8)"
name: "ipmidetectd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipmidetectd/"
description: "ipmidetectd – IPMI node detection monitoring daemon"
---

<p>ipmidetectd &#8211; IPMI node detection monitoring daemon</p>
<h2>Synopsis</h2>
<p><code>ipmidetectd</code> [<i>OPTION</i>&#8230;]</p>
<h2>Description</h2>
<p>The <code>ipmidetectd</code> daemon regularly sends out IPMI pings to determine if nodes have functioning IPMI interfaces or not. It is primarily used to determine those nodes in the cluster that are not functioning properly, allowing IPMI commands to be executed across the cluster faster by skipping those nodes that would automatically timeout. </p>
<p> The <code>ipmidetectd</code> daemon must be configured using the <code>ipmidetectd</code> configuration file. Until hosts to be pinged are configured, <code>ipmidetectd</code> will not function properly. </p>
<p> See the <code><a href="/docs/linux/man/5-ipmidetectd-conf/">ipmidetectd.conf</a>(5)</code> manpage for additional information.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Output help</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Output version</p>
<dt><code>-c</code> <i>FILE</i>, <code>&#8211;config-file</code></p>
<dd>Specify alternate configuration file</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd>Turn on debugging and run daemon in foreground</dl>
<h2>Errors</h2>
<p>Errors are logged to syslog.</p>
<h2>Files</h2>
<p>/etc/freeipmi//ipmidetectd.conf</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2007-2012 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2007 The Regents of the University of California. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-ipmidetectd-conf/">ipmidetectd.conf</a>(5) <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>
