---
title: "scomes(8)"
name: "scomes"
section: "8"
letter: "s"
url: "/docs/linux/man/8-scomes/"
description: "scomes – tool for watching system resources"
---

<p>scomes &#8211; tool for watching system resources</p>
<h2>Synopsis</h2>
<p><code>scomes</code> -c &quot;binary [binary arguments &#8230;]&quot; [timer]</p>
<h2>Description</h2>
<p><code>scomes</code> is a simple systemtap script for watching activity of one process. Syscalls count, userspace and kernelspace ticks, read and written bytes, transmitted and received bytes and polling syscalls are measured.</p>
<dl>
<dt>binary</p>
<dd>Binary file to be executed. This process will be watched.</p>
<dt>timer</p>
<dd>Setting this option causes the script to print out statistic every N seconds. If not provided, the statistics are printed only when watched process terminates. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-tuned/">tuned</a>(8) <a href="/docs/linux/man/8-diskdevstat/">diskdevstat</a>(8) <a href="/docs/linux/man/8-netdevstat/">netdevstat</a>(8) <a href="/docs/linux/man/8-varnetload/">varnetload</a>(8) <a href="/docs/linux/man/1-stap/">stap</a>(1)</p>
<h2>Author</h2>
<p>Written by Jan Hutar &lt;jhutar [at] redhat.com&gt;.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;pknirsch [at] redhat.com&gt;.</p>
