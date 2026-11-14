---
title: "dbcolcreate(1)"
name: "dbcolcreate"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbcolcreate/"
description: "dbcolcreate – create new columns"
---

<h2 class="name">NAME</h2>
<p> dbcolcreate &#8211; create new columns </p>
<h2>SYNOPSIS</h2>
<pre>
    dbcolcreate NewColumn1 [NewColumn2]
</pre>
<p> or </p>
<pre>
    dbcolcreate -e DefaultValue NewColumnWithDefault
</pre>
<h2>DESCRIPTION</h2>
<p> Create columns <tt>&quot;NewColumn1&quot;</tt>, etc. with an optional <tt>&quot;DefaultValue&quot;</tt>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-e</code> EmptyValue or <code>&#8211;empty</code></p>
<dd> Specify the value newly created columns get.</p>
<dt><code>-f</code> or <code>&#8211;first</code></p>
<dd> Put all new columns as the first columns of each row. By default, they go at the end of each row.</p>
<dt><code>&#8211;no-recreate-fatal</code></p>
<dd> By default, creating an existing column is an error. With <code>&#8211;no-recreate-fatal</code>, we ignore re-creation.</dl>
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
    #fsdb test
    a
    b
</pre>
<h3>Command:</h3>
<pre>
    cat data.fsdb | dbcolcreate foo
</pre>
<h3>Output:</h3>
<pre>
    #fsdb      test    foo
    a       -
    b       -
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
