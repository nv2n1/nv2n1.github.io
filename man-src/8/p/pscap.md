---
title: "pscap(8)"
name: "pscap"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pscap/"
description: "pscap – a program to see capabilities"
---

<p>pscap &#8211; a program to see capabilities</p>
<h2>Synopsis</h2>
<p><code>pscap [ -a ]</code></p>
<h2>Description</h2>
<p><code>pscap</code> is a program that prints out a report of process capabilities. If the application has any capabilities, it will be in the report with the exception of init. By giving the -a command line option, init will be included, too. If a process is not in the report, it has dropped all capabilities. If the process has partial capabilities, it is further examined to see if it has an open-ended bounding set. If this is found to be true, a &#8216;+&#8217; symbol is added. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-netcap/">netcap</a></code>(8), <code><a href="/docs/linux/man/8-filecap/">filecap</a></code>(8), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/8-ps/">ps</a></code>(8). </p>
<h2>Author</h2>
<p>Steve Grubb</p>
