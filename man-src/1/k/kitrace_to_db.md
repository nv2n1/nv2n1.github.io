---
title: "kitrace_to_db(1)"
name: "kitrace_to_db"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kitrace_to_db/"
description: "kitrace_to_db – convert kitrace output to Fsdb format"
---

<h2 class="name">NAME</h2>
<p> kitrace_to_db &#8211; convert kitrace output to Fsdb format </p>
<h2>SYNOPSIS</h2>
<pre><code>
kitrace_to_db[-Y year][registers]&lt;kitrace.out&gt; kitrace.fsdb
</code></pre>
<h2>DESCRIPTION</h2>
<p> Converts a kitrace data stream to Fsdb format. </p>
<p> Optional arguments list registers which will be picked out of the output stream and formatted as their own columns.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-Y Y</code> or <code>&#8211;year Y</code></p>
<dd> Specify the 4-digit year for the dataset (defaults to current year).</p>
<dt><code>-u</code> or <code>&#8211;utc</code></p>
<dd> Specify <font SIZE="-1">UTC</font> timezone (defaults to local time zeon).</dl>
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
    _null_getpage+4  Nov  7 22:40:13.281070 (            ) pid 4893
    _null_getpage+128 Nov  7 22:40:13.281756 (   00.000686) pid 4893
    _null_getpage+4  Nov  7 22:40:13.282694 (   00.000938) pid 4893
    _null_getpage+128 Nov  7 22:40:13.328709 (   00.046015) pid 4893
    _null_getpage+4  Nov  7 22:40:13.330758 (   00.002049) pid 4893
    _null_getpage+128 Nov  7 22:40:13.353830 (   00.023072) pid 4893
    _null_getpage+4  Nov  7 22:40:13.355566 (   00.001736) pid 4893
    _null_getpage+128 Nov  7 22:40:13.357169 (   00.001603) pid 4893
    _null_getpage+4  Nov  7 22:40:13.358780 (   00.001611) pid 4893
    _null_getpage+128 Nov  7 22:40:13.375844 (   00.017064) pid 4893
    _null_getpage+4  Nov  7 22:40:13.377850 (   00.002006) pid 4893
    _null_getpage+128 Nov  7 22:40:13.378358 (   00.000508) pid 4893
</pre>
<h3>Command:</h3>
<pre>
    kitrace_to_db -Y 1995
</pre>
<h3>Output:</h3>
<pre>
    #fsdb event clock diff
    _null_getpage+4  815812813.281070      0.0
    _null_getpage+128  815812813.281756  00.000686
    _null_getpage+4  815812813.282694  00.000938
    _null_getpage+128  815812813.328709  00.046015
    _null_getpage+4  815812813.330758  00.002049
    _null_getpage+128  815812813.353830  00.023072
    _null_getpage+4  815812813.355566  00.001736
    _null_getpage+128  815812813.357169  00.001603
    _null_getpage+4  815812813.358780  00.001611
    _null_getpage+128  815812813.375844  00.017064
    _null_getpage+4  815812813.377850  00.002006
    _null_getpage+128  815812813.378358  00.000508
    # | kitrace_to_db
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2011 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
