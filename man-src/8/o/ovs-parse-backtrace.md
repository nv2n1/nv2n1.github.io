---
title: "ovs-parse-backtrace(8)"
name: "ovs-parse-backtrace"
section: "8"
letter: "o"
url: "/docs/linux/man/8-ovs-parse-backtrace/"
description: "ovs-parse-backtrace – parses ovs-appctl backtrace output"
---

<p>ovs-parse-backtrace &#8211; parses ovs-appctl backtrace output</p>
<h2>Synopsis</h2>
<p><code>ovs-appctl backtrace</code> | <code>ovs-parse-backtrace</code> [<i>binary</i>] </p>
<p> <code>ovs-parse-backtrace</code> [<i>binary</i>] &lt; <i>backtrace</i></p>
<h2>Description</h2>
<p>In some configurations, many Open vSwitch daemons can produce a series of backtraces using the <code>ovs-appctl backtrace</code> command. Users can analyze these backtraces to figure out what the given Open vSwitch daemon may be spending most of its time doing. <code>ovs-parse-backtrace</code> makes this output easier to interpret. </p>
<p> The <code>ovs-appctl backtrace</code> output must be supplied on standard input. The binary that produced the output should be supplied as the sole non-option argument. For best results, the binary should have debug symbols.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd>Prints a usage message and exits.</dl>
<p> <code>&#8211;version</code> Prints the version and exits.</p>
