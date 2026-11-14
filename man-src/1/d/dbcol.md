---
title: "dbcol(1)"
name: "dbcol"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbcol/"
description: "dbcol – select columns from an Fsdb file"
---

<h2 class="name">NAME</h2>
<p> dbcol &#8211; select columns from an Fsdb file </p>
<h2>SYNOPSIS</h2>
<p> dbcol [-v] [-e -] [column&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Select one or more columns from the input database. If a value is given for empty columns with the -e option, then any named columns which don&#8217;t exist will be created. Otherwise, non-existent columns are an error. </p>
<p> Note: a safer way to create columns is dbcolcreate.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r</code> or <code>&#8211;relaxed-errors</code></p>
<dd> Relaxed error checking: ignore columns that aren&#8217;t there.</p>
<dt><code>-v</code> or <code>&#8211;invert-match</code></p>
<dd> Output all columns except those listed (like grep -v).</p>
<dt><code>-e</code> EmptyValue or <code>&#8211;empty</code></p>
<dd> Specify the value newly created columns get.</dl>
<p> and the standard fsdb options:</p>
<dl>
<dt><code>-d</code></p>
<dd> Enable debugging output.</p>
<dt><code>-i</code> or <code>&#8211;input</code> InputSource</p>
<dd> Read from InputSource, typically a file, or &#8211; for standard input, or (if in Perl) a IO::Handle, Fsdb::IO or Fsdb::BoundedQueue objects.</p>
<dt><code>-o</code> or <code>&#8211;output</code> OutputDestination</p>
<dd> Write to OutputDestination, typically a file, or &#8211; for standard output, or (if in Perl) a IO::Handle, Fsdb::IO or Fsdb::BoundedQueue objects.</p>
<dt><code>&#8211;autorun</code> or <code>&#8211;noautorun</code></p>
<dd> By default, programs process automatically, but Fsdb::Filter objects in Perl do not run until you invoke the <i>run()</i> method. The <tt>&quot;--(no)autorun&quot;</tt> option controls that behavior within Perl.</p>
<dt><code>&#8211;help</code></p>
<dd> Show help.</p>
<dt><code>&#8211;man</code></p>
<dd> Show full manual.</dl>
<h2>SAMPLE USAGE</h2>
<h3>Input:</h3>
<pre>
    #fsdb account passwd uid gid fullname homedir shell
    johnh * 2274 134 John_Heidemann /home/johnh /bin/bash
    greg * 2275 134 Greg_Johnson /home/greg /bin/bash
    root * 0 0 Root /root /bin/bash
    # this is a simple database
</pre>
<h3>Command:</h3>
<pre>
    cat DATA/passwd.fsdb account | dbcol account
</pre>
<h3>Output:</h3>
<pre>
    #fsdb      account
    johnh
    greg
    root
    # this is a simple database
    #  | dbcol account
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-dbcolcreate/">dbcolcreate</a></i>(1), <i><a href="/docs/linux/man/3-fsdb/">Fsdb</a></i>(3)</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
