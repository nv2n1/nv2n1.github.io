---
title: "avahi-autoipd(8)"
name: "avahi-autoipd"
section: "8"
letter: "a"
url: "/docs/linux/man/8-avahi-autoipd/"
description: "avahi-autoipd – IPv4LL network address configuration daemon"
---

<p>avahi-autoipd &#8211; IPv4LL network address configuration daemon</p>
<h2>Synopsis</h2>
<p><code>avahi-autoipd [</code><i>options</i><code>] </code><i>interface</i><code> </p>
<p> avahi-autoipd &#8211;kill </code><i>interface</i><code> </p>
<p> avahi-autoipd &#8211;refresh </code><i>interface</i><code> </p>
<p> avahi-autoipd &#8211;check </code><i>interface</i></p>
<h2>Description</h2>
<p>avahi-autoipd implements IPv4LL, &quot;Dynamic Configuration of IPv4 Link-Local Addresses&quot; (IETF RFC3927), a protocol for automatic IP address configuration from the link-local 169.254.0.0/16 range without the need for a central server. It is primarily intended to be used in ad-hoc networks which lack a DHCP server. </p>
<p> IPv4LL is part of the Zeroconf stack. </p>
<p> avahi-autoipd can be used as stand-alone address allocator or as plugin for a DHCP client such as ISC&#8217;s dhclient, where it can be used as fallback solution if no DHCP server is found. </p>
<p> To allow communication between hosts that have only an IPv4LL address assigned and hosts that only have a routable IP address assigned you may add the following routes to both network configurations: </p>
<p> <code>route add -net 169.254.0.0 netmask 255.255.0.0 dev eth0 metric 99</code> </p>
<p> <code>route add default dev eth0 metric 99</code> </p>
<p> See <a rel="nofollow" href="http://developer.apple.com/qa/qa2004/qa1357.html">http://developer.apple.com/qa/qa2004/qa1357.html</a> for more information.</p>
<h2>Options</h2>
<dl>
<dt><code>-D | &#8211;daemonize</code></dt>
<dd>Daemonize after startup. Implies <code>&#8211;syslog</code>.</dd>
<dt><code>-k | &#8211;kill</code></dt>
<dd>Kill an already running avahi-autoipd on the specified network interface. (Equivalent to sending a SIGTERM)</dd>
<dt><code>-r | &#8211;refresh</code></dt>
<dd>Tell an already running avahi-autoipd to re-announce the acquired IP address on the specified network interface. (Equivalent to sending a SIGHUP)</dd>
<dt><code>-c | &#8211;check</code></dt>
<dd>Return 0 as return code if avahi-autoipd is already running for the specified network interface.</dd>
<dt><code>-s | &#8211;syslog</code></dt>
<dd>Log to syslog instead of STDERR. Implied by <code>&#8211;daemonize</code>.</dd>
<dt><code>&#8211;debug</code></dt>
<dd>Enable verbose mode.</dd>
<dt><code>&#8211;no-drop-root</code></dt>
<dd>Don&#8217;t drop root privileges after startup. We recommend not to use this option.</dd>
<dt><code>&#8211;no-chroot</code></dt>
<dd>Don&#8217;t <code><a href="/docs/linux/man/2-chroot/">chroot</a>(2)</code> the daemon. This option is only available when compiled with chroot() support.</dd>
<dt><code>-S | &#8211;start=</code></dt>
<dd>Try to acquire the specified IP address, which must be from the IPv4LL range 169.254.0.0/16.</dd>
<dt><code>-w | &#8211;wait</code></dt>
<dd>Wait until a IP address has been successfully acquired before detaching. Only valid in combination with <code>&#8211;daemonize</code>.</dd>
<dt><code>&#8211;force-bind</code></dt>
<dd>Acquire an IPv4LL address, even if a routable address has been configured on the interface.</dd>
<dt><code>&#8211;no-proc-title</code></dt>
<dd>Don&#8217;t change the process name while running. Unless this option is specified avahi-autoipd will reflect its current state and the IP address in the process title.</dd>
<dt><code>-h | &#8211;help</code></dt>
<dd>Show help.</dd>
<dt><code>-v | &#8211;version</code></dt>
<dd>Show version information.</dd></dl>
<h2>Files</h2>
<p><i>/etc/avahi/avahi-autoipd.action</i>: the script to run when an IP address as been acquired or is lost.</p>
<h2>Signals</h2>
<p><i>SIGINT, SIGTERM</i>: avahi-autoipd will shutdown. (Same as <code>&#8211;kill</code>) </p>
<p> <i>SIGHUP</i>: avahi-autoipd will re-announce the acquired IP address. (Same as <code>&#8211;refresh</code>)</p>
<h2>Authors</h2>
<p>The Avahi Developers &lt;avahi (at) lists (dot) freedesktop (dot) org&gt;; Avahi is available from <code><a rel="nofollow" href="http://avahi.org/">http://avahi.org/</a></code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-avahi-autoipd-action/">avahi-autoipd.action</a>(8)</code>, <code><a href="/docs/linux/man/8-dhclient/">dhclient</a>(8)</code> </p>
<p> <a rel="nofollow" href="http://avahi.org/wiki/AvahiAutoipd">http://avahi.org/wiki/AvahiAutoipd</a> documents how avahi-autoipd is best packaged and integrated into distributions.</p>
<h2>Comments</h2>
<p>This man page was written using <code>xml2man(1)</code> by Oliver Kurth.</p>
