---
title: "dbrowuniq(1)"
name: "dbrowuniq"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbrowuniq/"
description: "dbrowuniq – eliminate adjacent rows with duplicate fields, maybe counting"
---

<h2 class="name">NAME</h2>
<p> dbrowuniq &#8211; eliminate adjacent rows with duplicate fields, maybe counting </p>
<h2>SYNOPSIS</h2>
<p> dbrowuniq [-cFLB] [uniquifying fields&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Eliminate adjacent rows with duplicate fields, perhaps counting them. Roughly equivalent to the Unix uniq command, but optionally only operating on the specified fields. </p>
<p> By default, <i>all</i> columns must be unique. If column names are specified, only those columns must be unique and the first row with those columns is returned. </p>
<p> Dbrowuniq eliminates only identical rows that <i>adjacent</i>. If you want to eliminate identical rows across the entirefile, you must make them adajcent, perhaps by using dbsort on your uniquifying field. (That is, the input with three lines a/b/a will produce three lines of output with both a&#8217;s, but if you dbsort it, it will become a/a/b and dbrowuniq will output a/b. </p>
<p> By default, dbrowuniq outputs the <i>first</i> unique row. Optionally, with <tt>&quot;-L&quot;</tt>, it will output the <i>last</i> unique row, or with <tt>&quot;-B&quot;</tt> it outputs both first and last. (This choice only matters when uniqueness is determined by specific fields.) </p>
<p> dbrowuniq can also count how many unique, adjacent lines it finds with <tt>&quot;-c&quot;</tt>, with the count going to a new column (defaulting to <tt>&quot;count&quot;</tt>). Incremental counting, when the <tt>&quot;count&quot;</tt> column already exists, is possible with <tt>&quot;-I&quot;</tt>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> or <code>&#8211;count</code></p>
<dd> Create a new column (count) which counts the number of times each line occurred. </p>
<p> The new column is named by the <tt>&quot;-N&quot;</tt> argument, defaulting to <tt>&quot;count&quot;</tt>.</p>
<dt><code>-N</code> on <code>&#8211;new-name</code></p>
<dd> Specify the name of the count column, if any. (Default is <tt>&quot;count&quot;</tt>.)</p>
<dt><code>-I</code> on <code>&#8211;incremental</code></p>
<dd> Incremental counting. If the count column exists, it is assumed to have a partial count and the count accumulates. If the count column doesn&#8217;t exist, it is created.</p>
<dt><code>-L</code> or <code>&#8211;last</code></p>
<dd> Output the last unique row. By default, it outputs the first unique row.</p>
<dt><code>-F</code> or <code>&#8211;first</code></p>
<dd> Output the first unique row. (This is the default.)</p>
<dt><code>-B</code> or <code>&#8211;both</code></p>
<dd> Output both the first and last unique rows.</dl>
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
<dt><code>&#8211;header</code> H</p>
<dd> Use H as the full Fsdb header, rather than reading a header from then input.</p>
<dt><code>&#8211;help</code></p>
<dd> Show help.</p>
<dt><code>&#8211;man</code></p>
<dd> Show full manual.</dl>
<h2>SAMPLE USAGE</h2>
<h3>Input:</h3>
<pre>
    #fsdb      event
    _null_getpage+128
    _null_getpage+128
    _null_getpage+128
    _null_getpage+128
    _null_getpage+128
    _null_getpage+128
    _null_getpage+4
    _null_getpage+4
    _null_getpage+4
    _null_getpage+4
    _null_getpage+4
    _null_getpage+4
    #  | /home/johnh/BIN/DB/dbcol event
    #  | /home/johnh/BIN/DB/dbsort event
</pre>
<h3>Command:</h3>
<pre>
    cat data.fsdb | dbrowuniq -c
</pre>
<h3>Output:</h3>
<pre>
    #fsdb       event   count
    _null_getpage+128   6
    _null_getpage+4     6
    #   2       /home/johnh/BIN/DB/dbcol        event
    #  | /home/johnh/BIN/DB/dbrowuniq -c
</pre>
<h2>SAMPLE USAGE 2</h2>
<p> Retaining the last unique row as an example.</p>
<h3>Input:</h3>
<pre>
        #fsdb event i
        _null_getpage+128 10
        _null_getpage+128 11
        _null_getpage+128 12
        _null_getpage+128 13
        _null_getpage+128 14
        _null_getpage+128 15
        _null_getpage+4 16
        _null_getpage+4 17
        _null_getpage+4 18
        _null_getpage+4 19
        _null_getpage+4 20
        _null_getpage+4 21
        #  | /home/johnh/BIN/DB/dbcol event
        #  | /home/johnh/BIN/DB/dbsort event
</pre>
<h3>Command:</h3>
<pre>
    cat data.fsdb | dbrowuniq -c -L event
</pre>
<h3>Output:</h3>
<pre>
        #fsdb event i count
        _null_getpage+128       15      6
        #  | /home/johnh/BIN/DB/dbcol event
        #  | /home/johnh/BIN/DB/dbsort event
        _null_getpage+4 21      6
        #   | dbrowuniq -c
</pre>
<h2>SAMPLE USAGE 3</h2>
<p> Incremental counting.</p>
<h3>Input:</h3>
<pre>
    #fsdb       event   count
    _null_getpage+128   6
    _null_getpage+128   6
    _null_getpage+4     6
    _null_getpage+4     6
    #  /home/johnh/BIN/DB/dbcol event
    #  | /home/johnh/BIN/DB/dbrowuniq -c
</pre>
<h3>Command:</h3>
<pre>
    cat data.fsdb | dbrowuniq -I -c event
</pre>
<h3>Output:</h3>
<pre>
        #fsdb event count
        _null_getpage+128   12
        _null_getpage+4     12
        #  /home/johnh/BIN/DB/dbcol     event
        #  | /home/johnh/BIN/DB/dbrowuniq -c
        #   | dbrowuniq -I -c event
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1997-2016 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
