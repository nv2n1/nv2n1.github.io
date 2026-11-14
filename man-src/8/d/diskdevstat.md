---
title: "diskdevstat(8)"
name: "diskdevstat"
section: "8"
letter: "d"
url: "/docs/linux/man/8-diskdevstat/"
description: "diskdevstat – tool for recording harddisk activity"
---

<p>diskdevstat &#8211; tool for recording harddisk activity</p>
<h2>Synopsis</h2>
<p><code>diskdevstat</code> [<i>update interval</i>] [<i>total duration</i>] [<i>display histogram</i>]</p>
<h2>Description</h2>
<p><code>diskdevstat</code> is a simple systemtap script to record harddisk activity of processes and display statistics for read/write operations.</p>
<dl>
<dt>update interval</p>
<dd>Sets sampling interval in seconds.</p>
<dt>total duration</p>
<dd>Sets total measurement time in seconds.</p>
<dt>display histogram</p>
<dd>If this parameter is present, the histogram will be shown at the end of the measurement. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-tuned/">tuned</a>(8) <a href="/docs/linux/man/8-netdevstat/">netdevstat</a>(8) <a href="/docs/linux/man/8-varnetload/">varnetload</a>(8) <a href="/docs/linux/man/8-scomes/">scomes</a>(8) <a href="/docs/linux/man/1-stap/">stap</a>(1)</p>
<h2>Author</h2>
<p>Written by Phil Knirsch &lt;pknirsch [at] redhat.com&gt;.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;pknirsch [at] redhat.com&gt;.</p>
