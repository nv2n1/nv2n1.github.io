---
title: "dbcolrename(1)"
name: "dbcolrename"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbcolrename/"
description: "dbcolrename – change the names of columns in a fsdb schema"
---

<h2 class="name">NAME</h2>
<p> dbcolrename &#8211; change the names of columns in a fsdb schema </p>
<h2>SYNOPSIS</h2>
<p> dbcolrename OldName1 NewName1 [OldName2 NewName2] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> Dbcolrename changes the names of columns in a fsdb schema, mapping OldName1 to NewName1, and so on for multiple pairs of column names. </p>
<p> Note that it is valid to do &#8220;overlapping&#8221; renames like <tt>&quot;dbcolrename a b b a&quot;</tt>.</p>
<h2>OPTIONS</h2>
<p> No non-standard options. </p>
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
    #fsdb account passwd uid gid fullname homedir shell
    johnh * 2274 134 John_Heidemann /home/johnh /bin/bash
    greg * 2275 134 Greg_Johnson /home/greg /bin/bash
    root * 0 0 Root /root /bin/bash
    # this is a simple database
</pre>
<h3>Command:</h3>
<pre>
    cat DATA/passwd.fsdb | dbcolrename fullname first_last
</pre>
<h3>Output:</h3>
<pre>
    #fsdb      account passwd  uid     gid     first_last      homedir shell
    johnh * 2274 134 John_Heidemann /home/johnh /bin/bash
    greg * 2275 134 Greg_Johnson /home/greg /bin/bash
    root * 0 0 Root /root /bin/bash
    # this is a simple database
    #  | dbcolrename fullname first_last
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
