---
title: "kerneloops(8)"
name: "kerneloops"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kerneloops/"
description: "kerneloops – program to collect and submit kernel oopses to oops.kernel.org"
---

<p>kerneloops &#8211; program to collect and submit kernel oopses to oops.kernel.org</p>
<h2>Synopsis</h2>
<p><code>kerneloops</code></p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>kerneloops</code> commands. </p>
<p> <code>kerneloops</code> is a program that collects kernel crash information and then submits the extracted signature to the oops.kernel.org website for statistical analysis and presentation to the Linux kernel developers.</p>
<h2>Options</h2>
<p>&nbsp;</p>
<dl>
<dt><code>&#8211;file filename</code></p>
<dd>Parse the file denoted with filename as if it were /var/log/messages</p>
<dt><code>&#8211;debug</code></p>
<dd>Enable debug mode</p>
<dt><code>&#8211;nodaemon</code></p>
<dd>Do not daemonize</dl>
<h2>Files</h2>
<p>/etc/kerneloops.conf</p>
<h2>Author</h2>
<p>kerneloops was written by Arjan van de Ven &lt;arjan [at] linux.intel.com&gt;.</p>
