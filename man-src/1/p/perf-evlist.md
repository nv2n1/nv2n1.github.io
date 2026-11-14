---
title: "perf-evlist(1)"
name: "perf-evlist"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-evlist/"
description: "perf-evlist – List the event names in a perf.data file"
---

<h2 class="name">NAME</h2>
<p> perf-evlist &#8211; List the event names in a perf.data file </p>
<h2>SYNOPSIS</h2>
<pre>
<i>perf evlist &lt;options&gt;</i>
</pre>
<h2>DESCRIPTION</h2>
<p> This command displays the names of events sampled in a perf.data file.</p>
<h2>OPTIONS</h2>
<p> -i, &#8211;input=</p>
<dl>
<dt>
<dd> Input file name. (default: perf.data unless stdin is a fifo)</dl>
<p> -F, &#8211;freq=</p>
<dl>
<dt>
<dd> Show just the sample frequency used for each event.</dl>
<p> -v, &#8211;verbose=</p>
<dl>
<dt>
<dd> Show all fields.</dl>
<p> -g, &#8211;group</p>
<dl>
<dt>
<dd> Show event group information.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-record/">perf-record</a></code>(1), <code><a href="/docs/linux/man/1-perf-list/">perf-list</a></code>(1), <code><a href="/docs/linux/man/1-perf-report/">perf-report</a></code>(1) </p>
<h2>Index</h2>
