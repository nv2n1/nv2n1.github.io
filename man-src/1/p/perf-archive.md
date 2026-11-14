---
title: "perf-archive(1)"
name: "perf-archive"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-archive/"
description: "perf-archive – Create archive with object files with build-ids found in perf.data file"
---

<h2 class="name">NAME</h2>
<p> perf-archive &#8211; Create archive with object files with build-ids found in perf.data file </p>
<h2>SYNOPSIS</h2>
<pre>
<i>perf archive</i> [file]
</pre>
<h2>DESCRIPTION</h2>
<p> This command runs perf-buildid-list &#8211;with-hits, and collects the files with the buildids found so that analysis of perf.data contents can be possible on another machine.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-record/">perf-record</a></code>(1), <code><a href="/docs/linux/man/1-perf-buildid-list/">perf-buildid-list</a></code>(1), <code><a href="/docs/linux/man/1-perf-report/">perf-report</a></code>(1) </p>
<h2>Index</h2>
