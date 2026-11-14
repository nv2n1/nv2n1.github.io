---
title: "perf-inject(1)"
name: "perf-inject"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-inject/"
description: "perf-inject – Filter to augment the events stream with additional information"
---

<h2 class="name">NAME</h2>
<p> perf-inject &#8211; Filter to augment the events stream with additional information </p>
<h2>SYNOPSIS</h2>
<pre>
<i>perf inject &lt;options&gt;</i>
</pre>
<h2>DESCRIPTION</h2>
<p> perf-inject reads a perf-record event stream and repipes it to stdout. At any point the processing code can inject other events into the event stream &#8211; in this case build-ids (-b option) are read and injected as needed into the event stream. </p>
<p> Build-ids are just the first user of perf-inject &#8211; potentially anything that needs userspace processing to augment the events stream with additional information could make use of this facility.</p>
<h2>OPTIONS</h2>
<p> -b, &#8211;build-ids=</p>
<dl>
<dt>
<dd> Inject build-ids into the output stream</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Be more verbose.</dl>
<p> -i, &#8211;input=</p>
<dl>
<dt>
<dd> Input file name. (default: stdin)</dl>
<p> -o, &#8211;output=</p>
<dl>
<dt>
<dd> Output file name. (default: stdout)</dl>
<p> -s, &#8211;sched-stat</p>
<dl>
<dt>
<dd> Merge sched_stat and sched_switch for getting events where and how long tasks slept. sched_switch contains a callchain where a task slept and sched_stat contains a timeslice how long a task slept.</dl>
<p> &#8211;kallsyms=&lt;file&gt;</p>
<dl>
<dt>
<dd> kallsyms pathname</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-record/">perf-record</a></code>(1), <code><a href="/docs/linux/man/1-perf-report/">perf-report</a></code>(1), <code><a href="/docs/linux/man/1-perf-archive/">perf-archive</a></code>(1) </p>
<h2>Index</h2>
