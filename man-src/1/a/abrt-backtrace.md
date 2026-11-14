---
title: "abrt-backtrace(1)"
name: "abrt-backtrace"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-backtrace/"
description: "abrt-backtrace – a backtrace analyzer for abrt"
---

<h2>NAME</h2>
<p> abrt-backtrace &#8211; a backtrace analyzer for abrt</p>
<h2>SYNOPSIS</h2>
<p> <code>abrt-backtrace</code> [option]&#8230; [FILE]</p>
<h2>DESCRIPTION</h2>
<p> <i>abrt-backtrace</i> is a command line tool that analyzes backtraces produced by GDB and provides their textual representation useful for crash duplication detection. </p>
<p> By default, abrt-backtrace prints the backtrace tree created by parsing the input file. </p>
<h2>OPTIONS</h2>
<p> <code>Basic startup options</code></p>
<dl>
<dt>-V, &#8211;version</p>
<dd> Displays version of abrt-backtrace.</p>
<dt>-?, &#8211;help</p>
<dd> Print a help message describing all of abrt-backtrace’s command-line options. </p>
</dl>
<p> <code>Actions</code></p>
<dl>
<dt>-i, &#8211;independent</p>
<dd> Prints independent backtrace fallback. The &quot;independent backtrace&quot; is used as a fallback internal representation of backtrace when the internal parser fails to process the input due to unsupported format. </p>
</dl>
<p> <code>Various options</code></p>
<dl>
<dt>-n, &#8211;single-thread</p>
<dd> Removes all threads except the one that caused the crash from the internal representation of the backtrace.</p>
<dt>-d=N, &#8211;frame-depth=N</p>
<dd> Display only the top N frames in every thread. Frames that are a part of system error handling do not count to the N. So more than N frames can be displayed, but N of them are useful for examination. N must be larger than 1.</p>
<dt>-r, &#8211;remove-exit-handlers</p>
<dd> Do not display exit handlers and frames that comes after them in the backtrace.</p>
<dt>-m, &#8211;remove-noncrash-frames</p>
<dd> Do not display frames known as not causing the crash, but which are a common part of backtraces.</p>
<dt>-a, &#8211;rate</p>
<dd> Print backtrace rating from 0 to 4.</p>
<dt>-c, &#8211;crash-function</p>
<dd> Print crash function if it&#8217;s successfully detected.</p>
<dt>-p, &#8211;debug-parser</p>
<dd> Prints debug information when parsing the backtrace.</p>
<dt>-s, &#8211;debug-scanner</p>
<dd> Prints debug information when scanning the input file for the parser. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-abrtd/">abrtd</a></i>(8), <i><a href="/docs/linux/man/5-abrt-conf/">abrt.conf</a></i>(5), <i><a href="/docs/linux/man/1-abrt-cli/">abrt-cli</a></i>(1), <i><a href="/docs/linux/man/7-abrt-plugins/">abrt-plugins</a></i>(7) </p>
<h2>Index</h2>
