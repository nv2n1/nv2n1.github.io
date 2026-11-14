---
title: "db_to_html_table(1)"
name: "db_to_html_table"
section: "1"
letter: "d"
url: "/docs/linux/man/1-db_to_html_table/"
description: "db_to_html_table – convert db to an HTML table"
---

<h2 class="name">NAME</h2>
<p> db_to_html_table &#8211; convert db to an HTML table </p>
<h2>SYNOPSIS</h2>
<pre>
    db_to_html_table [-g N] &lt;source.fsdb &gt;dest.html
</pre>
<h2>DESCRIPTION</h2>
<p> Covert an existing dbtable to an <font SIZE="-1">HTML</font> table. The output is a fragment of an <font SIZE="-1">HTML</font> page; we assume the user fills in the rest (head and body, etc.). </p>
<p> Input is fsdb format. </p>
<p> Output is <font SIZE="-1">HTML</font> code (<i>not</i> fsdb), with HTML-specific characters (less than, greater than, ampersand) are escaped. (The fsdb-1.x version assumed input was <font SIZE="-1">ISO-8859-1</font>; we now assume both input and output are unicode. This change is considered a feature of the 21st century.)</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-g N</code> or &lt;&#8211;group-count N&gt;</p>
<dd> Color groups of <i>N</i> consecutive rows with one background color.</dl>
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
        #fsdb -F S account passwd uid gid fullname homedir shell
        johnh  *  2274  134  John &amp; Ampersand  /home/johnh  /bin/bash
        greg  *  2275  134  Greg &lt; Lessthan  /home/greg  /bin/bash
        root  *  0  0  Root ; Semi  /root  /bin/bash
        four  *  1  1  Fourth Row  /home/four  /bin/bash
</pre>
<h3>Command:</h3>
<pre>
    cat data.fsdb | db_to_csv -g 3
</pre>
<h3>Output:</h3>
<pre>
        &lt;table&gt;
        &lt;tr&gt;&lt;th&gt;account&lt;/th&gt; &lt;th&gt;passwd&lt;/th&gt; &lt;th&gt;uid&lt;/th&gt; &lt;th&gt;gid&lt;/th&gt; &lt;th&gt;fullname&lt;/th&gt; &lt;th&gt;homedir&lt;/th&gt; &lt;th&gt;shell&lt;/th&gt; &lt;/tr&gt;
        &lt;tr bgcolor=&quot;#f0f0f0&quot;&gt;&lt;td&gt;johnh&lt;/td&gt; &lt;td&gt;*&lt;/td&gt; &lt;td&gt;2274&lt;/td&gt; &lt;td&gt;134&lt;/td&gt; &lt;td&gt;John &amp;amp; Ampersand&lt;/td&gt; &lt;td&gt;/home/johnh&lt;/td&gt; &lt;td&gt;/bin/bash&lt;/td&gt; &lt;/tr&gt;
        &lt;tr bgcolor=&quot;#f0f0f0&quot;&gt;&lt;td&gt;greg&lt;/td&gt; &lt;td&gt;*&lt;/td&gt; &lt;td&gt;2275&lt;/td&gt; &lt;td&gt;134&lt;/td&gt; &lt;td&gt;Greg &amp;lt; Lessthan&lt;/td&gt; &lt;td&gt;/home/greg&lt;/td&gt; &lt;td&gt;/bin/bash&lt;/td&gt; &lt;/tr&gt;
        &lt;tr bgcolor=&quot;#f0f0f0&quot;&gt;&lt;td&gt;root&lt;/td&gt; &lt;td&gt;*&lt;/td&gt; &lt;td&gt;0&lt;/td&gt; &lt;td&gt;0&lt;/td&gt; &lt;td&gt;Root ; Semi&lt;/td&gt; &lt;td&gt;/root&lt;/td&gt; &lt;td&gt;/bin/bash&lt;/td&gt; &lt;/tr&gt;
        &lt;tr bgcolor=&quot;#d0d0d0&quot;&gt;&lt;td&gt;four&lt;/td&gt; &lt;td&gt;*&lt;/td&gt; &lt;td&gt;1&lt;/td&gt; &lt;td&gt;1&lt;/td&gt; &lt;td&gt;Fourth Row&lt;/td&gt; &lt;td&gt;/home/four&lt;/td&gt; &lt;td&gt;/bin/bash&lt;/td&gt; &lt;/tr&gt;
        &lt;/table&gt;
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb. dbcolneaten. dbfileadjust. html_table_to_db.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 2007-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
