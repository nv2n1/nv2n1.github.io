---
title: "dbcolneaten(1)"
name: "dbcolneaten"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbcolneaten/"
description: "dbcolneaten – pretty-print columns of Fsdb data (assuming a monospaced font)"
---

<h2 class="name">NAME</h2>
<p> dbcolneaten &#8211; pretty-print columns of Fsdb data (assuming a monospaced font) </p>
<h2>SYNOPSIS</h2>
<p> dbcolneaten [-E] [field_settings]</p>
<h2>DESCRIPTION</h2>
<p> dbcolneaten arranges that the Fsdb data appears in neat columns if you view it with a monospaced font. To do this, it pads out each field with spaces to line up the next field. </p>
<p> Field settings are of the form </p>
<pre>
    field op value
</pre>
<p> <font SIZE="-1">OP</font> is &gt;=, =, or &lt;= specifying that the width of that <font SIZE="-1">FIELD</font> must be more, equal, or less than that <font SIZE="-1">VALUE</font> </p>
<p> dbcolneaten runs in <a href="/docs/linux/man/1-o/">O</a>(1) memory but disk space proportional to the size of data.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-E</code> or <code>&#8211;noeoln</code></p>
<dd> Omit padding for the last column (at the end-of-the-line). (Default behavior.)</p>
<dt><code>-e</code> or <code>&#8211;eoln</code></p>
<dd> Do padding and include an extra field separator after the last column. (Useful if you&#8217;re interactively adding a column.)</dl>
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
        #fsdb fullname homedir uid gid
        Mr._John_Heidemann_Junior       /home/johnh     2274    134
        Greg_Johnson    /home/greg      2275    134
        Root    /root   0       0
        # this is a simple database
        #   | dbcol fullname homedir uid gid
</pre>
<h3>Command:</h3>
<pre>
    dbcolneaten
</pre>
<h3>Output:</h3>
<pre>
        #fsdb -F s fullname       homedir     uid  gid
        Mr._John_Heidemann_Junior /home/johnh 2274 134
        Greg_Johnson              /home/greg  2275 134
        Root                      /root       0    0  
        # this is a simple database
        #   | dbcol fullname homedir uid gid
        #   | dbcolneaten
</pre>
<h2>BUGS</h2>
<p> Does not handle tab separators correctly.</p>
<h2>SEE ALSO</h2>
<p> Fsdb.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
