---
title: "dbrowaccumulate(1)"
name: "dbrowaccumulate"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbrowaccumulate/"
description: "dbrowaccumulate – compute a running sum of a column"
---

<h2 class="name">NAME</h2>
<p> dbrowaccumulate &#8211; compute a running sum of a column </p>
<h2>SYNOPSIS</h2>
<p> dbrowaccumulate [-C increment_constant] [-I initial_value] [-c increment_column] [-N new_column_name]</p>
<h2>DESCRIPTION</h2>
<p> Compute a running sum over a column of data, or of a constant incremented per row, perhaps to generate a cumulative distribution. </p>
<p> What to accumulate is specified by <tt>&quot;-c&quot;</tt> or <tt>&quot;-C&quot;</tt>. </p>
<p> The new column is named by the <tt>&quot;-N&quot;</tt> argument, defaulting to <tt>&quot;accum&quot;</tt>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> or <code>&#8211;column</code> <font SIZE="-1">COLUMN</font></p>
<dd> Accumulate values from the given <font SIZE="-1">COLUMN.</font> No default.</p>
<dt><code>-C</code> or <code>&#8211;constant</code> K</p>
<dd> Accumulate the given constant K for each row of input. No default.</p>
<dt><code>-I</code> or <code>&#8211;initial-value</code> I</p>
<dd> Start accumulation at value I. Defaults to zero.</p>
<dt><code>-N</code> or <code>&#8211;new-name</code> N</p>
<dd> Name the new column N. Defaults to <tt>&quot;accum&quot;</tt>.</dl>
<p> This module also supports the standard fsdb options:</p>
<dl>
<dt><code>-d</code></p>
<dd> Enable debugging output.</p>
<dt><code>-i</code> or <code>&#8211;input</code> InputSource</p>
<dd> Read from InputSource, typically a file name, or <tt>&quot;-&quot;</tt> for standard input, or (if in Perl) a IO::Handle, Fsdb::IO or Fsdb::BoundedQueue objects.</p>
<dt><code>-o</code> or <code>&#8211;output</code> OutputDestination</p>
<dd> Write to OutputDestination, typically a file name, or <tt>&quot;-&quot;</tt> for standard output, or (if in Perl) a IO::Handle, Fsdb::IO or Fsdb::BoundedQueue objects.</p>
<dt><code>&#8211;autorun</code> or <code>&#8211;noautorun</code></p>
<dd> By default, programs process automatically, but Fsdb::Filter objects in Perl do not run until you invoke the <i>run()</i> method. The <tt>&quot;--(no)autorun&quot;</tt> option controls that behavior within Perl.</p>
<dt><code>&#8211;help</code></p>
<dd> Show help.</p>
<dt><code>&#8211;man</code></p>
<dd> Show full manual.</dl>
<h2>SAMPLE USAGE</h2>
<h3>Input:</h3>
<pre>
    #fsdb      diff
    0.0
    00.000938
    00.001611
    00.001736
    00.002006
    00.002049
    #  | /home/johnh/BIN/DB/dbrow 
    #  | /home/johnh/BIN/DB/dbcol diff
    #  | dbsort diff
</pre>
<h3>Command:</h3>
<pre>
    cat DATA/kitrace.fsdb | dbrowaccumulate -c diff
</pre>
<h3>Output:</h3>
<pre>
    #fsdb      diff    accum
    0.0     0
    00.000938       .000938
    00.001611       .002549
    00.001736       .004285
    00.002006       .006291
    00.002049       .00834
    #  | /home/johnh/BIN/DB/dbrow 
    #  | /home/johnh/BIN/DB/dbcol diff
    #  | dbsort diff
    #  | /home/johnh/BIN/DB/dbrowaccumulate diff
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb, dbrowenumerate.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2008 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
