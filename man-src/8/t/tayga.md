---
title: "tayga(8)"
name: "tayga"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tayga/"
description: "tayga – stateless NAT64 daemon"
---

<p>tayga &#8211; stateless NAT64 daemon</p>
<h2>Synopsis</h2>
<p><code>tayga</code> <i>[OPTION]&#8230;</i> <code>tayga &#8211;mktun</code> <i>[OPTION]&#8230;</i> <code>tayga &#8211;rmtun</code> <i>[OPTION]&#8230;</i> </p>
<h2>Description</h2>
<p>TAYGA is a stateless NAT64 daemon for Linux. Using the in-kernel TUN network driver, TAYGA receives IPv4 and IPv6 packets from the host&#8217;s network stack, translates them to the other protocol, and then sends the translated packets back to the host using the same TUN interface. Translation is compliant with IETF Internet-Draft draft-ietf-behave-v6v4-xlate-23, and address mapping is performed in accordance with RFC 6052. Optionally, TAYGA may be configured to dynamically map IPv6 hosts to addresses drawn from a configured IPv4 address pool. As a stateless NAT, TAYGA requires a one-to-one mapping between IPv4 addresses and IPv6 addresses. Mapping multiple IPv6 addresses onto a single IPv4 address can be achieved by mapping IPv6 addresses to private IPv4 addresses with TAYGA and then using a stateful NAT44 (such as the <a href="/docs/linux/man/8-iptables/">iptables</a>(8) MASQUERADE target) to map the private IPv4 addresses onto the desired single IPv4 address. TAYGA&#8217;s configuration is stored in the <a href="/docs/linux/man/5-tayga-conf/">tayga.conf</a>(5) file, which is usually found in /etc/tayga.conf or /usr/local/etc/tayga.conf. </p>
<h2>Invocation</h2>
<p>Without the <code>&#8211;mktun</code> or <code>&#8211;rmtun</code> options, the `tayga` executable runs as a daemon, translating packets as described above. </p>
<p> The <code>&#8211;mktun</code> and <code>&#8211;rmtun</code> options instruct TAYGA to create or destroy, respectively, its configured TUN device as a &quot;persistent&quot; interface and then immediately exit. </p>
<p> Persistent TUN devices remain present on the host system even when TAYGA is not running. This allows host-side network parameters and firewall rules to be configured prior to commencement of packet translation. This may simplify network configuration on the host; for example, systems which use a Debian-style /etc/network/interfaces file may configure TAYGA&#8217;s TUN device at boot by running `tayga &#8211;mktun` as a &quot;pre-up&quot; command and then configuring the TUN device as any other network interface.</p>
<h2>Options</h2>
<dl>
<dt><code>-c </code><i>configfile</i><code> | &#8211;config </code><i>configfile</i></p>
<dd>Read configuration options from <i>configfile</i></p>
<dt><code>-d</code></p>
<dd>Enable debug messages (enables <code>&#8211;nodetach</code> as well)</p>
<dt><code>-n | &#8211;nodetach</code></p>
<dd>Do not detach from terminal</p>
<dt><code>-u </code><i>userid</i><code> | &#8211;user </code><i>userid</i></p>
<dd>Set uid to <i>userid</i> after initialization</p>
<dt><code>-g </code><i>groupid</i><code> | &#8211;group </code><i>groupid</i></p>
<dd>Set gid to <i>groupid</i> after initialization</p>
<dt><code>-r | &#8211;chroot</code></p>
<dd>chroot() to data-dir (specified in config file)</p>
<dt><code>-p </code><i>pidfile</i><code> | &#8211;pidfile </code><i>pidfile</i></p>
<dd>Write process ID of daemon to <i>pidfile</i></dl>
<h2>Author</h2>
<p>Written by Nathan Lutchansky &lt;lutchann [at] litech.org&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2010 Nathan Lutchansky<br />
 License GPLv2+: GNU GPL version 2 or later<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-tayga-conf/">tayga.conf</a></code>(5)<br />
 <code>&lt;<a rel="nofollow" href="http://www.litech.org/tayga/">http://www.litech.org/tayga/</a>&gt;</code> </p>
