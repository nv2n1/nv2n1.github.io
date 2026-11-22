---

title: "dbcolstats(1)"
name: "dbcolstats"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbcolstats/"
description: "dbcolstats – compute statistics on a fsdb column"
---

<p> dbcolstats &#8211; compute statistics on a fsdb column </p>
<h2>SYNOPSIS</h2>
<p> dbcolstats [-amS] [-c ConfidenceFraction] [-q NumberOfQuantiles] column</p>
<h2>DESCRIPTION</h2>
<p> Compute statistics over a COLUMN of data. Records containing non-numeric data are considered null do not contribute to the stats (with the <tt>&quot;-a&quot;</tt> option they are treated as zeros). </p>
<p> Confidence intervals are a t-test (+/- (t_{a/2})*s/sqrt(n)) and assume the population takes a normal distribution with a small number of samples (&lt; 100). </p>
<p> By default, all statistics are computed for as a population <i>sample</i> (with an &#8220;n-1&#8221; term), not as representing the whole population (using &#8220;n&#8221;). Select between them with <code>&#8211;sample</code> or <code>&#8211;nosample</code>. When you measure the entire population, use the latter option. </p>
<p> The output of this program is probably best looked at after reformatting with dblistize. </p>
<p> Dbcolstats runs in O(1) memory. Median or quantile requires sorting the data and invokes dbsort. Sorting will run in constant RAM but O(number of records) disk space. If median or quantile is required and the data is already sorted, dbcolstats will run more efficiently with the -S option.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code> or <code>&#8211;include-non-numeric</code></dt>
<dd> Compute stats over all records (treat non-numeric records as zero rather than just ignoring them).</dd>
<dt><code>-c </code><code>FRACTION</code> or <code>&#8211;confidence </code><code>FRACTION</code></dt>
<dd> Specify FRACTION for the confidence interval. Defaults to 0.95 for a 95% confidence factor.</dd>
<dt><code>-f </code><code>FORMAT</code> or <code>&#8211;format </code><code>FORMAT</code></dt>
<dd> Specify a <i><a href="/docs/linux/man/3-printf/">printf</a></i>(3)-style format for output statistics. Defaults to <tt>&quot;%.5g&quot;</tt>.</dd>
<dt><code>-m</code> or <code>&#8211;median</code></dt>
<dd> Compute median value. (Will sort data if necessary.) (Median is the quantitle for N=2.)</dd>
<dt><code>-q N</code> or <code>&#8211;quantile N</code></dt>
<dd> Compute quantile (quartile when N is 4), or an arbitrary quantile for other values of N, where the scores that are 1 Nth of the way across the population.</dd>
<dt><code>&#8211;sample</code></dt>
<dd> Compute <i>sample</i> population statistics (e.g., the sample standard deviation), assuming <i>n-1</i> degrees of freedom.</dd>
<dt><code>&#8211;nosample</code></dt>
<dd> Compute <i>whole</i> population statistics (e.g., the population standard devation).</dd>
<dt><code>-S</code> or <code>&#8211;pre-sorted</code></dt>
<dd> Assume data is already sorted. With one -S, we check and confirm this precondition. When repeated, we skip the check.</dd>
<dt>&lt;&#8211;parallelism=N&gt;</dt>
<dd> Allow sorting to happen in parallel. Defaults on. (Only relevant if using non-pre-sorted data with quantiles.)</dd>
<dt><code>-F</code> or <code>&#8211;fs</code> or <code>&#8211;fieldseparator</code> S</dt>
<dd> Specify the field (column) separator as <tt>&quot;S&quot;</tt>. See dbfilealter for valid field separators.</dd>
<dt><code>-T TmpDir</code></dt>
<dd> where to put temporary data. Only used if median or quantiles are requested. Also uses environment variable TMPDIR, if -T is not specified. Default is /tmp.</dd>
<dt><code>-k KeyField</code></dt>
<dd> Do multi-stats, grouped by each key. Assumes keys are sorted. (Use dbmultistats to guarantee sorting order.)</dd></dl>
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
    #fsdb      absdiff
    0
    0.046953
    0.072074
    0.075413
    0.094088
    0.096602
    #  | /home/johnh/BIN/DB/dbrow 
    #  | /home/johnh/BIN/DB/dbcol event clock
    #  | dbrowdiff clock
    #  | /home/johnh/BIN/DB/dbcol absdiff
</pre>
<h3>Command:</h3>
<pre>
    cat data.fsdb | dbcolstats absdiff
</pre>
<h3>Output:</h3>
<pre>
    #fsdb mean stddev pct_rsd conf_range conf_low conf_high conf_pct sum sum_squared min max n
    0.064188        0.036194        56.387  0.037989        0.026199        0.102180.95     0.38513 0.031271        0       0.096602        6
    #  | /home/johnh/BIN/DB/dbrow 
    #  | /home/johnh/BIN/DB/dbcol event clock
    #  | dbrowdiff clock
    #  | /home/johnh/BIN/DB/dbcol absdiff
    #  | dbcolstats absdiff
    #               0.95 confidence intervals assume normal distribution and small n.
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-dbmultistats/">dbmultistats</a></i>(1), handles multiple experiments in a single file. </p>
<p> <i><a href="/docs/linux/man/1-dblistize/">dblistize</a></i>(1), to pretty-print the output of dbcolstats. </p>
<p> <i><a href="/docs/linux/man/1-dbcolpercentile/">dbcolpercentile</a></i>(1), to compute an even more general version of median/quantiles. </p>
<p> <i><a href="/docs/linux/man/1-dbcolstatscores/">dbcolstatscores</a></i>(1), to compute z-scores or t-scores for each row </p>
<p> <i><a href="/docs/linux/man/1-dbrvstatdiff/">dbrvstatdiff</a></i>(1), to see if two sample populations are statistically different. </p>
<p> Fsdb.</p>
<h2>BUGS</h2>
<p> The algorithms used to compute variance have not been audited to check for numerical stability. (See <i><a rel="nofollow" href="http://en.wikipedia.org/wiki/Algorithms_for_calculating_variance">http://en.wikipedia.org/wiki/Algorithms_for_calculating_variance</a></i>).) Variance may be incorrect when standard deviation is small relative to the mean. </p>
<p> The field <tt>&quot;conf_pct&quot;</tt> implies percentage, but it&#8217;s actually reported as a fraction (0.95 means 95%). </p>
<p> Because of limits of floating point, statistics on numbers of widely different scales may be incorrect. See the test cases <i>dbcolstats_extrema</i> for examples.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the GNU general public license, version 2. See the file COPYING with the distribution for details. </p>
