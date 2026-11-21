---

title: "perf-sched(1)"
name: "perf-sched"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-sched/"
description: "perf-sched – Tool to trace/measure scheduler properties (latencies)"
---

<p> perf-sched &#8211; Tool to trace/measure scheduler properties (latencies) </p>
<h2>SYNOPSIS</h2>
<pre>
<i>perf sched</i> {record|latency|map|replay|script}
</pre>
<h2>DESCRIPTION</h2>
<p> There are five variants of perf sched: </p>
<dl>
<dt>
</dt><dd>
<pre>
'perf sched record &lt;command&gt;' to record the scheduling events
of an arbitrary workload.
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
'perf sched latency' to report the per task scheduling latencies
and other scheduling properties of the workload.
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
'perf sched script' to see a detailed trace of the workload that
 was recorded (aliased to 'perf script' for now).
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
'perf sched replay' to simulate the workload that was recorded
via perf sched record. (this is done by starting up mockup threads
that mimic the workload based on the events in the trace. These
threads can then replay the timings (CPU runtime and sleep patterns)
of the workload as it occurred when it was recorded - and can repeat
it a number of times, measuring its performance.)
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
'perf sched map' to print a textual context-switching outline of
workload captured via perf sched record.  Columns stand for
individual CPUs, and the two-letter shortcuts stand for tasks that
are running on a CPU. A '*' denotes the CPU that had the event, and
a dot signals an idle CPU.
</pre>
</dd></dl>
<h2>OPTIONS</h2>
<p> -i, &#8211;input=&lt;file&gt;</p>
<dl>
<dt>
</dt><dd> Input file name. (default: perf.data unless stdin is a fifo)</dd></dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
</dt><dd> Be more verbose. (show symbol address, etc)</dd></dl>
<p> -D, &#8211;dump-raw-trace=</p>
<dl>
<dt>
</dt><dd> Display verbose dump of the sched data.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-record/">perf-record</a></code>(1) </p>
