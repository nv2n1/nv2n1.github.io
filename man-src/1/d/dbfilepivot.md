---
title: "dbfilepivot(1)"
name: "dbfilepivot"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbfilepivot/"
description: "dbfilepivot – pivot a table, converting multiple rows into single wide row"
---

<h2 class="name">NAME</h2>
<p> dbfilepivot &#8211; pivot a table, converting multiple rows into single wide row </p>
<h2>SYNOPSIS</h2>
<p> dbfilepivot [-e empty] -k KeyField -p PivotField [-v ValueField]</p>
<h2>DESCRIPTION</h2>
<p> Pivot a table, converting multiple rows corresponding to the same key into a single wide row. </p>
<p> In a normalized database, one might have data with a schema like (id, attribute, value), but sometimes it&#8217;s more convenient to see the data with a schema like (id, attribute1, attribute2). (For example, gnuplot&#8217;s stacked histograms requires denormalized data.) Dbfilepivot converts the normalized format to the denormalized, but sometimes useful, format. Here the &#8220;id&#8221; is the key, the attribute is the &#8220;pivot&#8221;, and the value is, well, the optional &#8220;value&#8221;. </p>
<p> An example is clearer. A gradebook usually looks like: </p>
<pre>
    #fsdb name hw_1 hw_2 hw_3
    John       97  98  99
    Paul       -   80  82
</pre>
<p> but a properly normalized format would represent it as: </p>
<pre>
    #fsdb name hw score
    John       1  97
    John       2  98
    John       3  99
    Paul       2  80
    Paul       3  82
</pre>
<p> This tool converts the second form into the first, when used as </p>
<pre>
    dbfilepivot -k name -p hw -v score
</pre>
<p> Here name is the <i>key</i> column that indicates which rows belong to the same entity, hw is the <i>pivot</i> column that will be indicate which column in the output is relevant, and score is the <i>value</i> that indicates what goes in the output. </p>
<p> The pivot creates a new column <tt>&quot;key_tag1&quot;</tt>, <tt>&quot;key_tag2&quot;</tt>, etc. for each tag, the contents of the pivot field in the input. It then populates those new columns with the contents of the value field in the input. </p>
<p> If no value column is specified, then values are either empty or 1. </p>
<p> Dbfilepivot assumes all lines with the same key are adjacent in the input source, like <i><a href="/docs/linux/man/1-dbmapreduce/">dbmapreduce</a></i>(1) with the <i>-S</i> option. To enforce this invariant, by default, it <i>requires</i> input be sorted by key. </p>
<p> Dbfilepivot makes two passes over its data and so requires temporary disk space equal to the input size. </p>
<p> Memory usage is proportional to the number of unique pivot values.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-k</code> or <code>&#8211;key</code> KeyField</dt>
<dd> specify which column is the key for grouping. Required (no default).</dd>
<dt><code>-p</code> or <code>&#8211;pivot</code> PivotField</dt>
<dd> specify which column is the key to indicate which column in the output is relevant. Required (no default).</dd>
<dt><code>-v</code> or <code>&#8211;value</code> ValueField</dt>
<dd> Specify which column is the value in the output. If none is given, 1 is used for the value.</dd>
<dt><code>-C S</code> or <code>&#8211;element-separator S</code></dt>
<dd> Specify the separator <i>S</i> used to join the input&#8217;s key column with its contents. (Defaults to a single underscore.)</dd>
<dt><code>-e E</code> or <code>&#8211;empty E</code></dt>
<dd> give value E as the value for empty (null) records</dd>
<dt><code>-S</code> or <code>&#8211;pre-sorted</code></dt>
<dd> Assume data is already grouped by key. Provided twice, it removes the validation of this assertion. By default, we sort by key.</dd>
<dt><code>-T TmpDir</code></dt>
<dd> where to put tmp files. Also uses environment variable <font SIZE="-1">TMPDIR,</font> if -T is not specified. Default is /tmp.</dd></dl>
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
    #fsdb name hw_1 hw_2 hw_3
    John       97  98  99
    Paul       -   80  82
</pre>
<h3>Command:</h3>
<pre>
    cat data.fsdb | dbfilepivot -k name -p hw -v score
</pre>
<h3>Output:</h3>
<pre>
    #fsdb name hw score
    John       1  97
    John       2  98
    John       3  99
    Paul       2  80
    Paul       3  82
</pre>
<h2>SEE ALSO</h2>
<p> <i>Fsdb</i>(3). <i><a href="/docs/linux/man/1-dbcolmerge/">dbcolmerge</a></i>(1). <i><a href="/docs/linux/man/1-dbcolsplittorows/">dbcolsplittorows</a></i>(1). <i><a href="/docs/linux/man/1-dbcolsplittocols/">dbcolsplittocols</a></i>(1).</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 2011-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
