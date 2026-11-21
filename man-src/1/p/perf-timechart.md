---

title: "perf-timechart(1)"
name: "perf-timechart"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-timechart/"
description: "perf-timechart – Tool to visualize total system behavior during a workload"
---

<p> perf-timechart &#8211; Tool to visualize total system behavior during a workload </p>
<h2>SYNOPSIS</h2>
<h2>DESCRIPTION</h2>
<p> There are two variants of perf timechart: </p>
<dl>
<dt>
</dt><dd>
<pre>
'perf timechart record &lt;command&gt;' to record the system level events
of an arbitrary workload. By default timechart records only scheduler
and CPU events (task switches, running times, CPU power states, etc),
but it's possible to record IO (disk, network) activity using -I argument.
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
'perf timechart' to turn a trace into a Scalable Vector Graphics file,
that can be viewed with popular SVG viewers such as 'Inkscape'. Depending
on the events in the perf.data file, timechart will contain scheduler/cpu
events or IO events.
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
In IO mode, every bar has two charts: upper and lower.
Upper bar shows incoming events (disk reads, ingress network packets).
Lower bar shows outgoing events (disk writes, egress network packets).
There are also poll bars which show how much time application spent
in poll/epoll/select syscalls.
</pre>
</dd></dl>
<h2>TIMECHART OPTIONS</h2>
<p> -o, &#8211;output=</p>
<dl>
<dt>
</dt><dd> Select the output file (default: output.svg)</dd></dl>
<p> -i, &#8211;input=</p>
<dl>
<dt>
</dt><dd> Select the input file (default: perf.data unless stdin is a fifo)</dd></dl>
<p> -w, &#8211;width=</p>
<dl>
<dt>
</dt><dd> Select the width of the SVG file (default: 1000)</dd></dl>
<p> -P, &#8211;power-only</p>
<dl>
<dt>
</dt><dd> Only output the CPU power section of the diagram</dd></dl>
<p> -T, &#8211;tasks-only</p>
<dl>
<dt>
</dt><dd> Don&#8217;t output processor state transitions</dd></dl>
<p> -p, &#8211;process</p>
<dl>
<dt>
</dt><dd> Select the processes to display, by name or PID</dd></dl>
<p> &#8211;symfs=&lt;directory&gt;</p>
<dl>
<dt>
</dt><dd> Look for files with symbols relative to this directory.</dd></dl>
<p> -n, &#8211;proc-num</p>
<dl>
<dt>
</dt><dd> Print task info for at least given number of tasks.</dd></dl>
<p> -t, &#8211;topology</p>
<dl>
<dt>
</dt><dd> Sort CPUs according to topology.</dd></dl>
<p> &#8211;highlight=&lt;duration_nsecs|task_name&gt;</p>
<dl>
<dt>
</dt><dd> Highlight tasks (using different color) that run more than given duration or tasks with given name. If number is given it&#8217;s interpreted as number of nanoseconds. If non-numeric string is given it&#8217;s interpreted as task name.</dd></dl>
<p> &#8211;io-skip-eagain</p>
<dl>
<dt>
</dt><dd> Don&#8217;t draw EAGAIN IO events.</dd></dl>
<p> &#8211;io-min-time=&lt;nsecs&gt;</p>
<dl>
<dt>
</dt><dd> Draw small events as if they lasted min-time. Useful when you need to see very small and fast IO. It&#8217;s possible to specify ms or us suffix to specify time in milliseconds or microseconds. Default value is 1ms.</dd></dl>
<p> &#8211;io-merge-dist=&lt;nsecs&gt;</p>
<dl>
<dt>
</dt><dd> Merge events that are merge-dist nanoseconds apart. Reduces number of figures on the SVG and makes it more render-friendly. It&#8217;s possible to specify ms or us suffix to specify time in milliseconds or microseconds. Default value is 1us.</dd></dl>
<h2>RECORD OPTIONS</h2>
<p> -P, &#8211;power-only</p>
<dl>
<dt>
</dt><dd> Record only power-related events</dd></dl>
<p> -T, &#8211;tasks-only</p>
<dl>
<dt>
</dt><dd> Record only tasks-related events</dd></dl>
<p> -I, &#8211;io-only</p>
<dl>
<dt>
</dt><dd> Record only io-related events</dd></dl>
<p> -g, &#8211;callchain</p>
<dl>
<dt>
</dt><dd> Do call-graph (stack chain/backtrace) recording</dd></dl>
<h2>EXAMPLES</h2>
<p> $ perf timechart record git pull </p>
<dl>
<dt>
</dt><dd>
<pre><code>
[perf record:Woken up 13 times to write data]
    [perf record:Captured and wrote 4.253 MB perf.data(~185801 samples)]
</code></pre>
</dd></dl>
<p> $ perf timechart </p>
<dl>
<dt>
</dt><dd>
<pre>
Written 10.2 seconds of trace to output.svg.
</pre>
</dd></dl>
<p> Record system-wide timechart: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ perf timechart record
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
then generate timechart and highlight 'gcc' tasks:
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
$ perf timechart --highlight gcc
</pre>
</dd></dl>
<p> Record system-wide IO events: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ perf timechart record -I
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
then generate timechart:
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
$ perf timechart
</pre>
</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-record/">perf-record</a></code>(1) </p>
