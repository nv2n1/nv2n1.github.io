---
title: "dbrowenumerate(1)"
name: "dbrowenumerate"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbrowenumerate/"
description: "dbrowenumerate – enumerate rows, starting from zero"
---

<h2 class="name">NAME</h2>
<p> dbrowenumerate &#8211; enumerate rows, starting from zero </p>
<h2>SYNOPSIS</h2>
<p> dbrowenumerate</p>
<h2>DESCRIPTION</h2>
<p> Add a new column &#8220;count&#8221;, incremented for each row of data, starting with zero. Use dbrowaccumulate for control over initial value or increment; this module is just a wrapper around that.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-N</code> or <code>&#8211;new-name</code> N</p>
<dd> Name the new column N. Defaults to <tt>&quot;count&quot;</tt>.</dl>
<p> This module also supports the standard jdb options:</p>
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
    #h account passwd uid gid fullname homedir shell
    johnh * 2274 134 John_Heidemann /home/johnh /bin/bash
    greg * 2275 134 Greg_Johnson /home/greg /bin/bash
    root * 0 0 Root /root /bin/bash
    # this is a simple database
</pre>
<h3>Command:</h3>
<pre>
    cat DATA/passwd.jdb | dbrowenumerate
</pre>
<h3>Output:</h3>
<pre>
    #h account passwd uid  gid fullname       homedir     shell     count 
    johnh      *      2274 134 John_Heidemann /home/johnh /bin/bash 0     
    greg       *      2275 134 Greg_Johnson   /home/greg  /bin/bash 1     
    root       *      0    0   Root           /root       /bin/bash 2     
    # this is a simple database
    #  | /home/johnh/BIN/DB/dbrowenumerate
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb, dbrowaccumulate.</p>
<h2>CLASS FUNCTIONS</h2>
<h2>Index</h2>
