---
title: "dbmultistats(1)"
name: "dbmultistats"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbmultistats/"
description: "dbmultistats – run dbcolstats over each group of inputs identified by some key"
---

<h2 class="name">NAME</h2>
<p> dbmultistats &#8211; run dbcolstats over each group of inputs identified by some key </p>
<h2>SYNOPSIS</h2>
<p> <tt>$0</tt> [-dm] [-c ConfidencePercent] [-f FormatForm] [-q NumberOfQuartiles] -k KeyField ValueField</p>
<h2>DESCRIPTION</h2>
<p> The input table is grouped by KeyField, then we compute a separate set of column statistics on ValueField for each group with a unique key. </p>
<p> Assumptions and requirements are the same as dbmapreduce (this program is just a wrapper around that program): </p>
<p> By default, data can be provided in arbitrary order and the program consumes O(number of unique tags) memory, and O(size of data) disk space. </p>
<p> With the -S option, data must arrive group by tags (not necessarily sorted), and the program consumes O(number of tags) memory and no disk space. The program will check and abort if this precondition is not met. </p>
<p> With two -S&#8217;s, program consumes <a href="/docs/linux/man/1-o/">O</a>(1) memory, but doesn&#8217;t verify that the data-arrival precondition is met. </p>
<p> (Note that these semantics are exactly like<br />
&nbsp;<wbr>dbmapreduce -k KeyField &#8212; dbcolstats ValueField dbmultistats provides a simpler <font SIZE="-1">API</font> that passes through statistics-specific arguments and is optimized when data is pre-sorted and there are no quarties or medians.)</p>
<h2>OPTIONS</h2>
<p> Options are the same as dbcolstats.</p>
<dl>
<dt><code>-k</code> or <code>&#8211;key</code> KeyField</p>
<dd> specify which column is the key for grouping (default: the first column)</p>
<dt><code>-a</code> or <code>&#8211;include-non-numeric</code></p>
<dd> Compute stats over all records (treat non-numeric records as zero rather than just ignoring them).</p>
<dt><code>-c </code><font SIZE="-1"><code>FRACTION</code></font> or <code>&#8211;confidence </code><font SIZE="-1"><code>FRACTION</code></font></p>
<dd> Specify <font SIZE="-1">FRACTION</font> for the confidence interval. Defaults to 0.95 for a 95% confidence factor.</p>
<dt><code>-f </code><font SIZE="-1"><code>FORMAT</code></font> or <code>&#8211;format </code><font SIZE="-1"><code>FORMAT</code></font></p>
<dd> Specify a <i><a href="/docs/linux/man/3-printf/">printf</a></i>(3)-style format for output statistics. Defaults to <tt>&quot;%.5g&quot;</tt>.</p>
<dt><code>-m</code> or <code>&#8211;median</code></p>
<dd> Compute median value. (Will sort data if necessary.) (Median is the quantitle for N=2.)</p>
<dt><code>-q N</code> or <code>&#8211;quantile N</code></p>
<dd> Compute quantile (quartile when N is 4), or an arbitrary quantile for other values of N, where the scores that are 1 Nth of the way across the population.</p>
<dt><code>-S</code> or <code>&#8211;pre-sorted</code></p>
<dd> Assume data is already sorted. With one -S, we check and confirm this precondition. When repeated, we skip the check.</p>
<dt>&lt;-T TmpDir&gt;</p>
<dd> where to put temporary data. Only used if median or quantiles are requested. Also uses environment variable <font SIZE="-1">TMPDIR,</font> if -T is not specified. Default is /tmp.</p>
<dt>&lt;&#8211;parallelism=N&gt;</p>
<dd> Allow up to N reducers to run in parallel. Default is the number of CPUs in the machine.</dl>
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
    #fsdb experiment duration
    ufs_mab_sys 37.2
    ufs_mab_sys 37.3
    ufs_rcp_real 264.5
    ufs_rcp_real 277.9
</pre>
<h3>Command:</h3>
<pre>
    cat DATA/stats.fsdb | dbmultistats -k experiment duration
</pre>
<h3>Output:</h3>
<pre>
    #fsdb      experiment      mean    stddev  pct_rsd conf_range      conf_low       conf_high        conf_pct        sum     sum_squared     min     max     n
    ufs_mab_sys     37.25 0.070711 0.18983 0.6353 36.615 37.885 0.95 74.5 2775.1 37.2 37.3 2
    ufs_rcp_real    271.2 9.4752 3.4938 85.13 186.07 356.33 0.95 542.4 1.4719e+05 264.5 277.9 2
    #  | /home/johnh/BIN/DB/dbmultistats experiment duration
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb. dbmapreduce. dbcolstats.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
