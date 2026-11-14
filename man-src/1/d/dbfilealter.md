---
title: "dbfilealter(1)"
name: "dbfilealter"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbfilealter/"
description: "dbfilealter – alter the format of an Fsdb file, changing the row/column separator"
---

<h2 class="name">NAME</h2>
<p> dbfilealter &#8211; alter the format of an Fsdb file, changing the row/column separator </p>
<h2>SYNOPSIS</h2>
<p> dbfilealter [-c] [-F fs] [-R rs] [-Z compression] [column&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This program reformats a Fsdb file, altering the row (<tt>&quot;-R rs&quot;</tt>) or column (<tt>&quot;-F fs&quot;</tt>) separator. It verifies that this action does not violate the file constraints (for example, if spaces appear in data and the new format has space as a separator), and optionally corrects things. </p>
<p> With <tt>&quot;-Z compression&quot;</tt> it controls compression on the file</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-F</code> or <code>&#8211;fs</code> or <code>&#8211;fieldseparator</code> S</p>
<dd> Specify the field (column) separator as <tt>&quot;S&quot;</tt>. See below for valid field separators.</p>
<dt><code>-R</code> or <code>&#8211;rs</code> or <code>&#8211;rowseparator</code> S</p>
<dd> Specify the row separator as <tt>&quot;S&quot;</tt>. See below for valid row separators.</p>
<dt><code>-Z</code> or <code>&#8211;compression</code> S</p>
<dd> Specify file compression as given by file extension <tt>&quot;S&quot;</tt>. Supported compressions are <i>gz</i> for gzip, <i>bz2</i> for bzip2, <i>xz</i> for xz, or &#8220;none&#8221; or undef to disable compression. Default is none.</p>
<dt><code>-c</code> or <code>&#8211;correct</code></p>
<dd> Correct any inconsistency caused by the new separators, if possible.</dl>
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
<h3>Valid Field Separators</h3>
<dl>
<dt><code>D</code> default: any amount of whitespace on input, tabs on output.</p>
<dd>
<dt><code>s</code> single space (exactly one space for input and output).</p>
<dd>
<dt><code>S</code> double space on output; two or more spaces on input.</p>
<dd>
<dt><code>t</code> single tab character (exactly one tab for input and output).</p>
<dd>
<dt><font SIZE="-1"><code>XN</code></font> take <i>N</i> as one or more hex digits that specify a unicode character. Accept one or more of those characters on input, output exactly one of those characters.</p>
<dd>
<dt><font SIZE="-1"><code>CA</code></font> take <i>A</i> as a one (unicode) literal character. Accept one or more of those characters on input, output exactly one of those characters.</p>
<dd></dl>
<p> Potentially in the future <tt>&quot;xN&quot;</tt> and <tt>&quot;cA&quot;</tt> will support single-character-on-input equivalents of <tt>&quot;XN&quot;</tt> and &lt;<font SIZE="-1">CA</font>&gt;.</p>
<h3>Valid Row Seperators</h3>
<p> Three row separators are allowed:</p>
<dl>
<dt><code>D</code> the default, one line per row</p>
<dd>
<dt><code>C</code> complete rowized. Each line is a field-labeled and its value, and a blank line separates &quot;rows&quot;. All fields present in the output.</p>
<dd>
<dt><code>I</code> incompletely rowized. Like &quot;C&quot;, but null fields are omitted from the output.</p>
<dd></dl>
<h2>SAMPLE USAGE</h2>
<h3>Input:</h3>
<pre>
    #fsdb name id test1
    a 1 80
    b 2 70
    c 3 65
</pre>
<h3>Command:</h3>
<pre>
    cat data.fsdb | dbfilealter -F S
</pre>
<h3>Output:</h3>
<pre>
    #fsdb -F S name id test1
    a  1  80
    b  2  70
    c  3  65
    #  | dbfilealter -F S
</pre>
<h3>Command 2:</h3>
<pre>
    cat data.fsdb | dbfilealter -R C
</pre>
<h3>Output:</h3>
<pre>
    #fsdb -R C name id test1
    name: a
    id: 1
    test1: 80
    
    name: b
    id: 2
    test1: 70
    
    name: c
    id: 3
    test1: 65
    
    #   | dbfilealter -R C
</pre>
<h3>Correction mode input:</h3>
<pre>
    #fsdb -F S name id test1
    a student  1  80
    b nice  2  70
    c all  3  65
</pre>
<h3>Correction mode command:</h3>
<pre>
    cat correction.fsdb | dbfilealter -c -F D
</pre>
<h3>Correction mode output:</h3>
<pre>
    #fsdb name id test1
    a_student   1       80
    b_nice      2       70
    c_all       3       65
    #   | dbfilealter -c -F D
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb, dbcoldefine.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 2008-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
