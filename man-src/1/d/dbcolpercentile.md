---

title: "dbcolpercentile(1)"
name: "dbcolpercentile"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbcolpercentile/"
description: "dbcolpercentile – compute percentiles or ranks for an existing column"
---

<pre>
    dbcolpercentile [-rplhS] column
</pre>
<p> Compute a percentile of a column of numbers. The new column will be called <i>percentile</i> or <i>rank</i>. Non-numeric records are handled as in other programs. </p>
<p> If the data is pre-sorted and only a rank is requested, no extra storage is required. In all other cases, a full copy of data is buffered on disk.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p</code> or <code>&#8211;percentile</code></dt>
<dd> Show percentile (default).</dd>
<dt><code>-P</code> or <code>&#8211;rank</code> or <code>&#8211;nopercentile</code></dt>
<dd> Compute ranks instead of percentiles.</dd>
<dt><code>&#8211;fraction</code></dt>
<dd> Show fraction (percentage, except between 0 and 1, not cumulative fraction).</dd>
<dt><code>-a</code> or <code>&#8211;include-non-numeric</code></dt>
<dd> Compute stats over all records (treat non-numeric records as zero rather than just ignoring them).</dd>
<dt><code>-S</code> or <code>&#8211;pre-sorted</code></dt>
<dd> Assume data is already sorted. With one -S, we check and confirm this precondition. When repeated, we skip the check.</dd>
<dt><code>-f </code><font SIZE="-1"><code>FORMAT</code></font> or <code>&#8211;format </code><font SIZE="-1"><code>FORMAT</code></font></dt>
<dd> Specify a <i><a href="/docs/linux/man/3-printf/">printf</a></i>(3)-style format for output statistics. Defaults to <tt>&quot;%.5g&quot;</tt>.</dd>
<dt><code>-T TmpDir</code></dt>
<dd> where to put tmp files. Also uses environment variable <font SIZE="-1">TMPDIR,</font> if -T is not specified. Default is /tmp.</dd></dl>
<p> Sort specification options (can be interspersed with column names):</p>
<dl>
<dt><code>-r</code> or <code>&#8211;descending</code></dt>
<dd> sort in reverse order (high to low)</dd>
<dt><code>-R</code> or <code>&#8211;ascending</code></dt>
<dd> sort in normal order (low to high)</dd>
<dt><code>-n</code> or <code>&#8211;numeric</code></dt>
<dd> sort numerically (default)</dd>
<dt><code>-N</code> or <code>&#8211;lexical</code></dt>
<dd> sort lexicographically</dd></dl>
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
    cat DATA/grades.fsdb | dbcolpercentile test1
</pre>
<h3>Output:</h3>
<pre>
        #fsdb name id test1 percentile
        d       4       90      1
        f       6       90      1
        a       1       80      0.66667
        b       2       70      0.5
        e       5       70      0.5
        c       3       65      0.16667
        #  | dbsort -n test1
        #   | dbcolpercentile test1
</pre>
<h3>Command 2:</h3>
<pre>
    cat DATA/grades.fsdb | dbcolpercentile --rank test1
</pre>
<h3>Output 2:</h3>
<pre>
        #fsdb name id test1 rank
        d       4       90      1
        f       6       90      1
        a       1       80      3
        b       2       70      4
        e       5       70      4
        c       3       65      6
        #  | dbsort -n test1
        #   | dbcolpercentile --rank test1
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb. dbcolhisto.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
