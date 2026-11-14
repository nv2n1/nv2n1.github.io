---
title: "perf-buildid-list(1)"
name: "perf-buildid-list"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-buildid-list/"
description: "perf-buildid-list – List the buildids in a perf.data file"
---

<h2 class="name">NAME</h2>
<p> perf-buildid-list &#8211; List the buildids in a perf.data file </p>
<h2>SYNOPSIS</h2>
<pre>
<i>perf buildid-list &lt;options&gt;</i>
</pre>
<h2>DESCRIPTION</h2>
<p> This command displays the buildids found in a perf.data file, so that other tools can be used to fetch packages with matching symbol tables for use by perf report. </p>
<p> It can also be used to show the build id of the running kernel or in an ELF file using -i/&#8211;input.</p>
<h2>OPTIONS</h2>
<p> -H, &#8211;with-hits</p>
<dl>
<dt>
<dd> Show only DSOs with hits.</dl>
<p> -i, &#8211;input=</p>
<dl>
<dt>
<dd> Input file name. (default: perf.data unless stdin is a fifo)</dl>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> Don&#8217;t do ownership validation.</dl>
<p> -k, &#8211;kernel</p>
<dl>
<dt>
<dd> Show running kernel build id.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Be more verbose.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-record/">perf-record</a></code>(1), <code><a href="/docs/linux/man/1-perf-top/">perf-top</a></code>(1), <code><a href="/docs/linux/man/1-perf-report/">perf-report</a></code>(1) </p>
<h2>Index</h2>
