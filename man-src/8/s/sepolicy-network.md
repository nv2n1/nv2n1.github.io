---
title: "sepolicy-network(8)"
name: "sepolicy-network"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sepolicy-network/"
description: "sepolicy-network – Examine the SELinux Policy and generate a network report"
---

<p>sepolicy-network &#8211; Examine the SELinux Policy and generate a network report </p>
<h2>Synopsis</h2>
<p><code>sepolicy network [-h] (-l | -a application [application &#8230;] | -p PORT [PORT &#8230;] | -t TYPE [TYPE &#8230;] | -d DOMAIN [DOMAIN &#8230;])</code> </p>
<h2>Description</h2>
<p>Use sepolicy network to examine SELinux Policy and generate network reports. </p>
<h2>Options</h2>
<dl>
<dt><i>-a, &#8211;application</i></p>
<dd>Generate a report listing the ports to which the specified init application is allowed to connect and or bind.</p>
<dt><i>-d, &#8211;domain </i></p>
<dd>Generate a report listing the ports to which the specified domain is allowed to connect and or bind.</p>
<dt><i>-l, &#8211;list </i></p>
<dd>List all Network Port Types defined in SELinux Policy</p>
<dt><i>-h, &#8211;help </i></p>
<dd>Display help message</p>
<dt><i>-t, &#8211;type</i></p>
<dd>Generate a report listing the port numbers associate with the specified SELinux port type.</p>
<dt><i>-p, &#8211;port</i></p>
<dd>Generate a report listing the SELinux port types associate with the specified port number. </p>
</dl>
<h2>Examples</h2>
<p><code>sepolicy network -p 22</code><br />
 22: tcp ssh_port_t 22<br />
 22: udp reserved_port_t 1-511<br />
 22: tcp reserved_port_t 1-511 <code>sepolicy network -a /usr/sbin/sshd</code><br />
 sshd_t: tcp name_connect<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>111 (portmap_port_t)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>53 (dns_port_t)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>88, 750, 4444 (kerberos_port_t)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>9080 (ocsp_port_t)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>9180, 9701, 9443-9447 (pki_ca_port_t)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>32768-61000 (ephemeral_port_t)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>all ports &lt; 1024 (reserved_port_type)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>all ports with out defined types (port_t)</p>
<p> sshd_t: tcp name_bind<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>22 (ssh_port_t)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>5900-5983, 5985-5999 (vnc_port_t)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>6000-6020 (xserver_port_t)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>32768-61000 (ephemeral_port_t)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>all ports &gt; 500 and &lt; 1024 (rpc_port_type)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>all ports with out defined types (port_t)</p>
<p> sshd_t: udp name_bind<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>32768-61000 (ephemeral_port_t)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>all ports &gt; 500 and &lt; 1024 (rpc_port_type)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>all ports with out defined types (port_t)</p>
<h2>Author</h2>
<p>This man page was written by Daniel Walsh &lt;dwalsh [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8), <a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8) </p>
