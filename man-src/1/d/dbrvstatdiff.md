---
title: "dbrvstatdiff(1)"
name: "dbrvstatdiff"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbrvstatdiff/"
description: "dbrvstatdiff – evaluate statistical differences between two random variables"
---

<h2 class="name">NAME</h2>
<p> dbrvstatdiff &#8211; evaluate statistical differences between two random variables </p>
<h2>SYNOPSIS</h2>
<pre><code>
dbrvstatdiff[-f format][-c ConfRating]
            [-h HypothesizedDifference] m1c sd1c n1c m2c sd2c n2c
</code></pre>
<p> <font SIZE="-1">OR</font> </p>
<pre><code>
dbrvstatdiff[-f format][-c ConfRating] m1c n1c m2c n2c
</code></pre>
<h2>DESCRIPTION</h2>
<p> Produce statistics on the difference of sets of random variables. If a hypothesized difference is given (with <tt>&quot;-h&quot;</tt>), to does a Student&#8217;s t-test. </p>
<p> Random variables are specified by:</p>
<dl>
<dt>&quot;m1c&quot;, &quot;m2c&quot;</p>
<dd> The column names of means of random variables.</p>
<dt>&quot;sd1c&quot;, &quot;sd2c&quot;</p>
<dd> The column names of standard deviations of random variables.</p>
<dt>&quot;n1c&quot;, &quot;n2c&quot;</p>
<dd> Counts of number of samples for each random variable</dl>
<p> These values can be computed with dbcolstats. </p>
<p> Creates up to ten new columns:</p>
<dl>
<dt>&quot;diff&quot;</p>
<dd> The difference of <font SIZE="-1">RV 2 &#8211; RV 1.</font></p>
<dt>&quot;diff_pct&quot;</p>
<dd> The percentage difference (<font SIZE="-1">RV2-RV1</font>)/1</p>
<dt>&quot;diff_conf_{half,low,high}&quot; and &quot;diff_conf_pct_{half,low,high}&quot;</p>
<dd> The half half confidence intervals and low and high values for absolute and relative confidence.</p>
<dt>&quot;t_test&quot;</p>
<dd> The T-test value for the given hypothesized difference.</p>
<dt>&quot;t_test_result&quot;</p>
<dd> Given the confidence rating, does the test pass? Will be either &#8220;rejected&#8221; or &#8220;not-rejected&#8221;.</p>
<dt>&quot;t_test_break&quot;</p>
<dd> The hypothesized value that is break-even point for the T-test.</p>
<dt>&quot;t_test_break_pct&quot;</p>
<dd> Break-even point as a percent of m1c.</dl>
<p> Confidence intervals are not printed if standard deviations are not provided. Confidence intervals assume normal distributions with common variances. </p>
<p> T-tests are only computed if a hypothesized difference is provided. Hypothesized differences should be proceeded by &lt;=, &gt;=, =. T-tests assume normal distributions with common variances.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c </code><font SIZE="-1"><code>FRACTION</code></font> or <code>&#8211;confidence </code><font SIZE="-1"><code>FRACTION</code></font></p>
<dd> Specify <font SIZE="-1">FRACTION</font> for the confidence interval. Defaults to 0.95 for a 95% confidence factor (alpha = 0.05).</p>
<dt><code>-f </code><font SIZE="-1"><code>FORMAT</code></font> or <code>&#8211;format </code><font SIZE="-1"><code>FORMAT</code></font></p>
<dd> Specify a <i><a href="/docs/linux/man/3-printf/">printf</a></i>(3)-style format for output statistics. Defaults to <tt>&quot;%.5g&quot;</tt>.</p>
<dt><code>-h </code><font SIZE="-1"><code>DIFF</code></font> or <code>&#8211;hypothesis </code><font SIZE="-1"><code>DIFF</code></font></p>
<dd> Specify the hypothesized difference as <tt>&quot;DIFF&quot;</tt>, where <tt>&quot;DIFF&quot;</tt> is something like <tt>&quot;&lt;=0&quot;</tt> or <tt>&quot;&gt;=0&quot;</tt>, etc.</dl>
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
    #fsdb title mean2 stddev2 n2 mean1 stddev1 n1
    example6.12 0.17 0.0020 5 0.22 0.0010 4
