---
title: "netcap(8)"
name: "netcap"
section: "8"
letter: "n"
url: "/docs/linux/man/8-netcap/"
description: "netcap – a program to see capabilities"
---

<p>netcap &#8211; a program to see capabilities</p>
<h2>Synopsis</h2>
<p><code>netcap</code></p>
<h2>Description</h2>
<p><code>netcap</code> is a program that prints out a report of process capabilities. If the application is using tcp, udp, raw, or packet family of sockets AND has any capabilities, it will be in the report. If the process has partial capabilities, it is further examined to see if it has an open-ended bounding set. If this is found to be true, a &#8216;+&#8217; symbol is added. Some directories in the /proc file system are readonly by root. The program will try to access and report what it can. But if nothing comes out, try changing to the root user and re-run this program. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pscap/">pscap</a></code>(8), <code><a href="/docs/linux/man/8-filecap/">filecap</a></code>(8), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/8-netstat/">netstat</a></code>(8). </p>
<h2>Author</h2>
<p>Steve Grubb</p>
