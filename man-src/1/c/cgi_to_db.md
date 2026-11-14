---
title: "cgi_to_db(1)"
name: "cgi_to_db"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cgi_to_db/"
description: "cgi_to_db – convert stored CGI files (from CGI.pm) to fsdb"
---

<h2 class="name">NAME</h2>
<p> cgi_to_db &#8211; convert stored CGI files (from CGI.pm) to fsdb </p>
<h2>SYNOPSIS</h2>
<pre><code>
cgi_to_db[-duU][-e EmptyValue][cgi - files...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Converts all stored <font SIZE="-1">CGI</font> files (from <font SIZE="-1">CGI</font>.pm) to fsdb, optionally unescaping the contents. When contents are unescaped, <font SIZE="-1">CR NL</font> is recoded as &#8220;
&#8221;. </p>
<p> Output is always in fsdb list format with double space (type &#8220;S&#8221;) field separator. </p>
<p> Unlike most Fsdb programs, the input to this program is <i>not</i> usually from standard input. However, the program will take <tt>&quot;-i&quot;</tt> options. </p>
<p> This program requires temporary storage equal to the size of the data (so that it can handle the case of different entries having different headers).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-u</code> or <code>&#8211;unescape</code></p>
<dd> do unescape data, converting <font SIZE="-1">CGI</font> escape codes like <tt>%xx</tt> to regular characters (default)</p>
<dt><code>-U</code> or <code>&#8211;nounescape</code></p>
<dd> do <i>not</i> unescape data, but leave it CGI-encoded</p>
<dt><code>-e E</code> or <code>&#8211;empty E</code></p>
<dd> give value E as the value for empty (null) records</p>
<dt><code>-T TmpDir</code></p>
<dd> where to put tmp files. Also uses environment variable <font SIZE="-1">TMPDIR,</font> if -T is not specified. Default is /tmp.</dl>
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
<p> file A (TEST/cgi_to_db_ex.in): </p>
<pre>
    name=test
    id=111-11-1111
    email=test%40usc.edu
    submit_time=Tue%20Jan%2014%2011%3A32%3A39%202003
    =
</pre>
<p> file B (TEST/cgi_to_db_ex.in-2): </p>
<pre>
    name=test2
    id=222-22-2222
    email=test2%40usc.edu
    newfield=foo
    emptyfield=
    submit_time=Tue%20Jan%2024%2022%3A32%3A39%202003
    =
</pre>
<h3>Command:</h3>
<pre>
    cgi_to_db TEST/cgi_to_db_ex.in TEST/cgi_to_db_ex.in-2
</pre>
<h3>Output:</h3>
<pre>
    #fsdb -R C -F S name id email submit_time newfield emptyfield
    name:  test
    id:  111-11-1111
    email:  test\@usc.edu
    submit_time:  Tue Jan 14 11:32:39 2003
    name:  test2
    id:  222-22-2222
    email:  test2\@usc.edu
    newfield:  foo
    emptyfield:  -
    submit_time:  Tue Jan 24 22:32:39 2003
    #  | cgi_to_db TEST/cgi_to_db_ex.in TEST/cgi_to_db_ex.in-2
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb. <font SIZE="-1"><i><a href="//www.systutorials.com/docs/linux/man/3pm-CGI/">CGI</a></i></font><i></i>(3pm). &lt;<a rel="nofollow" href="http://stein.cshl.org/boulder/">http://stein.cshl.org/boulder/</a>&gt;. &lt;<a rel="nofollow" href="http://stein.cshl.org/WWW/software/CGI/">http://stein.cshl.org/WWW/software/CGI/</a>&gt;</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2008 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
