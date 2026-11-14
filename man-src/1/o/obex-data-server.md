---
title: "obex-data-server(1)"
name: "obex-data-server"
section: "1"
letter: "o"
url: "/docs/linux/man/1-obex-data-server/"
description: "obex-data-server – D-Bus service providing OBEX functionality"
---

<h2 class="name">NAME</h2>
<p> obex-data-server &#8211; D-Bus service providing OBEX functionality </p>
<h2>SYNOPSIS</h2>
<p> <code>obex-data-server </code> [OPTIONS]</p>
<h2>DESCRIPTION</h2>
<p> <code>obex-data-server </code> is D-Bus service providing high-level OBEX client and server side functionality. It currently supports OPP (Object Push Profile), FTP (File Transfer profile) and partially BIP (Basic Imaging profile). Supported transports are Bluetooth, USB (client only) or TTY. obex-data-server exposes it&#8217;s functionality through &#8216;org.openobex&#8217; namespace in D-Bus.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-n, &#8211;no-daemon</p>
<dd> Do not daemonize the service</p>
<dt>-s, &#8211;system-bus</p>
<dd> Use D-Bus System bus instead of the default Session bus</p>
<dt>-l, &#8211;log</p>
<dd> Log all messages to syslog</p>
<dt>-d, &#8211;debug</p>
<dd> Enable debugging messages</p>
<dt>-v, &#8211;version</p>
<dd> Show version of obex-data-server and exit immediately</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Tadas Dailyda &lt;tadas [at] dailyda.com&gt;.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="http://bugs.muiline.com">http://bugs.muiline.com</a> (obex-data-server project). </p>
<h2>Index</h2>
