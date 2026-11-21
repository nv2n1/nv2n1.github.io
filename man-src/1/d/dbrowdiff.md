---

title: "dbrowdiff(1)"
name: "dbrowdiff"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbrowdiff/"
description: "dbrowdiff – compute row-by-row differences of some column"
---

<p> dbrowdiff [-B|-I] column</p>
<p> For a given column, compute the differences between each row of the table. Differences are output to two new columns, <tt>&quot;absdiff&quot;</tt> and <tt>&quot;pctdiff&quot;</tt>. </p>
<p> Differences are either relative to the previous column (<i>incremental</i> mode), or relative to the first row (<i>baseline</i> mode), the default.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-B</code> or <code>&#8211;baseline</code></dt>
<dd> Select baseline mode (the default), where differences are relative to the first row.</dd>
<dt><code>-I</code> or <code>&#8211;incremental</code></dt>
<dd> Select incremental mode, where differences are relative to the previous row.</dd>
<dt><code>-f </code><font SIZE="-1"><code>FORMAT</code></font> or <code>&#8211;format </code><font SIZE="-1"><code>FORMAT</code></font></dt>
<dd> Specify a <i><a href="/docs/linux/man/3-printf/">printf</a></i>(3)-style format for output statistics. Defaults to <tt>&quot;%.5g&quot;</tt>.</dd></dl>
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
    #fsdb      event   clock
    _null_getpage+128       815812813.281756
    _null_getpage+128       815812813.328709
    _null_getpage+128       815812813.353830
    _null_getpage+128       815812813.357169
    _null_getpage+128       815812813.375844
    _null_getpage+128       815812813.378358
    #  | /home/johnh/BIN/DB/dbrow 
    #  | /home/johnh/BIN/DB/dbcol event clock
</pre>
<h3>Command:</h3>
<pre>
    cat DATA/kitrace.fsdb | dbrowdiff clock
</pre>
<h3>Output:</h3>
<pre>
    #fsdb      event   clock   absdiff pctdiff
    _null_getpage+128       815812813.281756        0       0
    _null_getpage+128       815812813.328709        0.046953        5.7554e-09
    _null_getpage+128       815812813.353830        0.072074        8.8346e-09
    _null_getpage+128       815812813.357169        0.075413        9.2439e-09
    _null_getpage+128       815812813.375844        0.094088        1.1533e-08
    _null_getpage+128       815812813.378358        0.096602        1.1841e-08
    #  | /home/johnh/BIN/DB/dbrow 
    #  | /home/johnh/BIN/DB/dbcol event clock
    #  | dbrowdiff clock
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb. dbcolmovingstats. dbrowuniq. dbfilediff. </p>
<p> dbrowdiff, dbrowuniq, and dbfilediff are similar but different. dbrowdiff computes row-by-row differences for a column, dbrowuniq eliminates rows that have no differences, and dbfilediff compares fields of two files.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2008 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
