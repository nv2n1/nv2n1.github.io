---
title: "netdevstat(8)"
name: "netdevstat"
section: "8"
letter: "n"
url: "/docs/linux/man/8-netdevstat/"
description: "netdevstat – tool for recording network activity"
---

<p>netdevstat &#8211; tool for recording network activity</p>
<h2>Synopsis</h2>
<p><code>netdevstat</code> [<i>update interval</i>] [<i>total duration</i>] [<i>display histogram</i>]</p>
<h2>Description</h2>
<p><code>netdevstat</code> is a simple systemtap script to record network activity of processes and display statistics for transmit/receive operations.</p>
<dl>
<dt>update interval</p>
<dd>Sets sampling interval in seconds.</p>
<dt>total duration</p>
<dd>Sets total measurement time in seconds.</p>
<dt>display histogram</p>
<dd>If this parameter is present, the histogram will be shown at the end of the measurement. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-tuned/">tuned</a>(8) <a href="/docs/linux/man/8-diskdevstat/">diskdevstat</a>(8) <a href="/docs/linux/man/8-varnetload/">varnetload</a>(8) <a href="/docs/linux/man/8-scomes/">scomes</a>(8) <a href="/docs/linux/man/1-stap/">stap</a>(1)</p>
<h2>Author</h2>
<p>Written by Phil Knirsch &lt;pknirsch [at] redhat.com&gt;.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;pknirsch [at] redhat.com&gt;.</p>
