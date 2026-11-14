---
title: "lsmem(1)"
name: "lsmem"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lsmem/"
description: "lsmem – list the ranges of available memory with their online status"
---

<h2 class="name">NAME</h2>
<p> lsmem &#8211; list the ranges of available memory with their online status </p>
<h2>SYNOPSIS</h2>
<p> <code>lsmem</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> The <code>lsmem</code> command lists the ranges of available memory with their online status. The listed memory blocks correspond to the memory block representation in sysfs. The command also shows the memory block size and the amount of memory in online and offline state. </p>
<p> The default output compatible with original implementation from s390-tools, but it&#8217;s strongly recommended to avoid using default outputs in your scripts. Always explicitly define expected columns by using the <code>&#8211;output</code> option together with a columns list in environments where a stable output is required. </p>
<p> The <code>lsmem</code> command lists a new memory range always when the current memory block distinguish from the previous block by some output column. This default behavior is possible to override by the <code>&#8211;split</code> option (e.g., <code>lsmem &#8211;split=ZONES</code>). The special word &quot;none&quot; may be used to ignore all differences between memory blocks and to create as large as possible continuous ranges. The opposite semantic is <code>&#8211;all</code> to list individual memory blocks. </p>
<p> Note that some output columns may provide inaccurate information if a split policy forces <code>lsmem</code> to ignore differences in some attributes. For example if you merge removable and non-removable memory blocks to the one range than all the range will be marked as non-removable on <code>lsmem</code> output. </p>
<p> Not all columns are supported on all systems. If an unsupported column is specified, <code>lsmem</code> prints the column but does not provide any data for it. </p>
<p> Use the <code>&#8211;help</code> option to see the columns description.</p>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dt>
<dd> List each individual memory block, instead of combining memory blocks with similar attributes.</dl>
<p> <code>-b</code>, <code>&#8211;bytes</code></p>
<dl>
<dt>
<dd> Print the SIZE column in bytes rather than in a human-readable format.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<p> <code>-J</code>, <code>&#8211;json</code></p>
<dl>
<dt>
<dd> Use JSON output format.</dl>
<p> <code>-n</code>, <code>&#8211;noheadings</code></p>
<dl>
<dt>
<dd> Do not print a header line.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>list</i></p>
<dl>
<dt>
<dd> Specify which output columns to print. Use <code>&#8211;help</code> to get a list of all supported columns. The default list of columns may be extended if <i>list</i> is specified in the format <code>+</code><i>list</i> (e.g., <code>lsmem -o +NODE</code>).</dl>
<p> <code>&#8211;output-all</code></p>
<dl>
<dt>
<dd> Output all available columns.</dl>
<p> <code>-P</code>, <code>&#8211;pairs</code></p>
<dl>
<dt>
<dd> Produce output in the form of key=&quot;value&quot; pairs. All potentially unsafe value characters are hex-escaped (
