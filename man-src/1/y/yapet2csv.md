---
title: "yapet2csv(1)"
name: "yapet2csv"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yapet2csv/"
description: "yapet2csv – convert YAPET file to CSV file"
---

<h2 class="name">NAME</h2>
<p> yapet2csv &#8211; convert YAPET file to CSV file </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>yapet2csv</code> [[<code>-c</code>] | [<code>-h</code>] | [<code>-V</code>]] [<code>-H</code>] [<code>-p</code>&nbsp;<wbr>{<i>password</i>}] [<code>-q</code>] [<code>-s</code>&nbsp;<wbr>{<i>separator</i>}] {<i>src</i>} {<i>dst</i>}</dl>
<h2>DESCRIPTION</h2>
<dd>Convert a YAPET file to a CSV file. The source file specified by <i>src</i> will not be modified. </p>
<p> The resulting CSV file <i>dst</i> has the format as shown in Table 1, &#8220;CSV file format&#8221;. </p>
<p> <code>Table 1. CSV file format</code> </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td ALIGN=center><code> Column # </code></td>
<td><code> YAPET record field </code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> 1 </td>
<td> Record Name
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> 2 </td>
<td> Host Name
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> 3 </td>
<td> User Name
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> 4 </td>
<td> Password
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> 5 </td>
<td> Comment
</td>
</tr>
</table>
<h2>OPTIONS</h2>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> Show help.</dl>
<p> <code>-c</code></p>
<dl>
<dt>
<dd> Show copyright.</dl>
<p> <code>-V</code></p>
<dl>
<dt>
<dd> Show version.</dl>
<p> <code>-H</code></p>
<dl>
<dt>
<dd> Add header line to CSV file.</dl>
<p> <code>-p</code></p>
<dl>
<dt>
<dd> Use the master password <i>password</i> provided to decrypt <i>src</i>. The use of this option is not recommended for security reasons. </p>
<p> By default, <code>yapet2csv</code> prompts for the master password.</dl>
<p> <code>-q</code></p>
<dl>
<dt>
<dd> Do not produce verbose output, except for error messages. By default, <code>yapet2csv</code> will print a period for each converted password record to stdout.</dl>
<h2>OPERANDS</h2>
<p> <i>src</i></p>
<dl>
<dt>
<dd> Source YAPET pathname which will be converted to CSV and stored in <i>dst</i>. If the file path does not end in .pet, <code>yapet2csv</code> will append .pet to the operand.</dl>
<p> <i>dst</i></p>
<dl>
<dt>
<dd> Pathname where the converted YAPET file will be stored. The file must not exist prior to invoking <code>yapet2csv</code>. Refer to Table 1, &#8220;CSV file format&#8221; for the format of the resulting CSV file <i>dst</i>.</dl>
<h2>EXAMPLES</h2>
<p> <code>Example 1. Prompt for Master Password</code> </p>
<p> Convert the YAPET file /tmp/foo.pet to a CSV file /tmp/bar.csv. Master password used to decrypt foo.pet will be prompted for: </p>
<dl>
<dt>
<dd>
<pre>
        $ yapet2csv /tmp/foo.pet /tmp/bar.csv
      
</pre>
</dl>
<p> <code>Example 2. Provide Master Password on command line</code> </p>
<p> Convert the YAPET file /tmp/foo2.pet to a CSV file /tmp/bar2.csv. Master password <code>secret</code> used to decrypt foo2.pet is provided on command line: </p>
<dl>
<dt>
<dd>
<pre>
        $ yapet2csv -p secret /tmp/foo2.pet /tmp/bar2.csv
      
</pre>
</dl>
<h2>EXIT STATUS</h2>
<p> 0</p>
<dl>
<dt>
<dd> Successful completion.</dl>
<p> 1</p>
<dl>
<dt>
<dd> Error while parsing command line arguments.</dl>
<p> 2</p>
<dl>
<dt>
<dd> File <i>dst</i> already exists.</dl>
<p> 3</p>
<dl>
<dt>
<dd> An error occurred.</dl>
<h2>BUGS</h2>
<p> Please report bugs to m[blue]<code><a rel="nofollow" href="http://bugs.guengel.ch/">http://bugs.guengel.ch/</a></code>m[].</p>
<h2>AUTHOR</h2>
<p> Rafael Ostertag rafi [at] guengel.ch</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-yapet/">yapet</a></code>(1), <code><a href="/docs/linux/man/1-csv2yapet/">csv2yapet</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2008, 2009, 2010, 2011, 2013, 2014 Rafael Ostertag &lt;rafi [at] guengel.ch&gt; </p>
<h2>Index</h2>
