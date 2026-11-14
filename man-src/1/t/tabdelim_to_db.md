---
title: "tabdelim_to_db(1)"
name: "tabdelim_to_db"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tabdelim_to_db/"
description: "tabdelim_to_db – convert tab-delimited data into fsdb"
---

<h2 class="name">NAME</h2>
<p> tabdelim_to_db &#8211; convert tab-delimited data into fsdb </p>
<h2>SYNOPSIS</h2>
<pre>
    tabdelim_to_db &lt;source.tabdelim &gt;target.fsdb
</pre>
<h2>DESCRIPTION</h2>
<p> Converts a tab-delimited data stream to Fsdb format. </p>
<p> The input is tab-delimited (<i>not</i> fsdb): the first row is taken to be the names of the columns; tabs separate columns. </p>
<p> The output is a fsdb file with a proper header and a tab field-separator. </p>
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
<pre><code>
name email test1
    Tommy Trojan tt[at] usc.edu 80 Joe Bruin joeb[at] ucla.edu 85 J.Random jr[at] caltech.edu 90
</code></pre>
<h3>Command:</h3>
<pre>
    tabdelim_to_db
</pre>
<h3>Output:</h3>
<pre><code>
#fsdb - Ft name email test1
Tommy Trojan tt[at] usc.edu 80 Joe Bruin joeb[at] ucla.edu 85 J.Random jr[at] caltech.edu 90
#| dbcoldefine name email test1
</code></pre>
<h2>SEE ALSO</h2>
<p> Fsdb.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2008 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
