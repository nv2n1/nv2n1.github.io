---
title: "op-check-perfevents(1)"
name: "op-check-perfevents"
section: "1"
letter: "o"
url: "/docs/linux/man/1-op-check-perfevents/"
description: "op-check-perfevents – checks for kernel perf pmu support"
---

<h2 class="name">NAME</h2>
<p> op-check-perfevents &#8211; checks for kernel perf pmu support </p>
<h2>SYNOPSIS</h2>
<p> <code>op-check-perfevents</code> [ <i>options</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The small helper program <code>op-check-perfevents</code> determines whether the kernel supports the perf interface and returns a zero exit status if the perf pmu support is available.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help / -h</code></p>
<dd> Show usage help message. </p>
<dt><code>&#8211;verbose / -v</code></p>
<dd> Print string describing the error number of perf_event_open syscall </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> No special environment variables are recognised by op-check-perfevents. </p>
<h2>VERSION</h2>
<dl>
<dt>This man page is current for oprofile-0.9.9.</p>
<dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code>/usr/share/doc/oprofile/,</code> <code><a href="/docs/linux/man/1-oprofile/">oprofile</a>(1)</code> </p>
<h2>Index</h2>
