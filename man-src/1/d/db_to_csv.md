---

title: "db_to_csv(1)"
name: "db_to_csv"
section: "1"
letter: "d"
url: "/docs/linux/man/1-db_to_csv/"
description: "db_to_csv – convert fsdb to the comma-separated-value file-format"
---

<p> db_to_csv &#8211; convert fsdb to the comma-separated-value file-format </p>
<h2>SYNOPSIS</h2>
<pre>
    db_to_csv [-C]
</pre>
<h2>DESCRIPTION</h2>
<p> Covert an existing fsdb file to comma-separated value format. </p>
<p> Input is fsdb format. </p>
<p> Output is CSV-format plain text (<i>not</i> fsdb).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-C</code> or &lt;&#8211;omit-comments&gt;</dt>
<dd> Also strip all comments.</dd></dl>
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
        #fsdb -F S paper papertitle reviewer reviewername score1 score2 score3 score4 score5
        1  test, paper  2  Smith  4  4  -  -  -
        2  other paper  3  Jones  3  3  -  -  -
        2  input double space  3  Jones  3  3  -  -  -
        #  | csv_to_db
</pre>
<h3>Command:</h3>
<pre>
    cat data.fsdb | db_to_csv
</pre>
<h3>Output:</h3>
<pre>
        paper,papertitle,reviewer,reviewername,score1,score2,score3,score4,score5
        1,&quot;test, paper&quot;,2,Smith,4,4,-,-,-
        2,&quot;other paper&quot;,3,Jones,3,3,-,-,-
        2,&quot;input double space&quot;,3,Jones,3,3,-,-,-
        #  | csv_to_db 
        #  | db_to_csv
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb. dbfilealter. csv_to_db</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2008 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
