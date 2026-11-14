---
title: "dbcolsregression(1)"
name: "dbcolsregression"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbcolsregression/"
description: "dbcolsregression – compute linear regression between two columns"
---

<h2 class="name">NAME</h2>
<p> dbcolsregression &#8211; compute linear regression between two columns </p>
<h2>SYNOPSIS</h2>
<pre>
    dbcolsregression  [-a] column1 column2
</pre>
<h2>DESCRIPTION</h2>
<p> Compute linear regression over <tt>&quot;column1&quot;</tt> and <tt>&quot;column2&quot;</tt>. Outputs slope, intercept, and correlation coefficient.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code> or <code>&#8211;include-non-numeric</code></p>
<dd> Compute stats over all records (treat non-numeric records as zero rather than just ignoring them).</p>
<dt><code>-f </code><font SIZE="-1"><code>FORMAT</code></font> or <code>&#8211;format </code><font SIZE="-1"><code>FORMAT</code></font></p>
<dd> Specify a <i><a href="/docs/linux/man/3-printf/">printf</a></i>(3)-style format for output statistics. Defaults to <tt>&quot;%.5g&quot;</tt>.</dl>
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
    #fsdb x     y
    160 126
    180 103
    200 82
    220 75
    240 82
    260 40
    280 20
</pre>
<h3>Command:</h3>
<pre>
    cat DATA/xy.fsdb | dbcolsregression x y | dblistize
</pre>
<h3>Output:</h3>
<pre>
    #fsdb -R C slope intercept confcoeff n
    slope:     -0.79286
    intercept: 249.86
    confcoeff: -0.95426
    n:         7
    #  | dbcolsregression x y
    #                confidence intervals assume normal distribution and small n.
    #  | dblistize
</pre>
<p> Sample data from &lt;<a rel="nofollow" href="http://people.hofstra.edu/faculty/Stefan_Waner/RealWorld/calctopic1/regression.html">http://people.hofstra.edu/faculty/Stefan_Waner/RealWorld/calctopic1/regression.html</a>&gt; by Stefan Waner and Steven R. Costenoble.</p>
<h2>SEE ALSO</h2>
<p> dbcolstats, dbcolscorrelate, Fsdb.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1997-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
