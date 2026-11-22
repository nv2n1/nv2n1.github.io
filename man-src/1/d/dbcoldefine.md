---

title: "dbcoldefine(1)"
name: "dbcoldefine"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbcoldefine/"
description: "dbcoldefine – define the columns of a plain text file to make it an Fsdb file"
---

<p> dbcoldefine &#8211; define the columns of a plain text file to make it an Fsdb file </p>
<h2>SYNOPSIS</h2>
<p> dbcoldefine [-F x] [column&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This program writes a new header before the data with the specified column names. It does <i>not</i> do any validation of the data contents; it is up to the user to verify that, other than the header, the input datastream is a correctly formatted Fsdb file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-F</code> or <code>&#8211;fs</code> or <code>&#8211;fieldseparator</code> s</dt>
<dd> Specify the field separator.</dd>
<dt><code>&#8211;header</code> H</dt>
<dd> Give the columns and field separator as a full Fsdb header (including <tt>&quot;#fsdb&quot;</tt>). Can only be used alone, not with other specifications.</dd></dl>
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
    102400      4937974.964736
    102400      4585247.875904
    102400      5098141.207123
</pre>
<h3>Command:</h3>
<pre>
    cat DATA/http_bandwidth | dbcoldefine size bw
</pre>
<h3>Output:</h3>
<pre>
    #fsdb size bw
    102400      4937974.964736
    102400      4585247.875904
    102400      5098141.207123
    # | dbcoldefine size bw
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb. dbfilestripcomments</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2016 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the GNU general public license, version 2. See the file COPYING with the distribution for details. </p>
