---
title: "dbfilecat(1)"
name: "dbfilecat"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbfilecat/"
description: "dbfilecat – concatenate two files with identical schema"
---

<h2 class="name">NAME</h2>
<p> dbfilecat &#8211; concatenate two files with identical schema </p>
<h2>SYNOPSIS</h2>
<pre><code>
dbfilecat-- input A.fsdb[--input B.fsdb...]
</code></pre>
<p> or </p>
<pre>
    echo A.fsdb | dbfilecat --xargs
</pre>
<h2>DESCRIPTION</h2>
<p> Concatenate all provided input files, producing one result. We remove extra header lines. </p>
<p> Inputs can both be specified with <tt>&quot;--input&quot;</tt>, or one can come from standard input and the other from <tt>&quot;--input&quot;</tt>. With <tt>&quot;--xargs&quot;</tt>, each line of standard input is a filename for input. </p>
<p> Inputs must have identical schemas (columns, column order, and field separators). </p>
<p> Like dbmerge, but no worries about sorting, and with no arguments we read standard input (although that&#8217;s not very useful).</p>
<h2>OPTIONS</h2>
<p> General option:</p>
<dl>
<dt><code>&#8211;xargs</code></p>
<dd> Expect that input filenames are given, one-per-line, on standard input. (In this case, merging can start incrementally.</p>
<dt><code>&#8211;removeinputs</code></p>
<dd> Delete the source files after they have been consumed. (Defaults off, leaving the inputs in place.) </p>
<p> This module also supports the standard fsdb options:</p>
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
    dbfilecat --input a.fsdb --input b.fsdb
</pre>
<h3>Output:</h3>
<pre>
    #fsdb      cid     cname
    11 numanal
    10 pascal
    12 os
    13 statistics
    #  | dbmerge --input a.fsdb --input b.fsdb
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-dbmerge/">dbmerge</a></i>(1), <i><a href="/docs/linux/man/3-fsdb/">Fsdb</a></i>(3)</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 2013-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
