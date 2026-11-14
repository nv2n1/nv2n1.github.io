---
title: "dbmerge2(1)"
name: "dbmerge2"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbmerge2/"
description: "dbmerge2 – merge exactly two inputs in sorted order based on the the specified columns"
---

<h2 class="name">NAME</h2>
<p> dbmerge2 &#8211; merge exactly two inputs in sorted order based on the the specified columns </p>
<h2>SYNOPSIS</h2>
<pre><code>
dbmerge2-- input A.fsdb-- input B.fsdb[-T TemporaryDirectory][-nNrR] column[column...]
</code></pre>
<p> or<br />
&nbsp;<wbr>cat A.fsdb | dbmerge2 &#8211;input B.fsdb&nbsp;<wbr>[-T TemporaryDirectory]&nbsp;<wbr>[-nNrR]&nbsp;<wbr>column&nbsp;<wbr>[column&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Merge exactly two sorted input files, producing one sorted result. Inputs can both be specified with <tt>&quot;--input&quot;</tt>, or one can come from standard input and the other from <tt>&quot;--input&quot;</tt>. </p>
<p> Inputs must have identical schemas (columns, column order, and field separators). </p>
<p> Dbmerge2 consumes a fixed amount of memory regardless of input size. </p>
<p> Although described above as a command line too, the command line version of dbmerge2 is not installed by default. Dbmerge2 is used primarily internal to perl; <i><a href="/docs/linux/man/1-dbmerge/">dbmerge</a></i>(1) is the command-line tool for user use.</p>
<h2>OPTIONS</h2>
<p> General option:</p>
<dl>
<dt><code>&#8211;saveoutput $OUT_REF</code></p>
<dd> Save output writer (for integration with other fsdb filters).</p>
<dt>&lt;-T TmpDir&gt;</p>
<dd> where to put tmp files. Also uses environment variable <font SIZE="-1">TMPDIR,</font> if -T is not specified. Default is /tmp.</dl>
<p> Sort specification options (can be interspersed with column names):</p>
<dl>
<dt><code>-r</code> or <code>&#8211;descending</code></p>
<dd> sort in reverse order (high to low)</p>
<dt><code>-R</code> or <code>&#8211;ascending</code></p>
<dd> sort in normal order (low to high)</p>
<dt><code>-n</code> or <code>&#8211;numeric</code></p>
<dd> sort numerically</p>
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
<p> File <i>a.fsdb</i>: </p>
<pre>
    #fsdb cid cname
    11 numanal
    10 pascal
</pre>
<p> File <i>b.fsdb</i>: </p>
<pre>
    #fsdb cid cname
    12 os
    13 statistics
</pre>
<h3>Command:</h3>
<pre>
    dbmerge2 --input a.fsdb --input b.fsdb cname
</pre>
<p> or </p>
<pre>
    cat a.fsdb | dbmerge2 --input b.fsdb cname
</pre>
<h3>Output:</h3>
<pre>
    #fsdb      cid     cname
    11 numanal
    12 os
    10 pascal
    13 statistics
    #  | dbmerge2 --input a.fsdb --input b.fsdb cname
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-dbmerge/">dbmerge</a></i>(1), <i><a href="/docs/linux/man/1-dbsort/">dbsort</a></i>(1), <i><a href="/docs/linux/man/3-fsdb/">Fsdb</a></i>(3)</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
