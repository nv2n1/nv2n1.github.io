---
title: "dbfilestripcomments(1)"
name: "dbfilestripcomments"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbfilestripcomments/"
description: "dbfilestripcomments – remove comments from a fsdb file"
---

<h2>SYNOPSIS</h2>
<p> dbfilestripcomments [-h]</p>
<h2>DESCRIPTION</h2>
<p> Remove any comments in a file, including the header. This makes the file unreadable by other Fsdb utilities, but perhaps more readable by humans. </p>
<p> With the -h option, leave the header.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code> or <code>&#8211;header</code></dt>
<dd> Retain the header.</dd></dl>
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
    #fsdb -R C      experiment      mean    stddev  pct_rsd conf_range      conf_low       conf_high        conf_pct        sum     sum_squared     min     max     n
    experiment:  ufs_mab_sys
    mean:        37.25
    stddev:      0.070711
    pct_rsd:     0.18983
    conf_range:  0.6353
    conf_low:    36.615
    conf_high:   37.885
    conf_pct:    0.95
    sum:         74.5
    sum_squared: 2775.1
    min:         37.2
    max:         37.3
    n:           2
    #  | /home/johnh/BIN/DB/dbmultistats experiment duration
    #  | /home/johnh/BIN/DB/dblistize
</pre>
<h3>Command:</h3>
<pre>
    cat data.fsdb | dbfilestripcomments
</pre>
<h3>Output:</h3>
<pre>
    experiment:  ufs_mab_sys
    mean:        37.25
    stddev:      0.070711
    pct_rsd:     0.18983
    conf_range:  0.6353
    conf_low:    36.615
    conf_high:   37.885
    conf_pct:    0.95
    sum:         74.5
    sum_squared: 2775.1
    min:         37.2
    max:         37.3
    n:           2
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb. dbcoldefine.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2008 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
