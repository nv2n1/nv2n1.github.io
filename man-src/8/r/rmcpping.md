---
title: "rmcpping(8)"
name: "rmcpping"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rmcpping/"
description: "rmcpping – send RMCP Ping to network hosts"
---

<p>rmcpping &#8211; send RMCP Ping to network hosts</p>
<h2>Synopsis</h2>
<p><code>rmcpping</code> [<i>OPTION</i>&#8230;] destination</p>
<h2>Description</h2>
<p><code>rmcpping</code> uses the RMCP Ping request datagram to elicit an RMCP Pong response from a remote host. The utility can be used to verify if a remote host supports RMCP or IPMI. The initial starting sequence number will be randomized. <code>rmcpping</code> will return 0 to the environment if it receives atleast 1 response from the remote host. Otherwise, it exits with a value of 1.</p>
<h2>Options</h2>
<p>The following options are available</p>
<dl>
<dt><code>-h</code></p>
<dd>Output help menu.</p>
<dt><code>-V</code></p>
<dd>Output version.</p>
<dt><code>-c</code> <i>count</i></p>
<dd>Stop after sending <i>count</i> packets.</p>
<dt><code>-i</code> <i>interval</i></p>
<dd>Wait <i>interval</i> seconds between sending each packet. The default is to wait for one second between each packet.</p>
<dt><code>-I</code> <i>interface address</i></p>
<dd>Set source address to specified interface address. Argument may be numeric IP address or name of device.</p>
<dt><code>-t</code> <i>timeout</i></p>
<dd>Time to wait for a response, in seconds. Default is five seconds.</p>
<dt><code>-v</code></p>
<dd>Verbose output.</p>
<dt><code>-s</code> <i>num</i></p>
<dd>Specify an initial starting sequence number. The default is to use a random initial sequence number.</p>
<dt><code>-d</code></p>
<dd>Turn on debugging.</dl>
<h2>Known Issues</h2>
<p>It has been observed that some remote BMCs can get &quot;confused&quot; and delay packet responses if duplicate packets (with duplicate sequence numbers) are sent in succession very quickly. There is no known way to cleanly deal with a &quot;confused&quot; BMC other than the wait awhile. </p>
<p> Unlike <code><a href="/docs/linux/man/8-ping/">ping</a>(8),</code> local network devicess (e.g. 127.0.0.1) cannot be &quot;pinged&quot;.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2007-2012 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2003-2007 The Regents of the University of California. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.</p>
<h2>Origin</h2>
<p>Command and manpage based off <code><a href="/docs/linux/man/8-ping/">ping</a>(8).</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-freeipmi/">freeipmi</a>(7), <a href="/docs/linux/man/8-ping/">ping</a>(8), <a href="/docs/linux/man/8-ipmiping/">ipmiping</a>(8) <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>
