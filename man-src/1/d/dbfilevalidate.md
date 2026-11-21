---
title: "dbfilevalidate(1)"
name: "dbfilevalidate"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbfilevalidate/"
description: "dbfilevalidate – insure the source input is a well-formed Fsdb file"
---

<h2 class="name">NAME</h2>
<p> dbfilevalidate &#8211; insure the source input is a well-formed Fsdb file </p>
<h2>SYNOPSIS</h2>
<pre>
    dbfilevalidate [-vc]
</pre>
<h2>DESCRIPTION</h2>
<p> Validates the input file to make sure it is a well-formed fsdb file. If the file is well-formed, it outputs the whole file and exits with a good exit code. For invalid files, it exits with an error exit code and embedded error messages in the stream as comments with &#8220;***&#8221; in them. </p>
<p> Currently this program checks for rows with missing or extra columns.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code> or <code>&#8211;errors-only</code></dt>
<dd> Output only broken lines, not the whole thing.</dd>
<dt><code>-c</code> or <code>&#8211;correct</code></dt>
<dd> Correct errors, if possible. Pad out rows with the empty value; truncate rows with extra values. If errors can be corrected the program exits with a good return code.</dd>
<dt>&quot;-e E&quot; or &quot;&#8211;empty E&quot;</dt>
<dd> give value E as the value for empty (null) records</dd></dl>
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
<dt><code>&#8211;help</code></dt>
<dd> Show help.</dd>
<dt><code>&#8211;man</code></dt>
<dd> Show full manual.</dd></dl>
<h2>SAMPLE USAGE</h2>
<h3>Input:</h3>
<pre>
    #fsdb sid cid
    1 10
    2
    1 12
    2 12
</pre>
<h3>Command:</h3>
<pre>
    cat TEST/dbfilevalidate_ex.in | dbvalidate
</pre>
<h3>Output:</h3>
<pre>
    #fsdb sid cid
    1 10
    2
    # *** line above is missing field cid.
    1 12
    2 12
    #  | dbfilevalidate
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2008 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
