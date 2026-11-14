---
title: "try-from(8)"
name: "try-from"
section: "8"
letter: "t"
url: "/docs/linux/man/8-try-from/"
description: "try-from – test program for the tcp_wrapper"
---

<p>try-from &#8211; test program for the tcp_wrapper</p>
<h2>Synopsis</h2>
<p><code>try-from</code></p>
<h2>Description</h2>
<p>The <code>try-from</code> command can be called via a remote shell command to find out if the hostname and address are properly recognized by the <code>tcp_wrapper</code> library, if username lookup works, and (SysV only) if the TLI on top of IP heuristics work. Diagnostics are reported through <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) and redirected to stderr. Example: rsh host /some/where/try-from </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a></code>(5), <code><a href="/docs/linux/man/5-hosts_options/">hosts_options</a></code>(5), <code><a href="/docs/linux/man/8-tcpd/">tcpd</a></code>(8)</p>
<h2>Author</h2>
<p>Wietse Venema, Eindhoven University of Technology, The Netherlands.</p>
