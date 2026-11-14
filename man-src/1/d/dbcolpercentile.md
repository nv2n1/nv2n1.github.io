---
title: "dbcolpercentile(1)"
name: "dbcolpercentile"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbcolpercentile/"
description: "dbcolpercentile – compute percentiles or ranks for an existing column"
---

<h2 class="name">NAME</h2>
<p> dbcolpercentile &#8211; compute percentiles or ranks for an existing column </p>
<h2>SYNOPSIS</h2>
<pre>
    dbcolpercentile [-rplhS] column
</pre>
<h2>DESCRIPTION</h2>
<p> Compute a percentile of a column of numbers. The new column will be called <i>percentile</i> or <i>rank</i>. Non-numeric records are handled as in other programs. </p>
<p> If the data is pre-sorted and only a rank is requested, no extra storage is required. In all other cases, a full copy of data is buffered on disk.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p</code> or <code>&#8211;percentile</code></p>
<dd> Show percentile (default).</p>
<dt><code>-P</code> or <code>&#8211;rank</code> or <code>&#8211;nopercentile</code></p>
<dd> Compute ranks instead of percentiles.</p>
<dt><code>&#8211;fraction</code></p>
<dd> Show fraction (percentage, except between 0 and 1, not cumulative fraction).</p>
<dt><code>-a</code> or <code>&#8211;include-non-numeric</code></p>
<dd> Compute stats over all records (treat non-numeric records as zero rather than just ignoring them).</p>
<dt><code>-S</code> or <code>&#8211;pre-sorted</code></p>
<dd> Assume data is already sorted. With one -S, we check and confirm this precondition. When repeated, we skip the check.</p>
<dt><code>-f </code><font SIZE="-1"><code>FORMAT</code></font> or <code>&#8211;format </code><font SIZE="-1"><code>FORMAT</code></font></p>
<dd> Specify a <i><a href="/docs/linux/man/3-printf/">printf</a></i>(3)-style format for output statistics. Defaults to <tt>&quot;%.5g&quot;</tt>.</p>
<dt><code>-T TmpDir</code></p>
<dd> where to put tmp files. Also uses environment variable <font SIZE="-1">TMPDIR,</font> if -T is not specified. Default is /tmp.</dl>
<p> Sort specification options (can be interspersed with column names):</p>
<dl>
<dt><code>-r</code> or <code>&#8211;descending</code></p>
<dd> sort in reverse order (high to low)</p>
<dt><code>-R</code> or <code>&#8211;ascending</code></p>
<dd> sort in normal order (low to high)</p>
<dt><code>-n</code> or <code>&#8211;numeric</code></p>
<dd> sort numerically (default)</p>
<dt><code>-N</code> or <code>&#8211;lexical</code></p>
<dd> sort lexicographically</dl>
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
    #fsdb name id test1
    a 1 80
    b 2 70
    c 3 65
    d 4 90
    e 5 70
    f 6 90
</pre>
<h3>Command:</h3>
<pre>
    cat DATA/grades.fsdb | dbcolpercentile test1
</pre>
<h3>Output:</h3>
<pre>
        #fsdb name id test1 percentile
        d       4       90      1
        f       6       90      1
        a       1       80      0.66667
        b       2       70      0.5
        e       5       70      0.5
        c       3       65      0.16667
        #  | dbsort -n test1
        #   | dbcolpercentile test1
</pre>
<h3>Command 2:</h3>
<pre>
    cat DATA/grades.fsdb | dbcolpercentile --rank test1
</pre>
<h3>Output 2:</h3>
<pre>
        #fsdb name id test1 rank
        d       4       90      1
        f       6       90      1
        a       1       80      3
        b       2       70      4
        e       5       70      4
        c       3       65      6
        #  | dbsort -n test1
        #   | dbcolpercentile --rank test1
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb. dbcolhisto.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
