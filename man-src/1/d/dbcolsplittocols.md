---
title: "dbcolsplittocols(1)"
name: "dbcolsplittocols"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbcolsplittocols/"
description: "dbcolsplittocols – split an existing column into multiple new columns"
---

<h2 class="name">NAME</h2>
<p> dbcolsplittocols &#8211; split an existing column into multiple new columns </p>
<h2>SYNOPSIS</h2>
<p> dbcolsplittocols [-E] [-C ElementSeparator] column [column&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Create new columns by splitting an existing column. The fragments of the column are each divided by ElementSeparator (default is underscore). </p>
<p> This command is the opposite of dbcolmerge. Names of the new columns are given by splitting the name of the existing column. dbcolrename may be useful to set column names.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-C S</code> or <code>&#8211;element-separator S</code></p>
<dd> Specify the separator <i>S</i> used to join columns. (Defaults to a single underscore.)</p>
<dt><code>-E</code> or <code>&#8211;enumerate</code></p>
<dd> Enumerate output columns: rather than assuming the column name uses the element separator, we keep it whole and fill in with indexes starting from 0. (Not currently implemented, but planned. See dbcolsplittorows.)</dl>
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
    #fsdb      first_last
    John_Heidemann
    Greg_Johnson
    Root
    # this is a simple database
    #  | dbcolrename fullname first_last
    #  | /home/johnh/BIN/DB/dbcol first_last
</pre>
<h3>Command:</h3>
<pre>
    cat data.fsdb | dbcolsplittocols first_last
</pre>
<h3>Output:</h3>
<pre>
    #fsdb      first_last      first   last
    John_Heidemann  John    Heidemann
    Greg_Johnson    Greg    Johnson
    Root    Root
    # this is a simple database
    #  | dbcolrename fullname first_last
    #  | /home/johnh/BIN/DB/dbcol first_last
    #  | /home/johnh/BIN/DB/dbcolsplittocols first_last
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-fsdb/">Fsdb</a></i>(3). <i><a href="/docs/linux/man/1-dbcolmerge/">dbcolmerge</a></i>(1). <i><a href="/docs/linux/man/1-dbcolsplittorows/">dbcolsplittorows</a></i>(1). <i><a href="/docs/linux/man/1-dbcolrename/">dbcolrename</a></i>(1).</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
