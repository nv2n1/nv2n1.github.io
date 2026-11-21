---
title: "perf-lock(1)"
name: "perf-lock"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-lock/"
description: "perf-lock – Analyze lock events"
---

<h2 class="name">NAME</h2>
<p> perf-lock &#8211; Analyze lock events </p>
<h2>SYNOPSIS</h2>
<pre>
<i>perf lock</i> {record|report|script|info}
</pre>
<h2>DESCRIPTION</h2>
<p> You can analyze various lock behaviours and statistics with this <i>perf lock</i> command. </p>
<dl>
<dt>
</dt><dd>
<pre>
'perf lock record &lt;command&gt;' records lock events
between start and end &lt;command&gt;. And this command
produces the file &quot;perf.data&quot; which contains tracing
results of lock events.
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
'perf lock report' reports statistical data.
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
'perf lock script' shows raw lock events.
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
'perf lock info' shows metadata like threads or addresses
of lock instances.
</pre>
</dd></dl>
<h2>COMMON OPTIONS</h2>
<p> -i, &#8211;input=&lt;file&gt;</p>
<dl>
<dt>
</dt><dd> Input file name. (default: perf.data unless stdin is a fifo)</dd></dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
</dt><dd> Be more verbose (show symbol address, etc).</dd></dl>
<p> -D, &#8211;dump-raw-trace</p>
<dl>
<dt>
</dt><dd> Dump raw trace in ASCII.</dd></dl>
<h2>REPORT OPTIONS</h2>
<p> -k, &#8211;key=&lt;value&gt;</p>
<dl>
<dt>
</dt><dd> Sorting key. Possible values: acquired (default), contended, avg_wait, wait_total, wait_max, wait_min.</dd></dl>
<h2>INFO OPTIONS</h2>
<p> -t, &#8211;threads</p>
<dl>
<dt>
</dt><dd> dump thread list in perf.data</dd></dl>
<p> -m, &#8211;map</p>
<dl>
<dt>
</dt><dd> dump map of lock instances (address:name table)</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf/">perf</a></code>(1) </p>
