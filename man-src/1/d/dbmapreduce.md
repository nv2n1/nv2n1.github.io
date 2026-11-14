---
title: "dbmapreduce(1)"
name: "dbmapreduce"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbmapreduce/"
description: "dbmapreduce – reduce all input rows with the same key"
---

<h2 class="name">NAME</h2>
<p> dbmapreduce &#8211; reduce all input rows with the same key </p>
<h2>SYNOPSIS</h2>
<pre><code>
dbmapreduce[-dMS][-k KeyField][-f CodeFile][-C Filtercode][--][ReduceCommand[ReduceArguments...]]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Group input data by KeyField, then apply a function (the &#8220;reducer&#8221;) to each group. The reduce function can be an external program given by ReduceCommand and ReduceArguments, or an Perl subroutine given in CodeFile or FilterCode. </p>
<p> If a &#8220;&#8211;&#8221; appears before reduce command, arguments after the &#8212; passed the the command.</p>
<h3>Grouping (The Mapper)</h3>
<p> By default the KeyField is the first field in the row. Unlike Hadoop streaming, the -k KeyField option can explicitly name where the key is in any column of each input row. </p>
<p> By default, we sort the data to make sure data is grouped by key. If the input is already grouped, the <tt>&quot;-S&quot;</tt> option avoids this cost.</p>
<h3>The Reducer</h3>
<p> Reduce functions default to be shell commands. However, with <tt>&quot;-C&quot;</tt>, one can use arbitrary Perl code </p>
<p> (see the <tt>&quot;-C&quot;</tt> option below for details). the <tt>&quot;-f&quot;</tt> option is useful to specify complex Perl code somewhere other than the command line. </p>
<p> Finally, as a special case, if there are no rows of input, the reducer will be invoked once with the empty value (if it&#8217;s an external reducer) or with undef (if it&#8217;s a subroutine). It is expected to generate the output header, and it may generate no data rows itself, or a null data row of its choosing.</p>
<h3>Output</h3>
<p> For non-multi-key-aware reducers, we add the KeyField use for each Reduce is in the output stream. (If the reducer passes the key we trust that it gives a correct value.) We also insure that the output field separator is the same as the input field separator. </p>
<p> Adding the key and adjusting the output field separator is not possible for non-multi-key-aware reducers.</p>
<h3>Comparison to Related Work</h3>
<p> This program thus implements Google-style map/reduce, but executed sequentially. </p>
<p> For input, these systems include a map function and apply it to input data to generate the key. We assume this key generation (the map function) has occurred head of time. </p>
<p> We also allow the grouping key to be in any column. Hadoop Streaming requires it to be in the first column. </p>
<p> By default, the reducer gets exactly (and only) one key. This invariant is stronger than Google and Hadoop. They both pass multiple keys to the reducer, insuring that each key is grouped together. With the <tt>&quot;-M&quot;</tt> option, we also pass multiple multiple groups to the reducer. </p>
<p> Unlike those systems, with the <tt>&quot;-S&quot;</tt> option we do not require the groups arrive in any particular order, just that they be grouped together. (They guarantees they arrive in lexically sorted order). However, with <tt>&quot;-S&quot;</tt> we create lexical ordering. </p>
<p> With <tt>&quot;--prepend-key&quot;</tt> we insure that the KeyField is in the output stream; other systems do not enforce this.</p>
<h3>Assumptions and requirements</h3>
<p> By default, data can be provided in arbitrary order and the program consumes O(number of unique tags) memory, and O(size of data) disk space. </p>
<p> With the <tt>&quot;-S&quot;</tt> option, data must arrive group by tags (not necessarily sorted), and the program consumes O(number of tags) memory and no disk space. The program will check and abort if this precondition is not met. </p>
<p> With two <tt>&quot;-S&quot;</tt>&#8216;s, program consumes <a href="/docs/linux/man/1-o/">O</a>(1) memory, but doesn&#8217;t verify that the data-arrival precondition is met. </p>
<p> The field separators of the input and the output can now be different (early versions of this tool prohibited such variation.) With <tt>&quot;--copy-fs&quot;</tt> we copy the input field separator to the output, but only for non-multi-key-aware reducers. (this used to be done automatically).</p>
<h3>Known bugs</h3>
<p> As of 2013-09-21, we don&#8217;t verify key order with options <tt>&quot;-M -S&quot;</tt>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-k</code> or <code>&#8211;key</code> KeyField</p>
<dd> specify which column is the key for grouping (default: the first column)</p>
<dt><code>-S</code> or <code>&#8211;pre-sorted</code></p>
<dd> Assume data is already grouped by tag. Provided twice, it removes the validation of this assertion.</p>
<dt><code>-M</code> or <code>&#8211;multiple-ok</code></p>
<dd> Assume the ReduceCommand can handle multiple grouped keys, and the ReduceCommand is responsible for outputting the with each output row. (By default, a separate ReduceCommand is run for each key, and dbmapreduce adds the key to each output row.)</p>
<dt><code>-K</code> or <code>&#8211;pass-current-key</code></p>
<dd> Pass the current key as an argument to the external, non-map-aware ReduceCommand. This is only done optionally since some external commands do not expect an extra argument. (Internal, non-map-aware Perl reducers are always given the current key as an argument.)</p>
<dt><code>&#8211;prepend-key</code></p>
<dd> Add the current key into the reducer output for non-multi-key-aware reducers only. Not done by default.</p>
<dt><code>&#8211;copy-fs</code> or <code>&#8211;copy-fieldseparator</code></p>
<dd> Change the field separator of a non-multi-key-aware reducers to match the input&#8217;s field separator. Not done by default.</p>
<dt>&lt;&#8211;parallelism=N&gt;</p>
<dd> Allow up to N reducers to run in parallel. Default is the number of CPUs in the machine.</p>
<dt><code>-C FILTER-CODE</code> or <code>&#8211;filter-code=FILTER-CODE</code></p>
<dd> Provide FILTER-CODE, Perl code that generates and returns a Fsdb::Filter object that implements the reduce function. The provided code should be an anonymous sub that creates a Fsdb Filter that implements the reduce object. </p>
<p> The reduce object will then be called with &#8211;input and &#8211;output parameters that hook it into a the reduce with queues. </p>
<p> One sample fragment that works is just: </p>
<pre>
    dbcolstats(qw(--nolog duration))
</pre>
<p> So this command: </p>
<pre>
    cat DATA/stats.fsdb | \
        dbmapreduce -k experiment -C 'dbcolstats(qw(--nolog duration))'
</pre>
<p> is the same as the example </p>
<pre>
    cat DATA/stats.fsdb | \
        dbmapreduce -k experiment -- dbcolstats duration
</pre>
<p> except that with <tt>&quot;-C&quot;</tt> there is no forking and so things run faster. </p>
<p> If <tt>&quot;dbmapreduce&quot;</tt> is invoked from within Perl, then one can use a code <font SIZE="-1">SUB</font> as well:<br />
&nbsp;<wbr>dbmapreduce(-k&nbsp;<wbr>=&gt;&nbsp;<wbr>&#8216;experiment&#8217;,&nbsp;<wbr> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-C =&gt; sub { dbcolstats(qw(&#8211;nolong duration)) });</p>
<p> The reduce object must consume <i>all</i> input as a Fsdb stream, and close the output Fsdb stream. (If this assumption is not met the map/reduce will be aborted.) </p>
<p> For non-map-reduce-aware filters, when the filter-generator code runs, <tt>$_[0]</tt> will be the current key.</p>
<dt><code>-f CODE-FILE</code> or <code>&#8211;code-file=CODE-FILE</code></p>
<dd> Includes <i>CODE-FILE</i> in the program. This option is useful for more complicated perl reducer functions. </p>
<p> Thus, if reducer.pl has the code. </p>
<pre><code>
sub make_reducer
{
    my($current_key) = @_;
    dbcolstats(qw(--nolog duration));
}
</code></pre>
<p> Then the command </p>
<pre>
    cat DATA/stats.fsdb | \
        dbmapreduce -k experiment -f reducer.pl -C make_reducer
</pre>
<p> does the same thing as the example.</p>
<dt><code>-w</code> or <code>&#8211;warnings</code></p>
<dd> Enable warnings in user supplied code. Warnings are issued if an external reducer fails to consume all input. (Default to include warnings.)</p>
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
<dt><code>&#8211;header</code> H</p>
<dd> Use H as the full Fsdb header, rather than reading a header from then input.</p>
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
    cat DATA/stats.fsdb | \
        dbmapreduce --prepend-key -k experiment -- dbcolstats duration
</pre>
<h3>Output:</h3>
<pre>
    #fsdb      experiment      mean    stddev  pct_rsd conf_range      conf_low       conf_high        conf_pct        sum     sum_squared     min     max     n
    ufs_mab_sys     37.25 0.070711 0.18983 0.6353 36.615 37.885 0.95 74.5 2775.1 37.2 37.3 2
    ufs_rcp_real    271.2 9.4752 3.4938 85.13 186.07 356.33 0.95 542.4 1.4719e+05 264.5 277.9 2
    #  | dbmapreduce -k experiment dbstats duration
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb. dbmultistats dbrowsplituniq</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2016 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
