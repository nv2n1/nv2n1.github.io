---
title: "dbcolmovingstats(1)"
name: "dbcolmovingstats"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbcolmovingstats/"
description: "dbcolmovingstats – compute moving statistics over a window of a column of data"
---

<h2 class="name">NAME</h2>
<p> dbcolmovingstats &#8211; compute moving statistics over a window of a column of data </p>
<h2>SYNOPSIS</h2>
<p> dbcolmovingstats [-am] [-w window-width] [-e EmptyValue] column</p>
<h2>DESCRIPTION</h2>
<p> Compute moving statistics over a <font SIZE="-1">COLUMN</font> of data. Records containing non-numeric data are considered null do not contribute to the stats (optionally they are treated as zeros with <tt>&quot;-a&quot;</tt>). </p>
<p> Currently we compute mean and sample standard deviation. (Note we only compute sample standard deviation, not full population.) Optionally, with <tt>&quot;-m&quot;</tt> we also compute median. (Currently there is no support for generalized quantiles.) </p>
<p> Values before a sufficient number have been accumulated are given the empty value (if specified with <tt>&quot;-e&quot;</tt>). If no empty value is given, stats are computed on as many are possible if no empty value is specified. </p>
<p> Dbcolmovingstats runs in <a href="/docs/linux/man/1-o/">O</a>(1) memory, but must buffer a full window of data. Quantiles currently will repeatedly sort the window and so may perform poorly with wide windows.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code> or <code>&#8211;include-non-numeric</code></p>
<dd> Compute stats over all records (treat non-numeric records as zero rather than just ignoring them).</p>
<dt><code>-w</code> or <code>&#8211;window</code> <font SIZE="-1">WINDOW</font></p>
<dd> <font SIZE="-1">WINDOW</font> of how many items to accumulate (defaults to 10). (For compatibility with fsdb-1.x, <code>-n</code> is also supported.)</p>
<dt><code>-m</code> or <code>&#8211;median</code></p>
<dd> Show median of the window in addition to mean.</p>
<dt><code>-e E</code> or <code>&#8211;empty E</code></p>
<dd> Give value E as the value for empty (null) records. This null value is then output before a full window is accumulated.</p>
<dt><code>-f </code><font SIZE="-1"><code>FORMAT</code></font> or <code>&#8211;format </code><font SIZE="-1"><code>FORMAT</code></font></p>
<dd> Specify a <i><a href="/docs/linux/man/3-printf/">printf</a></i>(3)-style format for output mean and standard deviation. Defaults to <tt>&quot;%.5g&quot;</tt>.</dl>
<p> Eventually we expect to support other options of dbcolstats. </p>
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
    #fsdb date  epoch count
    19980201        886320000       6
    19980202        886406400       8
    19980203        886492800       19
    19980204        886579200       53
    19980205        886665600       20
    19980206        886752000       18
    19980207        886838400       5
    19980208        886924800       9
    19980209        887011200       22
    19980210        887097600       22
    19980211        887184000       36
    19980212        887270400       26
    19980213        887356800       23
    19980214        887443200       6
</pre>
<h3>Command:</h3>
<pre>
    cat data.fsdb | dbmovingstats -e - -w 4 count
</pre>
<h3>Output:</h3>
<pre>
        #fsdb date epoch count moving_mean moving_stddev
        19980201        886320000       6       -       -
        19980202        886406400       8       -       -
        19980203        886492800       19      -       -
        19980204        886579200       53      21.5    21.764
        19980205        886665600       20      25      19.442
        19980206        886752000       18      27.5    17.02
        19980207        886838400       5       24      20.445
        19980208        886924800       9       13      7.1647
        19980209        887011200       22      13.5    7.8528
        19980210        887097600       22      14.5    8.8129
        19980211        887184000       36      22.25   11.026
        19980212        887270400       26      26.5    6.6081
        19980213        887356800       23      26.75   6.3966
        19980214        887443200       6       22.75   12.473
        #   | dbcolmovingstats -e - -n 4 count
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb. dbcolstats. dbmultistats. dbrowdiff.</p>
<h2>BUGS</h2>
<p> Currently there is no support for generalized quantiles.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
