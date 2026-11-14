---
title: "dhcp6ctl(8)"
name: "dhcp6ctl"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dhcp6ctl/"
description: "dhcp6ctl – DHCPv6 client and server control utility"
---

<p><code>dhcp6ctl</code> &#8211; DHCPv6 client and server control utility</p>
<h2>Synopsis</h2>
<p>[-<code>C | -S</code> ] [-<code>k </code><i>keyfile</i> ] [-<code>p </code><i>port</i> ] [-<code>s </code><i>address</i> ] <code>command</code></p>
<h2>Description</h2>
<p>controls the operation of a DHCPv6 process, which is either <code>dhcp6c</code> or <code>dhcp6s</code> a DHCPv6 client or a server. By default, controls a client. The type of the process can also be specified explicitly by the &#8211;<code>C</code> or &#8211;<code>S</code> options. communicates with the DHCPv6 process over a TCP connection, sending commands authenticated with digital signatures. Currently, the only supported authentication algorithm is HMAC-MD5, which uses a shared secret on each end of the connection. Command line options are as below:</p>
<dl>
<dt><code>-C</code></p>
<dd>Control a DHCPv6 client. This option is exclusive with the &#8211;<code>S</code> option.</p>
<dt><code>-S</code></p>
<dd>Control a DHCPv6 server. This option is exclusive with the &#8211;<code>C</code> option.</p>
<dt><code>-k </code><i>keyfile</i></p>
<dd>Use <i>keyfile</i> to provide the shared secret to communicate with the process. The default file name used when unspecified is /etc/wide-dhcpv6/dhcp6cctlkey with a client, and /etc/wide-dhcpv6/dhcp6sctlkey with a server.</p>
<dt><code>-p </code><i>port</i></p>
<dd>Specify <i>port</i> as the listening port of the process. The default port number used when unspecified is 5546 for a client, and 5547 for a server.</p>
<dt><code>-s </code><i>address</i></p>
<dd>Specify <i>address</i> as the listening address of the process. The default address used when unspecified is ::1.</dl>
<h2>Key File</h2>
<p>Since the operation available with the command is powerful, the communication between the command and <code>dhcp6c</code> or <code>dhcp6s</code> must be authenticated. The supported algorithm for authentication is HMAC-MD5, which requires a shared secret, and the secret is stored in the key file. The key file must consist of a single line, in which the secret value is written in the form of BASE-64 encoding.</p>
<h2>Commands</h2>
<p>Each <code>command</code> specifies a single control operation. Supported commands are as follows: </p>
<dl>
<dt> <code>reload</code></p>
<dd>
<dd>This command specifies the process to reload the configuration file. Existing bindings, if any, are intact.</p>
<dt> <code>remove </code><i>arguments</i></p>
<dd>
<dd>This command is only applicable to a server. This specifies the server to remove a run-time object specified by <i>arguments</i> from the server. Currently, the only possible object is one particular IA_NA or IA_PD binding, which is specified as `<code>binding</code> &#8216; IA Ic IA_NA Ar IAID Ar DUID or `<code>binding</code> &#8216; IA Ic IA_PD Ar IAID Ar DUID where <i>IAID</i> is a decimal number specifying the IAID of the IA, and <i>DUID</i> is a DHCP Unique Identifier of the binding. The format of <i>DUID</i> is the same as that specified in dhcp6s.conf5.</p>
<dt> <code>start interface </code><i>ifname</i></p>
<dd>
<dd>This command is only applicable to a client. It tells the client to release the current configuration information (if any) on the interface <i>ifname</i> and restart the DHCPv6 configuration process on the interface.</p>
<dt> <code>stop interface </code><i>ifname</i></p>
<dd>
<dd>This command is only applicable to a client. It tells the client to release the current configuration information (if any) on the interface <i>ifname</i> Any timer running for the interface will be stopped, and no more DHCPv6 messages will be sent on the interface. The configuration process can later be restarted by the <code>start</code> command.</p>
<dt> <code>stop</code></p>
<dd>
<dd>This command stops the specified process. If the process is a client, it will release all configuration information (if any) and exits.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/wide-dhcpv6/dhcp6cctlkey </code></p>
<dd>is the default key file to communicate with a client.</p>
<dt><code>/etc/wide-dhcpv6/dhcp6sctlkey </code></p>
<dd>is the default key file to communicate with a server.</dl>
<h2>See Also</h2>
<p>dhcp6s.conf5 <a href="/docs/linux/man/8-dhcp6s/">dhcp6s</a>(8)</p>
<h2>History</h2>
<p>The command first appeared in WIDE/KAME IPv6 protocol stack kit.</p>
