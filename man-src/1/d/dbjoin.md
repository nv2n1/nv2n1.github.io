---
title: "dbjoin(1)"
name: "dbjoin"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbjoin/"
description: "dbjoin – join two tables on common columns"
---

<h2 class="name">NAME</h2>
<p> dbjoin &#8211; join two tables on common columns </p>
<h2>SYNOPSIS</h2>
<pre><code>
dbjoin[-Sid]-- input table1.fsdb-- input table2.fsdb[-nNrR] column[column...]
</code></pre>
<p> <font SIZE="-1">OR</font> </p>
<pre><code>
cat table1.fsdb | dbjoin[-Sid]-- input table2.fsdb[-nNrR] column[column...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Does a natural, inner join on <font SIZE="-1">TABLE1</font> and <font SIZE="-1">TABLE2 </font> the specified columns. With the <tt>&quot;-a&quot;</tt> option, or with <tt>&quot;-t outer&quot;</tt> it will do a natural, full outer join. </p>
<p> (Database review: inner joints output records only when there are matches in both tables and will omit records that do not match. Outer joins output all records from both tables, filling with the empty value as needed. Right (left) outer joins keep all elements of the right (left) table, even those that don&#8217;t match in the other table.) </p>
<p> By default for non-hash joins, data will be sorted lexically, but the usual sorting options can be mixed with the column specification. </p>
<p> Because two tables are required, input is typically in files. Standard input is accessible by the file &#8220;-&#8221;.</p>
<h2>RESOURCE REQUIREMENTS AND PERFORMANCE</h2>
<p> Joins can be expensive. Most databases have a query optimizer that knows something about the data and so can select algorithms for efficent operation, in Fsdb, <i>you</i> are that optimizer. </p>
<p> For <i>non-hash joins</i>: If data is already sorted, dbjoin will run more efficiently by telling dbjoin the data is sorted with the <tt>&quot;-S&quot;</tt>. </p>
<p> The resource requirements dbjoin vary. If input data is sorted and <tt>&quot;-S&quot;</tt> is given, then memory consumption is bounded by the the sum of the largest number of records in either dataset with the same value in the join column, and there is no disk consumption. If data is not sorted, then dbjoin requires disk storage the size of both input files. </p>
<p> One can minimize memory consumption by making sure each record of table1 matches relatively few records in table2. Typically this means that table2 should be the smaller. For example, given two files: people.fsdb (schema: name iso_country_code) and countries.fsdb (schema: iso_country_code full_country_name), then </p>
<pre>
    dbjoin -i people.fsdb -i countries.fsdb iso_country_code
</pre>
<p> will require less memory than </p>
<pre>
    dbjoin -i countries.fsdb -i people.fsdb iso_country_code
</pre>
<p> if there are many people per country (as one would expect). If warning &#8220;lots of matching rows accumulating in memory&#8221; appears, this is the cause and try swapping join order. </p>
<p> For <i>hash joins</i> (that is, with <tt>&quot;-m righthash&quot;</tt> or <tt>&quot;-m lefthash&quot;</tt>): all of the right table (the second input) or the left (the first) is loaded into memory (and &#8220;hashed&#8221;). The other table need not be sorted. Runtime is <a href="/docs/linux/man/n-o/">O</a>(n), but memory is O(size of hashed table).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code> or <code>&#8211;all</code></p>
<dd> Perform a <i>full outer join</i>, include non-matches (each record which doesn&#8217;t match at all will appear once). Default is an <i>inner join</i>.</p>
<dt><code>-t </code><font SIZE="-1"><code>TYPE</code></font> or <code>&#8211;type </code><font SIZE="-1"><code>TYPE</code></font></p>
<dd> Explicitly specify the join type. <font SIZE="-1">TYPE</font> must be inner, outer, left (outer), right (outer). Default: inner.</p>
<dt><code>-m </code><font SIZE="-1"><code>METHOD</code></font> or <code>&#8211;method </code><font SIZE="-1"><code>METHOD</code></font></p>
<dd> Select join method (algorithm). Choices are merge, righthash, and lefthash. Default: merge.</p>
<dt><code>-S</code> or <code>&#8211;pre-sorted</code></p>
<dd> assume (and verify) data is already sorted</p>
<dt><code>-e E</code> or <code>&#8211;empty E</code></p>
<dd> give value E as the value for empty (null) records</p>
<dt><code>-T TmpDir</code></p>
<dd> where to put tmp files. Also uses environment variable <font SIZE="-1">TMPDIR,</font> if -T is not specified. Default is /tmp.</dl>
<p> Sort specification options (can be interspersed with column names):</p>
<dl>
<dt><code>-r</code> or <code>&#8211;descending</code></p>
<dd> sort in reverse order (high to low)</p>
<dt><code>-R</code> or <code>&#8211;ascending</code></p>
<dd> sort in normal order (low to high)</p>
<dt><code>-n</code> or <code>&#8211;numeric</code></p>
<dd> sort numerically</p>
<dt><code>-N</code> or <code>&#8211;lexical</code></p>
<dd> sort lexicographically</dl>
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
    #fsdb sid cid
    1 10
    2 11
    1 12
    2 12
</pre>
<p> And in the file <i>DATA/classes</i>: </p>
<pre>
    #fsdb cid cname
    10 pascal
    11 numanal
    12 os
</pre>
<h3>Command:</h3>
<pre>
    cat DATA/reg.fsdb | dbsort -n cid | dbjoin -i - -i DATA/classes -n cid
</pre>
<h3>Output:</h3>
<pre>
    #fsdb      cid     sid     cname
    10      1       pascal
    11      2       numanal
    12      1       os
    12      2       os
    # - COMMENTS:
    #  | /home/johnh/BIN/DB/dbsort -n cid
    # DATA/classes COMMENTS:
    # joined comments:
    #  | /home/johnh/BIN/DB/dbjoin - DATA/classes cid
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2016 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
