---
title: "dbsort(1)"
name: "dbsort"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbsort/"
description: "dbsort – sort rows based on the the specified columns"
---

<h2 class="name">NAME</h2>
<p> dbsort &#8211; sort rows based on the the specified columns </p>
<h2>SYNOPSIS</h2>
<pre><code>
dbsort[-M MemLimit][-T TemporaryDirectory][-nNrR] column[column...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Sort all input rows as specified by the numeric or lexical columns. </p>
<p> Dbsort consumes a fixed amount of memory regardless of input size. (It reverts to temporary files on disk if necessary, based on the -M and -T options.) </p>
<p> The sort should be stable, but this has not yet been verified. </p>
<p> For large inputs (those that spill to disk), dbsort will do some of the merging in parallel, if possible. The &lt;&#8211;parallel&gt; option can control the degree of parallelism, if desired.</p>
<h2>OPTIONS</h2>
<p> General option:</p>
<dl>
<dt><code>-M MaxMemBytes</code></dt>
<dd> Specify an approximate limit on memory usage (in bytes). Larger values allow faster sorting because more operations happen in-memory, provided you have enough memory.</dd>
<dt><code>-T TmpDir</code></dt>
<dd> where to put tmp files. Also uses environment variable <font SIZE="-1">TMPDIR,</font> if -T is not specified. Default is /tmp.</dd>
<dt>&lt;&#8211;parallelism&gt; N</dt>
<dd> Allow up to N merges to happen in parallel. Default is the number of CPUs in the machine.</dd></dl>
<p> Sort specification options (can be interspersed with column names):</p>
<dl>
<dt><code>-r</code> or <code>&#8211;descending</code></dt>
<dd> sort in reverse order (high to low)</dd>
<dt><code>-R</code> or <code>&#8211;ascending</code></dt>
<dd> sort in normal order (low to high)</dd>
<dt><code>-n</code> or <code>&#8211;numeric</code></dt>
<dd> sort numerically</dd>
<dt><code>-N</code> or <code>&#8211;lexical</code></dt>
<dd> sort lexicographically</dd></dl>
<p> This module also supports the standard fsdb options:</p>
<dl>
<dt><code>-d</code></dt>
<dd> Enable debugging output.</dd>
<dt><code>-i</code> or <code>&#8211;input</code> InputSource</dt>
<dd> Read from InputSource, typically a file name, or <tt>&quot;-&quot;</tt> for standard input, or (if in Perl) a IO::Handle, Fsdb::IO or Fsdb::BoundedQueue objects.</dd>
<dt><code>-o</code> or <code>&#8211;output</code> OutputDestination</dt>
<dd> Write to OutputDestination, typically a file name, or <tt>&quot;-&quot;</tt> for standard output, or (if in Perl) a IO::Handle, Fsdb::IO or Fsdb::BoundedQueue objects.</dd>
<dt><code>&#8211;autorun</code> or <code>&#8211;noautorun</code></dt>
<dd> By default, programs process automatically, but Fsdb::Filter objects in Perl do not run until you invoke the <i>run()</i> method. The <tt>&quot;--(no)autorun&quot;</tt> option controls that behavior within Perl.</dd>
<dt><code>&#8211;header</code> H</dt>
<dd> Use H as the full Fsdb header, rather than reading a header from then input.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Show help.</dd>
<dt><code>&#8211;man</code></dt>
<dd> Show full manual.</dd></dl>
<h2>SAMPLE USAGE</h2>
<h3>Input:</h3>
<pre>
    #fsdb cid cname
    10 pascal
    11 numanal
    12 os
</pre>
<h3>Command:</h3>
<pre>
    cat data.fsdb | dbsort cname
</pre>
<h3>Output:</h3>
<pre>
    #fsdb      cid     cname
    11 numanal
    12 os
    10 pascal
    #  | dbsort cname
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-dbmerge/">dbmerge</a></i>(1), <i><a href="/docs/linux/man/1-dbmapreduce/">dbmapreduce</a></i>(1), <i>Fsdb</i>(3)</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
