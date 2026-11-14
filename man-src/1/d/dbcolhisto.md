---
title: "dbcolhisto(1)"
name: "dbcolhisto"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbcolhisto/"
description: "dbcolhisto – compute a histogram over a column of Fsdb data"
---

<h2 class="name">NAME</h2>
<p> dbcolhisto &#8211; compute a histogram over a column of Fsdb data </p>
<h2>SYNOPSIS</h2>
<p> dbcolhisto [-ag] [-W BucketWidth] [-S BucketStart] [-E BucketEnd] [-N NumberOfBuckets] column</p>
<h2>DESCRIPTION</h2>
<p> This program computes a histogram over a column of data. Records containing non-numeric data are considered null do not contribute to the stats (optionally they are treated as zeros). </p>
<p> Defaults to 10 buckets over the exact range of data. Up to three parameters (number of buckets, start, end, and width) can be specified, the rest default accordingly. </p>
<p> Buckets range from a value (given the the low column) to just below the next low value and buckets are equal width. If necessary, extra &#8220;&lt;min&#8221; and &#8220;&gt;max&#8221; buckets are created. By default, the last bucket includes max (and is thus infinitesimally larger than the other buckets). This irregularity can be removed with the <tt>&quot;-I&quot;</tt> option. </p>
<p> This program requires O(number of buckets) memory and O(size of data) temporary disk space.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-W</code> or <code>&#8211;width</code> N</p>
<dd> Gives with width of each bucket, in data units. Default is whatever gives 10 buckets over the whole range of data.</p>
<dt><code>-S</code> or <code>&#8211;start</code> N</p>
<dd> Buckets start at value N, in data units. Default is the minimum data value.</p>
<dt><code>-E</code> or <code>&#8211;end</code> N</p>
<dd> Buckets end at value N, in data units. Default is the maximum data value.</p>
<dt><code>-N</code> or <code>&#8211;number</code> N</p>
<dd> Create N buckets. The default is 10 buckets.</p>
<dt><code>-g</code> or <code>&#8211;graphical</code></p>
<dd> Generate a graphical histogram (with asterisks). Default is numeric.</p>
<dt><code>-I</code> or <code>&#8211;last-inclusive</code></p>
<dd> Make the last bucket non-inclusive of the last value.</p>
<dt><code>-a</code></p>
<dd> Compute stats over all records (treat non-numeric records as zero rather than just ignoring them). Default is non-numeric records are ignored.</dl>
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
    cat DATA/grades.fsdb | dbcolhisto -S 0 -E 100 -N 10 test1
</pre>
<h3>Output:</h3>
<pre>
    #fsdb low histogram
    0       0
    10      0
    20      0
    30      0
    40      0
    50      0
    60      1
    70      2
    80      1
    90      2
    #  | dbcolhisto -S 0 -E 100 -N 10 test1
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb, dbcolpercentile, dbcolstats</p>
<h2>BUGS</h2>
<p> This program could run in constant memory with no external storage when the buckets are pre-specified. That optimization is not implemented.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2008 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
