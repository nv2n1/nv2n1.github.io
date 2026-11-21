---

title: "dbcolcopylast(1)"
name: "dbcolcopylast"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbcolcopylast/"
description: "dbcolcopylast – create new columns that are copies of prior columns"
---

<pre><code>
dbcolcopylast[-e EMPTY][column...]
</code></pre>
<p> For each <font SIZE="-1">COLUMN,</font> create a new column copylast_COLUMN that is the last value for that column&#8212;that is, the value of that column from the row before.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-e</code> EmptyValue or <code>&#8211;empty</code></dt>
<dd> Specify the value newly created columns get.</dd></dl>
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
    #fsdb test
    a
    b
</pre>
<h3>Command:</h3>
<pre>
    cat data.fsdb | dbcolcopylast foo
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
