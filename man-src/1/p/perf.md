---
title: "perf(1)"
name: "perf"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf/"
description: "perf – Performance analysis tools for Linux"
---

<h2 class="name">NAME</h2>
<p> perf &#8211; Performance analysis tools for Linux </p>
<h2>SYNOPSIS</h2>
<pre><code>
perf[--version][--help][OPTIONS] COMMAND[ARGS]
</code></pre>
<h2>OPTIONS</h2>
<p> &#8211;debug</p>
<dl>
<dt>
<dd> Setup debug variable (just verbose for now) in value range (0, 10). Use like: &#8211;debug verbose # sets verbose = 1 &#8211;debug verbose=2 # sets verbose = 2</dl>
<h2>DESCRIPTION</h2>
<p> Performance counters for Linux are a new kernel-based subsystem that provide a framework for all things performance analysis. It covers hardware level (CPU/PMU, Performance Monitoring Unit) features and software features (software counters, tracepoints) as well.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-stat/">perf-stat</a></code>(1), <code><a href="/docs/linux/man/1-perf-top/">perf-top</a></code>(1), <code><a href="/docs/linux/man/1-perf-record/">perf-record</a></code>(1), <code><a href="/docs/linux/man/1-perf-report/">perf-report</a></code>(1), <code><a href="/docs/linux/man/1-perf-list/">perf-list</a></code>(1) </p>
<h2>Index</h2>
