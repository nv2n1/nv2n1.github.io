---
title: "dbcolstatscores(1)"
name: "dbcolstatscores"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbcolstatscores/"
description: "dbcolstatscores – compute z-scores or t-scores for each value in a population"
---

<h2 class="name">NAME</h2>
<p> dbcolstatscores &#8211; compute z-scores or t-scores for each value in a population </p>
<h2>SYNOPSIS</h2>
<p> dbcolstatscores [-t] [&#8211;tmean=MEAN] [&#8211;tstddev=STDDEV] column</p>
<h2>DESCRIPTION</h2>
<p> Compute statistics (z-score and optionally t-score) over a <font SIZE="-1">COLUMN</font> of numbers. Creates new columns called &#8220;zscore&#8221;, &#8220;tscore&#8221;. T-scores are only computed if requested with the <tt>&quot;-t&quot;</tt> option, or if <tt>&quot;--tmean&quot;</tt> or <tt>&quot;--tstddev&quot;</tt> are explicitly specified (defaults are mean of 50, standard deviation of 10). </p>
<p> You may recall from your statistics class that a z-score is simply the value normalized by mean and standard deviation, so that 0.0 is the mean and positive or negative values are multiples of the standard deviation. It assumes data follows a normal (Gaussian) distribution. </p>
<p> T-score scales the z-score to match a mean of 50 and a standard deviation of 10. This program allows generalized t-scores that use any mean and standard deviation. </p>
<p> Other scales are sometimes used as well. The Wechsler Adult Intelligence Scale (one type of <font SIZE="-1">IQ</font> test) is adjusted to a mean of 100 and a standard deviation of 15. Other tests scale to other standard deviations. </p>
<p> This program requires two passes over the data, and consumes <a href="/docs/linux/man/1-o/">O</a>(1) memory and O(number of rows) disk space.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code> or <code>&#8211;include-non-numeric</code></p>
<dd> Compute stats over all records (treat non-numeric records as zero rather than just ignoring them).</p>
<dt><code>-t</code></p>
<dd> Compute t-scores in addition to z-scores.</p>
<dt><code>&#8211;tmean </code><font SIZE="-1"><code>MEAN</code></font></p>
<dd> Use the given <font SIZE="-1">MEAN</font> for t-scores.</p>
<dt><code>&#8211;tstddev </code><font SIZE="-1"><code>STDDEV</code></font> or <code>&#8211;tsd </code><font SIZE="-1"><code>STDDEV</code></font></p>
<dd> Use the given <font SIZE="-1">STDDEV</font> for the standard deviation of the t-scores.</p>
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
    #fsdb name id test1
    a 1 80
    b 2 70
    c 3 65
    d 4 90
    e 5 70
    f 6 90
</pre>
<h3>Command:</h3>
<pre>
    cat DATA/grades.fsdb | dbcolstatscores --tmean 50 --tstddev 10 test1 | dbcolneaten
</pre>
<h3>Output:</h3>
<pre>
    #fsdb name id test1 zscore   tscore 
    a       1  80    0.23063  52.306 
    b       2  70    -0.69188 43.081 
    c       3  65    -1.1531  38.469 
    d       4  90    1.1531   61.531 
    e       5  70    -0.69188 43.081 
    f       6  90    1.1531   61.531 
    #  | dbcolstatscores --tmean 50 --tstddev 10 test1
    #  | dbcolneaten
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-dbcolpercentile/">dbcolpercentile</a></i>(1), <i><a href="/docs/linux/man/1-dbcolstats/">dbcolstats</a></i>(1), Fsdb, dbcolscorrelate</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2007 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
