---

title: "dbfilecat(1)"
name: "dbfilecat"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbfilecat/"
description: "dbfilecat – concatenate two files with identical schema"
---

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
<dt><code>&#8211;xargs</code></dt>
<dd> Expect that input filenames are given, one-per-line, on standard input. (In this case, merging can start incrementally.</dd>
<dt><code>&#8211;removeinputs</code></dt>
<dd> Delete the source files after they have been consumed. (Defaults off, leaving the inputs in place.) </dd>
<p> This module also supports the standard fsdb options:</p>
<dt><code>-d</code></dt>
<dd> Enable debugging output.</dd>
<dt><code>-i</code> or <code>&#8211;input</code> InputSource</dt>
<dd> Read from InputSource, typically a file name, or <tt>&quot;-&quot;</tt> for standard input, or (if in Perl) a IO::Handle, Fsdb::IO or Fsdb::BoundedQueue objects.</dd>
<dt><code>-o</code> or <code>&#8211;output</code> OutputDestination</dt>
<dd> Write to OutputDestination, typically a file name, or <tt>&quot;-&quot;</tt> for standard output, or (if in Perl) a IO::Handle, Fsdb::IO or Fsdb::BoundedQueue objects.</dd>
<dt><code>&#8211;autorun</code> or <code>&#8211;noautorun</code></dt>
<dd> By default, programs process automatically, but Fsdb::Filter objects in Perl do not run until you invoke the <i>run()</i> method. The <tt>&quot;--(no)autorun&quot;</tt> option controls that behavior within Perl.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Show help.</dd>
<dt><code>&#8211;man</code></dt>
<dd> Show full manual.</dd></dl>
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
<p> <i><a href="/docs/linux/man/1-dbmerge/">dbmerge</a></i>(1), <i>Fsdb</i>(3)</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 2013-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the GNU general public license, version 2. See the file COPYING with the distribution for details. </p>
