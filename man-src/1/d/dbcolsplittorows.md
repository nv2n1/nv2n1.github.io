---
title: "dbcolsplittorows(1)"
name: "dbcolsplittorows"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbcolsplittorows/"
description: "dbcolsplittorows – split an existing column into multiple new rows"
---

<h2 class="name">NAME</h2>
<p> dbcolsplittorows &#8211; split an existing column into multiple new rows </p>
<h2>SYNOPSIS</h2>
<p> dbcolsplittorows [-C ElementSeperator] [-e null] [-E] [-N enumerated-name] column [column&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Split column into pieces, outputting one row for each piece. </p>
<p> By default, any empty fields are ignored. If an empty field value is given with -e, then they produce output. </p>
<p> When a null value is given, empty fields at the beginning and end of lines are suppressed (like perl split). Unlike perl, if <font SIZE="-1">ALL</font> fields are empty, we generate one (and not zero) empty fields.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-C S</code> or <code>&#8211;element-separator S</code></p>
<dd> Specify the separator used to split columns. (Defaults to a single underscore.)</p>
<dt><code>-E</code> or <code>&#8211;enumerate</code></p>
<dd> Enumerate output columns: rather than assuming the column name uses the element separator, we keep it whole and fill in with indexes starting from 0.</p>
<dt><code>-N</code> or <code>&#8211;new-name</code> N</p>
<dd> Name the new column N for enumeration. Defaults to <tt>&quot;index&quot;</tt>.</p>
<dt><code>-e E</code> or <code>&#8211;empty E</code></p>
<dd> give value E as the value for empty (null) records</dl>
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
    #fsdb name uid
    John_Heidemann  2274
    Greg_Johnson    2275
    Root    0
    # this is a simple database
    #  | dbcol fullname uid
    #  | dbcolrename fullname name
</pre>
<h3>Command:</h3>
<pre>
    cat data.fsdb | dbcolsplittorows name
</pre>
<h3>Output:</h3>
<pre>
    #fsdb name uid
    John    2274
    Heidemann       2274
    Greg    2275
    Johnson 2275
    Root    0
    # this is a simple database
    #  | dbcol fullname uid
    #  | dbcolrename fullname name
    #  | dbcolsplittorows name
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-fsdb/">Fsdb</a></i>(1). <i><a href="/docs/linux/man/1-dbcolmerge/">dbcolmerge</a></i>(1). <i><a href="/docs/linux/man/1-dbcolsplittocols/">dbcolsplittocols</a></i>(1). <i><a href="/docs/linux/man/1-dbcolrename/">dbcolrename</a></i>(1).</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2008 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
