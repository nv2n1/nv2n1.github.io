---
title: "halt(5)"
name: "halt"
section: "5"
letter: "h"
url: "/docs/linux/man/5-halt/"
description: "halt – variables that affect the behavior of the shutdown scripts"
---

<p>halt &#8211; variables that affect the behavior of the shutdown scripts</p>
<h2>Description</h2>
<p>The <i>/etc/default/halt</i> file contains variable settings in POSIX format:</p>
<dl>
<dd>VAR=VAL</dl>
<p> Only one assignment is allowed per line. Comments (starting with &#8216;#&#8217;) are also allowed. </p>
<h2>Options</h2>
<p>The following variables can be set. </p>
<dl>
<dt><code>HALT</code></p>
<dd>If set to <code>poweroff</code> the system will be powered down after it has been brought down. This is the default.<br />
 If set to <code>halt </code> the system will only be halted after it has been brought down. What exactly this means depends on your hardware. </p>
<dt><code>NETDOWN</p>
<dd>Setting this to no</code> prevents shutdown from shutting down the network intefaces. This is necessary to use Wake-On-Lan. Setting it to <code>yes</code> causes shutdown to also bring down the network interfaces (and thus prevent the machine from being woken up remotely). </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-halt/">halt</a></code>(8), <code><a href="/docs/linux/man/8-shutdown/">shutdown</a></code>(8). </p>
<h2>Author</h2>
<p><code>Casper Gielen</code> &lt;casper [at] gielen.name&gt;</p>
<h2>Copyright</h2>
<p>This manual page is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This manual page is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this manual page; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA</p>
