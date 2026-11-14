---
title: "dbrowcount(1)"
name: "dbrowcount"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbrowcount/"
description: "dbrowcount – count the number of rows in an Fsdb stream"
---

<h2 class="name">NAME</h2>
<p> dbrowcount &#8211; count the number of rows in an Fsdb stream </p>
<h2>SYNOPSIS</h2>
<p> dbrowcount</p>
<h2>DESCRIPTION</h2>
<p> Count the number of rows and write out a new fsdb file with one column (n) and one value: the number of rows. This program is a strict subset of dbcolstats. </p>
<p> Although there are other ways to get a count of rows (<tt>&quot;dbcolstats&quot;</tt>, or <tt>&quot;dbrowaccumulate -C 1&quot;</tt> and some processing), counting is so common it warrants its own command. (For example, consider how often <tt>&quot;wc -l&quot;</tt> is used in regular shell scripting.) There are some gross and subtle differences, though, in that <tt>&quot;dbrowcount&quot;</tt> doesn&#8217;t require one to specify a column to search, and it also doesn&#8217;t look for and skip null data items.</p>
<h2>OPTIONS</h2>
<p> No program-specific options. </p>
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
    cat data.fsdb | dbrowcount
</pre>
<h3>Output:</h3>
<pre>
    #fsdb n
    6
    #  | /home/johnh/BIN/DB/dbrow 
    #  | /home/johnh/BIN/DB/dbcol event clock
    #  | dbrowdiff clock
    #  | /home/johnh/BIN/DB/dbcol absdiff
</pre>
<h3>Input 2:</h3>
<p> As another example, this input produces the same output as above in <tt>&quot;dbrowcount&quot;</tt>, but different output in <tt>&quot;dbstats&quot;</tt>: </p>
<pre>
    #fsdb      absdiff
    -
    -
    -
    -
    -
    -
    #  | /home/johnh/BIN/DB/dbrow 
    #  | /home/johnh/BIN/DB/dbcol event clock
    #  | dbrowdiff clock
    #  | /home/johnh/BIN/DB/dbcol absdiff
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-dbcolaccumulate/">dbcolaccumulate</a></i>(1), <i><a href="/docs/linux/man/1-dbcolstats/">dbcolstats</a></i>(1), <i><a href="/docs/linux/man/3-fsdb/">Fsdb</a></i>(3)</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 2007-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
