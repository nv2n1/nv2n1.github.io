---
title: "dbrow(1)"
name: "dbrow"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbrow/"
description: "dbrow – select rows from an Fsdb file based on arbitrary conditions"
---

<h2 class="name">NAME</h2>
<p> dbrow &#8211; select rows from an Fsdb file based on arbitrary conditions </p>
<h2>SYNOPSIS</h2>
<p> dbrow [-vw] <font SIZE="-1">CONDITION</font> [<font SIZE="-1">CONDITION&#8230;</font>]</p>
<h2>DESCRIPTION</h2>
<p> Select rows for which all <font SIZE="-1">CONDITIONS</font> are true. Conditions are specified as Perl code, in which column names are be embedded, preceded by underscores.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></dt>
<dd> Invert the selection, picking rows where at least one condition does <i>not</i> match.</dd></dl>
<p> This module also supports the standard fsdb options:</p>
<dl>
<dt><code>-d</code></dt>
<dd> Enable debugging output.</dd>
<dt><code>-w</code> or <code>&#8211;warnings</code></dt>
<dd> Enable warnings in user supplied code.</dd>
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
    #fsdb account passwd uid gid fullname homedir shell
    johnh * 2274 134 John_Heidemann /home/johnh /bin/bash
    greg * 2275 134 Greg_Johnson /home/greg /bin/bash
    root * 0 0 Root /root /bin/bash
    # this is a simple database
</pre>
<h3>Command:</h3>
<pre>
    cat DATA/passwd.fsdb | dbrow '_fullname =~ /John/'
</pre>
<h3>Output:</h3>
<pre>
    #fsdb      account passwd  uid     gid     fullname        homedir shell
    johnh   *       2274    134     John_Heidemann  /home/johnh     /bin/bash
    greg    *       2275    134     Greg_Johnson    /home/greg      /bin/bash
    # this is a simple database
    #  | /home/johnh/BIN/DB/dbrow
</pre>
<h2>BUGS</h2>
<p> Doesn&#8217;t detect references to unknown columns in conditions. </p>
<p> <font SIZE="-1">END<br />
</font>&nbsp;<wbr>#&#8217;&nbsp;<wbr>for font-lock mode.<br />
&nbsp;<wbr>exit 1;</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2007 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
