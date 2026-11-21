---

title: "cgi_to_db(1)"
name: "cgi_to_db"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cgi_to_db/"
description: "cgi_to_db – convert stored CGI files (from CGI.pm) to fsdb"
---

<pre><code>
cgi_to_db[-duU][-e EmptyValue][cgi - files...]
</code></pre>
<p> Converts all stored <font SIZE="-1">CGI</font> files (from <font SIZE="-1">CGI</font>.pm) to fsdb, optionally unescaping the contents. When contents are unescaped, <font SIZE="-1">CR NL</font> is recoded as &#8220;
&#8221;. </p>
<p> Output is always in fsdb list format with double space (type &#8220;S&#8221;) field separator. </p>
<p> Unlike most Fsdb programs, the input to this program is <i>not</i> usually from standard input. However, the program will take <tt>&quot;-i&quot;</tt> options. </p>
<p> This program requires temporary storage equal to the size of the data (so that it can handle the case of different entries having different headers).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-u</code> or <code>&#8211;unescape</code></dt>
<dd> do unescape data, converting <font SIZE="-1">CGI</font> escape codes like <tt>%xx</tt> to regular characters (default)</dd>
<dt><code>-U</code> or <code>&#8211;nounescape</code></dt>
<dd> do <i>not</i> unescape data, but leave it CGI-encoded</dd>
<dt><code>-e E</code> or <code>&#8211;empty E</code></dt>
<dd> give value E as the value for empty (null) records</dd>
<dt><code>-T TmpDir</code></dt>
<dd> where to put tmp files. Also uses environment variable <font SIZE="-1">TMPDIR,</font> if -T is not specified. Default is /tmp.</dd></dl>
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
<p> Fsdb. <font SIZE="-1"><i>CGI</i></font><i></i>(3pm). &lt;<a rel="nofollow" href="http://stein.cshl.org/boulder/">http://stein.cshl.org/boulder/</a>&gt;. &lt;<a rel="nofollow" href="http://stein.cshl.org/WWW/software/CGI/">http://stein.cshl.org/WWW/software/CGI/</a>&gt;</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2008 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
