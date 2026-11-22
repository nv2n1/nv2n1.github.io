---

title: "xml_to_db(1)"
name: "xml_to_db"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xml_to_db/"
description: "xml_to_db – convert a subset of XML into fsdb"
---

<p> xml_to_db &#8211; convert a subset of XML into fsdb </p>
<h2>SYNOPSIS</h2>
<pre>
    xml_to_db -k EntityField &lt;source.xml
</pre>
<h2>DESCRIPTION</h2>
<p> Converts a <i>very limited</i> subset of XML into Fsdb format. </p>
<p> The input is XML-format (<i>not</i> fsdb). The input is parsed as XML, and each entity of type ENTITYFIELD is extracted as a row. ENTITYFIELD can have mutliple components separated by slashes to walk down the XML tree, if necessary. </p>
<p> The input XML file is assumed to be <i>very simple</i>. All rows are assumed to be sequential in one entity. Any other than the specified ENTITYFIELD are ignored. The schema is assumed to be defined by the first instances of that field. </p>
<p> The output is two-space-separated fsdb. (Someday more general field separators should be supported.) Fsdb fields are normalized version of the CSV file: spaces are converted to single underscores.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-e</code> EmptyValue or <code>&#8211;empty</code></dt>
<dd> Specify the value newly created columns get.</dd></dl>
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
        &lt;?xml version='1.0' standalone='yes'?&gt;
        &lt;gnuPod&gt;
         &lt;files&gt;
          &lt;file addtime=&quot;3389919728&quot; album=&quot;Born to Pick&quot; artist=&quot;7th Day Buskers&quot; title=&quot;Loch Lamor&quot; /&gt;
          &lt;file addtime=&quot;3389919728&quot; album=&quot;Born to Pick&quot; artist=&quot;7th Day Buskers&quot; title=&quot;The Floods&quot; /&gt;
          &lt;file addtime=&quot;3389919735&quot; album=&quot;Copland Conducts Copland&quot; artist=&quot;Aaron Copland&quot; title=&quot;Our Town&quot; /&gt;
         &lt;/files&gt;
         &lt;playlist name=&quot;new shows&quot; plid=&quot;97241&quot; &gt;
           &lt;regex artist=&quot;^(Le Show|This American Life)$&quot; /&gt;
         &lt;/playlist&gt;
        &lt;/gnuPod&gt;
</pre>
<h3>Command:</h3>
<pre>
        xml_to_db -k files/file &lt;gnupod.xml
</pre>
<h3>Output:</h3>
<pre>
        #fsdb -F S addtime album artist title
        3389919728  Born to Pick  7th Day Buskers  Loch Lamor
        3389919728  Born to Pick  7th Day Buskers  The Floods
        3389919735  Copland Conducts Copland  Aaron Copland  Our Town
        #   | xml_to_db -k files/file
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 2011-2015 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the GNU general public license, version 2. See the file COPYING with the distribution for details. </p>
