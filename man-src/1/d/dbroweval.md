---
title: "dbroweval(1)"
name: "dbroweval"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbroweval/"
description: "dbroweval – evaluate code for each row of a fsdb file"
---

<h2 class="name">NAME</h2>
<p> dbroweval &#8211; evaluate code for each row of a fsdb file </p>
<h2>SYNOPSIS</h2>
<pre><code>
dbroweval[-f CodeFile] code[code...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Evaluate code for each row of the data. </p>
<p> Typical actions are things like reformatting and other data transformations. </p>
<p> Code can include embedded column names preceded by underscores; these result in the value of that column for the current row. </p>
<p> The values of the last row&#8217;s columns are retrieved with _last_foo where foo is the column name. </p>
<p> Even more perverse, _columname(N) is the value of the Nth column after columnname [so <i>_columnname</i>(0) is the also the column&#8217;s value.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b </code><font SIZE="-1"><code>CODE</code></font></p>
<dd> Run <font SIZE="-1">CODE</font> before reading any data (like awk <font SIZE="-1">BEGIN</font> blocks).</p>
<dt><code>-e </code><font SIZE="-1"><code>CODE</code></font></p>
<dd> Run <font SIZE="-1">CODE</font> at the end of all data (like awk <font SIZE="-1">END</font> blocks).</p>
<dt><code>-f </code><font SIZE="-1"><code>FILE</code></font></p>
<dd> Read code from the <font SIZE="-1">FILE.</font></p>
<dt><code>-n</code> or <code>&#8211;no-output</code></p>
<dd> no output except for comments and what is in the provided code</p>
<dt><code>-N</code> or <code>&#8211;no-output-even-comments</code></p>
<dd> no output at all, except for what is in the provided code</p>
<dt><code>-m</code> or <code>&#8211;manual-output</code></p>
<dd> The user must setup output, allowing arbitrary comments. See example 2 below for details.</p>
<dt><code>-w</code> or <code>&#8211;warnings</code></p>
<dd> Enable warnings in user supplied code.</p>
<dt><code>&#8211;saveoutput $OUT_REF</code></p>
<dd> Save output writer (for integration with other fsdb filters).</dl>
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
<h2>ADVANCED USAGE</h2>
<p> Typically dbroweval outputs a line in the same schema for each input line. For advanced usage, one can violate each of these assumptions. </p>
<p> Some fun:</p>
<dl>
<dt><code>omitting a line</code></p>
<dd> Add the code <tt>&quot;next row if ($your condition);&quot;</tt></p>
<dt><code>outputting an extra line</code></p>
<dd> Call <tt>&quot;&amp;$write_fastpath_sub($fref)&quot;</tt>. You may find <tt>$fref</tt>, the input row, useful.</p>
<dt><code>changing the schema</code></p>
<dd> See the examples below in &#8220;Command 2: Changing the Schema&#8221;</dl>
<h2>SAMPLE USAGE</h2>
<h3>Input:</h3>
<pre>
    #fsdb      size    mean    stddev  pct_rsd
    1024    1.4962e+06      2.8497e+05      19.047
    10240   5.0286e+06      6.0103e+05      11.952
    102400  4.9216e+06      3.0939e+05      6.2863
    #  | dbsetheader size bw
    #  | /home/johnh/BIN/DB/dbmultistats size bw
    #  | /home/johnh/BIN/DB/dbcol size mean stddev pct_rsd
</pre>
<h3>Command:</h3>
<p>cat data.fsdb | dbroweval &#8216;_mean = sprintf(&#8220;%8.0f&#8221;, _mean); _stddev = sprintf(&#8220;%8.0f&#8221;, _stddev);&#8217;</p>
<h3>Output:</h3>
<p>#fsdb size mean stddev pct_rsd<br />
1024 1496200 284970 19.047 10240 5028600 601030 11.952 102400 4921600 309390 6.2863<br />
#| dbsetheader size bw<br />
#| / home / johnh / BIN / DB / dbmultistats size bw<br />
#| / home / johnh / BIN / DB / dbcol size mean stddev pct_rsd<br />
#| / home / johnh / BIN / DB / dbroweval{_mean = sprintf(&#8220;%8.0f&#8221;, _mean); _stddev = sprintf(&#8220;%8.0f&#8221;, _stddev); }</p>
<h3>Command 2: Changing the Schema</h3>
<p> By default, dbroweval reads and writes the same format file. The recommended method of adding and removing columns is to do so before or after dbroweval. I.e., </p>
<pre>
    cat data.fsdb |
        dbcolcreate divisible_by_ten | 
        dbroweval '_divisible_by_ten = (_size % 10 == 0);' |
        dbrow '_divisible_by_ten == 1' |
        dbcol size mean divisible_by_ten
</pre>
<p> Another approach is to use the <tt>&quot;next row&quot;</tt> command to skip output of a row. I.e., the equivalent: </p>
<p>cat data.fsdb |<br />
    dbcolcreate divisible_by_ten |<br />
    dbroweval &#8216;_divisible_by_ten = (_size % 10 == 0); next row if (!_divisible_by_ten);&#8217; |<br />
    dbcol size mean divisible_by_ten</p>
<p> However, neither of these approachs work very well when the output is a <i>completely</i> different schema. </p>
<p> The recommended method for schema-changing commands is to write a full filter, but a full filter is a bit heavy weight. As an alternative, one can use the <tt>&quot;-m&quot;</tt> option to request manual configuration of the output, then use <tt>@out_args</tt> to define the output schema (it specifies the <tt>&quot;Fsdb::IO::Writer&quot;</tt> arguments), and <tt>$ofref</tt> is the output row. It may also reference &lt;$in&gt;, the input <tt>&quot;Fsdb::IO::Reader&quot;</tt> argument, and &lt;$fref&gt; as an aref to the current line. Note that newly created columns <i>do not</i> have underscore-names </p>
<p> Thus a third equivalent is: </p>
<p>cat data.fsdb |<br />
    dbroweval &#8211; m &#8211; b &#8216;@out_args = ( -clone =&gt; $in, \<br />
                 -cols =&gt; ($in-&gt;cols, divisible_by_ten); &#8216; &#8216;my $div_by_10 = (_size % 10 == 0); \<br />
            $ofref = [ @$fref, $div_by_10 ] if ($div_by_ten);&#8217; |<br />
    dbcol size mean divisible_by_ten</p>
<p> or </p>
<p>cat data.fsdb |<br />
    dbroweval &#8211; m &#8211; b &#8216;@out_args = ( -clone =&gt; $in, \<br />
                -cols =&gt; [qw(size mean divisible_by_ten)] ); &#8216; &#8216;my $div_by_10 = (_size % 10 == 0);  \<br />
            $ofref = [ _mean, _size, $div_by_10 ] if ($div_by_ten);&#8217;</p>
<p> Finally, one can write different a completely different schema, although it&#8217;s more work: </p>
<p>cat data.fsdb |<br />
    dbroweval &#8211; m &#8211; b &#8216;@out_args = (-cols =&gt; [qw(size n)]);&#8217; &#8216;$ofref = [ _size, 1 ];&#8217;</p>
<p> writes different columns, and </p>
<pre><code>
cat data.fsdb |
    dbroweval - n - m - b '@out_args = (-cols =&gt; [qw(n)]);  \
            my $count = 0;' -
        e '$ofref = [ $count ];' '$count++;'
</code></pre>
<p> Is a fancy way to count lines. </p>
<p> The begin code block should setup <tt>@out_args</tt> to be the arguments to a <tt>&quot;Fsdb::IO::Writer::new&quot;</tt> call, and whatever is in <tt>$ofref</tt> (if anything) is written for each input line, and once at the end.</p>
<h3>Command 3: Fun With Suppressing Output</h3>
<p> The <tt>&quot;-n&quot;</tt> option suppresses default output. Thus, a simple equivalent to <i>tail -1</i> is: </p>
<pre>
    dbroweval -n -e '$ofref = $lfref;'
</pre>
<p> Where <tt>$ofref</tt> is the output fields, which are copied from <tt>$lfref</tt>, the hereby documented internal representation of the last row. Yes, this is a bit unappetizing, but, in for a penny with <tt>$ofref</tt>, in for a pound.</p>
<h3>Command 4: Extra Ouptut</h3>
<p> Calling <tt>&quot;&amp;$write_fastpath_sub($fref)&quot;</tt> will do extra output, so this simple program will duplicate each line of input (one extra output, plus one regular output for each line of input): </p>
<pre>
    dbroweval  '&amp;$write_fastpath_sub($fref)'
</pre>
<h2>BUGS</h2>
<p> Handling of code in files isn&#8217;t very elegant.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-fsdb/">Fsdb</a></i>(3)</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2007 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