</pre>
<h3>Command:</h3>
<pre>
    cat data.fsdb | dbrvstatdiff mean2 stddev2 n2 mean1 stddev1 n1
</pre>
<h3>Output:</h3>
<pre>
    #fsdb title mean2 stddev2 n2 mean1 stddev1 n1 diff diff_pct diff_conf_half diff_conf_low diff_conf_high diff_conf_pct_half diff_conf_pct_low diff_conf_pct_high
    example6.12 0.17    0.0020  5       0.22    0.0010  4       0.05    29.412  0.0026138       0.047386        0.052614        1.5375  27.874  30.949
    #  | dbrvstatdiff mean2 stddev2 n2 mean1 stddev1 n1
</pre>
<h3>Input 2:</h3>
<p> (example 7.10 from Scheaffer and McClave): </p>
<pre>
    #fsdb title x2 sd2 n2 x1 sd1 n1
    example7.10 9 35.22 24.44 9 31.56 20.03
</pre>
<h3>Command 2:</h3>
<pre>
    dbrvstatdiff -h '&lt;=0' x2 sd2 n2 x1 sd1 n1
</pre>
<h3>Output 2:</h3>
<pre>
    #fsdb title n1 x1 sd1 n2 x2 sd2 diff diff_pct diff_conf_half diff_conf_low diff_conf_high diff_conf_pct_half diff_conf_pct_low diff_conf_pct_high t_test t_test_result
    example7.10 9 35.22 24.44 9 31.56 20.03 3.66 0.11597 4.7125 -1.0525 8.3725 0.14932 -0.033348 0.26529 1.6465 not-rejected
    #  | /global/us/edu/ucla/cs/ficus/users/johnh/BIN/DB/dbrvstatdiff -h &lt;=0 x2 sd2 n2 x1 sd1 n1
</pre>
<h3>Case 3:</h3>
<p> A common use case is to have one file with a set of trials from two experiments, and to use dbrvstatdiff to see if they are different. </p>
<p> <i>Input 3:</i> </p>
<pre>
    #fsdb case trial value
    a  1  1
    a  2  1.1
    a  3  0.9
    a  4  1
    a  5  1.1
    b  1  2
    b  2  2.1
    b  3  1.9
    b  4  2
    b  5  1.9
</pre>
<h3>Command 3:</h3>
<pre>
    cat two_trial.fsdb | 
        dbmultistats -k case value |
        dbcolcopylast mean stddev n |
        dbrow '_case eq &quot;b&quot;' |
        dbrvstatdiff -h '=0' mean stddev n copylast_mean copylast_stddev copylast_n |
        dblistize
</pre>
<p> <i>Output 3:</i> </p>
<pre>
        #fsdb -R C case mean stddev pct_rsd conf_range conf_low conf_high conf_pct sum sum_squared min max n copylast_mean copylast_stddev copylast_n diff diff_pct diff_conf_half diff_conf_low diff_conf_high diff_conf_pct_half diff_conf_pct_low diff_conf_pct_high t_test t_test_result t_test_break t_test_break_pct
        case: b
        mean: 1.98
        stddev: 0.083666
        pct_rsd: 4.2256
        conf_range: 0.10387
        conf_low: 1.8761
        conf_high: 2.0839
        conf_pct: 0.95
        sum: 9.9
        sum_squared: 19.63
        min: 1.9
        max: 2.1
        n: 5
        copylast_mean: 1.02
        copylast_stddev: 0.083666
        copylast_n: 5
        diff: -0.96
        diff_pct: -48.485
        diff_conf_half: 0.12202
        diff_conf_low: -1.082
        diff_conf_high: -0.83798
        diff_conf_pct_half: 6.1627
        diff_conf_pct_low: -54.648
        diff_conf_pct_high: -42.322
        t_test: -18.142
        t_test_result: rejected
        t_test_break: -1.082
        t_test_break_pct: -54.648
        
        #  | dbmultistats -k case value
        #   | dbcolcopylast mean stddev n
        #   | dbrow _case eq &quot;b&quot;
        #   | dbrvstatdiff -h =0 mean stddev n copylast_mean copylast_stddev copylast_n
        #   | dbfilealter -R C
</pre>
<p> (So one cannot say that they are statistically equal.)</p>
<h2>SEE ALSO</h2>
<p> Fsdb. dbcolstats. dbcolcopylast.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
