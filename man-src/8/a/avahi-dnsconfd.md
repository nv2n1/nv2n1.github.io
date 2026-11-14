---
title: "avahi-dnsconfd(8)"
name: "avahi-dnsconfd"
section: "8"
letter: "a"
url: "/docs/linux/man/8-avahi-dnsconfd/"
description: "avahi-dnsconfd – Unicast DNS server from mDNS/DNS-SD configuration daemon"
---

<p>avahi-dnsconfd &#8211; Unicast DNS server from mDNS/DNS-SD configuration daemon</p>
<h2>Synopsis</h2>
<p><code>avahi-dnsconfd [</code><i>options</i><code>] </p>
<p> avahi-dnsconfd &#8211;kill </p>
<p> avahi-dnsconfd &#8211;refresh </p>
<p> avahi-dnsconfd &#8211;check </code></p>
<h2>Description</h2>
<p>avahi-dnsconfd connects to a running avahi-daemon and runs the script <i>/etc/avahi/dnsconfd.action</i> for each unicast DNS server that is announced on the local LAN. This is useful for configuring unicast DNS servers in a DHCP-like fashion with mDNS.</p>
<h2>Options</h2>
<dl>
<dt><code>-D | &#8211;daemonize</code></p>
<dd>Daemonize after startup and redirect log messages to syslog.</p>
<dt><code>-s | &#8211;syslog</code></p>
<dd>Log to syslog instead of STDERR. Implied by <code>&#8211;daemonize</code>.</p>
<dt><code>-k | &#8211;kill</code></p>
<dd>Kill an already running avahi-dnsconfd. (equivalent to sending a SIGTERM)</p>
<dt><code>-r | &#8211;refresh</code></p>
<dd>Tell an already running avahi-dnsconfd to refresh the DNS server data. (equivalent to sending a SIGHUP)</p>
<dt><code>-c | &#8211;check</code></p>
<dd>Return 0 as return code when avahi-dnsconfd is already running.</p>
<dt><code>-h | &#8211;help</code></p>
<dd>Show help</p>
<dt><code>-v | &#8211;version</code></p>
<dd>Show version information</dl>
<h2>Files</h2>
<p><i>/etc/avahi/avahi-dnsconfd.action</i>: the script to run when a DNS server is found or removed.</p>
<h2>Signals</h2>
<p><i>SIGINT, SIGTERM</i>: avahi-dnsconfd will shutdown. This is issued by passing &#8211;kill to avahi-daemon. </p>
<p> <i>SIGHUP</i>: avahi-dnsconfd will refresh the DNS server data.</p>
<h2>Authors</h2>
<p>The Avahi Developers &lt;avahi (at) lists (dot) freedesktop (dot) org&gt;; Avahi is available from <code><a rel="nofollow" href="http://avahi.org/">http://avahi.org/</a></code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-avahi-daemon/">avahi-daemon</a>(8)</code>, <code><a href="/docs/linux/man/8-avahi-dnsconfd-action/">avahi-dnsconfd.action</a>(8)</code></p>
<h2>Comments</h2>
<p>This man page was written using <code><a href="/docs/linux/man/1-xml2man/">xml2man</a>(1)</code> by Oliver Kurth.</p>
