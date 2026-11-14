---
title: "dbcolmerge(1)"
name: "dbcolmerge"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbcolmerge/"
description: "dbcolmerge – merge multiple columns into one"
---

<h2 class="name">NAME</h2>
<p> dbcolmerge &#8211; merge multiple columns into one </p>
<h2>SYNOPSIS</h2>
<p> dbcolmerge [-C ElementSeparator] [columns&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> For each row, merge multiple columns down to a single column, joining elements with ElementSeparator (defaults to a single underscore).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-C S</code> or <code>&#8211;element-separator S</code></p>
<dd> Specify the separator used to join columns. (Defaults to a single underscore.)</p>
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
    #fsdb      first   last
    John    Heidemann
    Greg    Johnson
    Root    -
    # this is a simple database
    #  | /home/johnh/BIN/DB/dbcol fullname
    #  | dbcolrename fullname first_last
    #  | /home/johnh/BIN/DB/dbcolsplit -C _ first_last
    #  | /home/johnh/BIN/DB/dbcol first last
</pre>
<h3>Command:</h3>
<pre>
    cat data.fsdb | dbcolmerge -C _ first last
</pre>
<h3>Output:</h3>
<pre>
    #fsdb      first   last    first_last
    John    Heidemann       John_Heidemann
    Greg    Johnson Greg_Johnson
    Root    -        Root_
    # this is a simple database
    #  | /home/johnh/BIN/DB/dbcol fullname
    #  | dbcolrename fullname first_last
    #  | /home/johnh/BIN/DB/dbcolsplit first_last
    #  | /home/johnh/BIN/DB/dbcol first last
    #  | /home/johnh/BIN/DB/dbcolmerge -C _ first last
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb. dbcolsplittocols. dbcolsplittorows. dbcolrename.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2008 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
