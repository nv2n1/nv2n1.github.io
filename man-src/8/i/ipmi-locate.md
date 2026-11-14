---
title: "ipmi-locate(8)"
name: "ipmi-locate"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipmi-locate/"
description: "IPMI – IPMI probing utility"
---

<p>IPMI &#8211; IPMI probing utility</p>
<h2>Synopsis</h2>
<p><code>ipmi-locate</code> [<i>OPTION</i>&#8230;]</p>
<h2>Description</h2>
<p><code>Ipmi-locate</code> probes and displays information about a BMC device, such as device addresses or IPMI version support. <code>Ipmi-locate</code> is sometimes used to determine if IPMI can be found on your system. Users are cautioned though, the failure to discover IPMI via <code>Ipmi-locate</code> is not sufficient to disprove that IPMI exists on your system. Your system may not publish such information or may expect clients to communicate at default locations.</p>
<h2>Options</h2>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd>Output a help list and exit.</p>
<dt><code>&#8211;usage</code></p>
<dd>Output a usage message and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Output the program version and exit.</dl>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2005-2012 FreeIPMI Core Team </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-freeipmi/">freeipmi</a>(7) <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>
