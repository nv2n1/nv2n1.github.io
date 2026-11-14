---
title: "dbcolscorrelate(1)"
name: "dbcolscorrelate"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbcolscorrelate/"
description: "dbcolscorrelate – find the coefficient of correlation over columns"
---

<h2 class="name">NAME</h2>
<p> dbcolscorrelate &#8211; find the coefficient of correlation over columns </p>
<h2>SYNOPSIS</h2>
<pre>
    dbcolscorrelate column1 column2 [column3...]
</pre>
<h2>DESCRIPTION</h2>
<p> Compute the coefficient of correlation over two (or more) columns. </p>
<p> The output is one line of correlations. </p>
<p> With exactly two columns, a new column <i>correlation</i> is created. </p>
<p> With more than two columns, correlations are computed for each pairwise combination of rows, and each output column is given a name which is the concatenation of the two source rows, joined with an underscore. </p>
<p> By default, we compute the <i>population correlation coefficient</i> (usually designed rho, X) and assume we see all members of the population. With the <code>&#8211;sample</code> option we instead compute the <i>sample correlation coefficient</i>, usually designated <i>r</i>. (Be careful in that the default here to full-population is the <i>opposite</i> of the default in dbcolstats.) </p>
<p> This program requires a complete copy of the input data on disk.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;sample</code></p>
<dd> Select a the Pearson product-moment correlation coefficient (the &#8220;sample correlation coefficient&#8221;, usually designated <i>r</i>).</p>
<dt><code>&#8211;nosample</code></p>
<dd> Select a the Pearson product-moment correlation coefficient (the &#8220;sample correlation coefficient&#8221;, usually designated <i>r</i>).</p>
<dt><code>-f </code><font SIZE="-1"><code>FORMAT</code></font> or <code>&#8211;format </code><font SIZE="-1"><code>FORMAT</code></font></p>
<dd> Specify a <i><a href="/docs/linux/man/3-printf/">printf</a></i>(3)-style format for output statistics. Defaults to <tt>&quot;%.5g&quot;</tt>.</p>
<dt><code>-T TmpDir</code></p>
<dd> where to put tmp files. Also uses environment variable <font SIZE="-1">TMPDIR,</font> if -T is not specified. Default is /tmp.</dl>
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
    #fsdb name id test1 test2
    a 1 80 81
    b 2 70 71
    c 3 65 66
    d 4 90 91
    e 5 70 71
    f 6 90 91
</pre>
<h3>Command:</h3>
<pre>
    cat DATA/more_grades.fsdb | dbcolscorrelate test1 test2
</pre>
<h3>Output:</h3>
<pre>
    #fsdb correlation
    0.83329
    #  | dbcolscorrelate test1 test2
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb, dbcolstatscores, dbcolsregression.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
