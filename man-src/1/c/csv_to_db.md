---
title: "csv_to_db(1)"
name: "csv_to_db"
section: "1"
letter: "c"
url: "/docs/linux/man/1-csv_to_db/"
description: "csv_to_db – convert comma-separated-value data into fsdb"
---

<h2 class="name">NAME</h2>
<p> csv_to_db &#8211; convert comma-separated-value data into fsdb </p>
<h2>SYNOPSIS</h2>
<pre>
    csv_to_db &lt;source.csv
</pre>
<h2>DESCRIPTION</h2>
<p> Converts a comma-separated-value data stream to Fsdb format. </p>
<p> The input is CSV-format (<i>not</i> fsdb). The first row is taken to be the names of the columns. </p>
<p> The output is two-space-separated fsdb. (Someday more general field separators should be supported.) Fsdb fields are normalized version of the <font SIZE="-1">CSV</font> file: spaces are converted to single underscores. </p>
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
    paper,papertitle,reviewer,reviewername,score1,score2,score3,score4,score5
    1,&quot;test, paper&quot;,2,Smith,4,4,,,
    2,other paper,3,Jones,3,3,,,
</pre>
<h3>Command:</h3>
<pre>
    csv_to_db
</pre>
<h3>Output:</h3>
<pre>
    #fsdb -F S paper papertitle reviewer reviewername score1 score2 score3 score4 score5
    1  test, paper  2  Smith  4  4  -  -  -
    2  other paper  3  Jones  3  3  -  -  -
    #  | csv_to_db
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb. db_to_csv.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2008 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
