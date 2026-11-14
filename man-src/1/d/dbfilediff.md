---
title: "dbfilediff(1)"
name: "dbfilediff"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbfilediff/"
description: "dbfilediff – compare two fsdb tables"
---

<h2 class="name">NAME</h2>
<p> dbfilediff &#8211; compare two fsdb tables </p>
<h2>SYNOPSIS</h2>
<pre><code>
dbfilediff[-Eq][-N diff_column_name]-- input table1.fsdb-- input table2.fsdb
</code></pre>
<p> <font SIZE="-1">OR</font> </p>
<pre>
    cat table1.fsdb  | dbfilediff [-sq] --input table2.fsdb
</pre>
<h2>DESCRIPTION</h2>
<p> Dbfilediff compares two Fsdb tables, row by row. Unlike Unix <i><a href="/docs/linux/man/1-diff/">diff</a></i>(1), this program assumes the files are identical line-by-line and we compare fields. Thus, insertion of one extra row will result in all subsequent lines being marked different. </p>
<p> By default, <i>all</i> columns must be unique. (At some point, support to specific specific columns may be added.) </p>
<p> Output is a new table with a new column <tt>&quot;diff&quot;</tt> (or something else if the <tt>&quot;-N&quot;</tt> option is given), &#8220;-&#8221; and &#8220;+&#8221; for the first and second non-equal rows, &#8220;=&#8221; for matching lines, or &#8220;~&#8221; if they are equal with epsilon numerics (in which case only the second row is included). Unlike Unix <i><a href="/docs/linux/man/1-diff/">diff</a></i>(1), we output <i>all</i> rows (the &#8220;=&#8221; lines), not just diffs (the <tt>&quot;--quiet&quot;</tt> option suppresses this output). </p>
<p> Optionally, with <tt>&quot;-E&quot;</tt> it will do a &#8220;epsilon numeric&#8221; comparision, to account for things like variations in different computer&#8217;s floating point precision and differences in printf output. </p>
<p> Epsilon comparision is asymmetric, in that it assumes the first input is correct an allows the second input to vary, but not the reverse. </p>
<p> Because two tables are required, input is typically in files. Standard input is accessible by the file &#8220;-&#8221;.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-E</code> or <code>&#8211;epsilon</code></p>
<dd> Do epsilon-numeric comparison. (Described above.) </p>
<p> Epsilon-comparision is only done on columns that look like floating point numbers, not on strings or integers. Epsilon comparision allows the last digit to vary by 1, or for there to be one extra digit of precision, but only for floating point numbers. </p>
<p> Rows that are within epsilon are not considered different for purposes of the exit code.</p>
<dt><code>&#8211;exit</code></p>
<dd> Exit with a status of 1 if some differences were found. (By default, the exit status is 0 with or without differences if the file is processed successfully.)</p>
<dt><code>-N</code> on <code>&#8211;new-name</code></p>
<dd> Specify the name of the <tt>&quot;diff&quot;</tt> column, if any. (Default is <tt>&quot;diff&quot;</tt>.)</p>
<dt><code>-q</code> or <code>&#8211;quiet</code></p>
<dd> Be quiet, suppressing output for identical rows. (This behavior is different from Unix <i><a href="/docs/linux/man/1-diff/">diff</a></i>(1) where <tt>&quot;-q&quot;</tt> suppresses <i>all</i> output.) If repeated, omits epsilon-equivalent rows.</dl>
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
    #fsdb event clock absdiff pctdiff
    _null_getpage+128   815812813.281756        0       0
    _null_getpage+128   815812813.328709        0.046953        5.7554e-09
    _null_getpage+128   815812813.353830        0.025121        3.0793e-09
    _null_getpage+128   815812813.357169        0.0033391       4.0929e-10
</pre>
<p> And in the file <i>TEST/dbfilediff_ex.in-2</i>: </p>
<pre>
    #fsdb event clock absdiff pctdiff
    _null_getpage+128   815812813.281756        0       0
    _null_getpage+128   815812813.328709        0.046953        5.7554e-09
    _null_getpage+128   815812813.353830        0.025121        3.0793e-09
    _null_getpage+128   815812813.357169        0.003339        4.0929e-10
</pre>
<h3>Command:</h3>
<pre>
    cat TEST/dbfilediff_ex.in | dbfilediff -i - -i TEST/dbfilediff_ex.in-2
</pre>
<h3>Output:</h3>
<pre>
    #fsdb event clock absdiff pctdiff diff
    _null_getpage+128   815812813.281756        0       0       =
    _null_getpage+128   815812813.328709        0.046953        5.7554e-09      =
    _null_getpage+128   815812813.353830        0.025121        3.0793e-09      =
    _null_getpage+128   815812813.357169        0.0033391       4.0929e-10      -
    _null_getpage+128   815812813.357169        0.003339        4.0929e-10      +
    #   | dbfilediff --input TEST/dbfilediff_ex.in-2
</pre>
<p> By comparision, if one adds the <tt>&quot;-s&quot;</tt> option, then all rows will pass as equal.</p>
<h2>SEE ALSO</h2>
<p> Fsdb. dbrowuniq. dbfilediff. </p>
<p> dbrowdiff, dbrowuniq, and dbfilediff are similar but different. dbrowdiff computes row-by-row differences for a column, dbrowuniq eliminates rows that have no differences, and dbfilediff compares fields of two files.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 2012-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
