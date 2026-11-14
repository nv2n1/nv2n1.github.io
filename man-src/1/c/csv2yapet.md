---
title: "csv2yapet(1)"
name: "csv2yapet"
section: "1"
letter: "c"
url: "/docs/linux/man/1-csv2yapet/"
description: "csv2yapet – convert CSV file to YAPET file"
---

<h2 class="name">NAME</h2>
<p> csv2yapet &#8211; convert CSV file to YAPET file </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>csv2yapet</code> [[<code>-c</code>] | [<code>-h</code>] | [<code>-V</code>]] [<code>-p</code>&nbsp;<wbr>{<i>password</i>}] [<code>-q</code>] [<code>-s</code>&nbsp;<wbr>{<i>separator</i>}] {<i>src</i>} {<i>dst</i>}</dl>
<h2>DESCRIPTION</h2>
<dd>Convert a CSV file <i>src</i> to an YAPET file <i>dst</i>. The default character for delimiting the fields is &#8216;,&#8217; (comma) unless specified otherwise on the command line by providing the <code>-s</code> option (refer to the section called &#8220;OPTIONS&#8221;). </p>
<p> Fields containing the field separator character have to be enclosed in double quotes (&quot;). </p>
<p> In order to convert a double quote character it has to be preceded by another double quote character (see the section called &#8220;EXAMPLES&#8221;). </p>
<p> The following table describes the fields of the source CSV file as expected by <code>csv2yapet</code>: </p>
<p> <code>Table 1. Source file format</code> </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td ALIGN=center><code> Column # </code></td>
<td><code> YAPET Record Field </code></td>
<td><code> Maximum size in bytes </code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> 1 </td>
<td> Record Name </td>
<td> 127
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> 2 </td>
<td> Host Name </td>
<td> 255
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> 3 </td>
<td> User Name </td>
<td> 255
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> 4 </td>
<td> Password </td>
<td> 255
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center> 5 </td>
<td> Comment </td>
<td> 511
</td>
</tr>
</table>
<p> See the section called &#8220;EXAMPLES&#8221; for an example CSV file.</p>
<h2>OPTIONS</h2>
<p> The following options are supported: </p>
<p> <code>-c</code></p>
<dl>
<dt>
<dd> Show copyright.</dl>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> Show help.</dl>
<p> <code>-V</code></p>
<dl>
<dt>
<dd> Show version.</dl>
<p> <code>-p</code> <i>password</i></p>
<dl>
<dt>
<dd> The password to be used to encrypt the YAPET file. If <code>csv2yapet</code> is invoked without this option, it will prompt for the password on the standard input.</dl>
<p> <code>-q</code></p>
<dl>
<dt>
<dd> Enable the quiet mode. No details about errors are reported.</dl>
<p> <code>-s</code> <i>separator</i></p>
<dl>
<dt>
<dd> Change the default field separator &#8216;,&#8217; (comma) to the single character <i>separator</i>.</dl>
<h2>OPERANDS</h2>
<p> The following operands are required: </p>
<p> <i>src</i></p>
<dl>
<dt>
<dd> The source CSV file to be converted. It must be of the format described in Table 1, &#8220;Source file format&#8221;.</dl>
<p> <i>dst</i></p>
<dl>
<dt>
<dd> The resulting YAPET file holding the content of <i>src</i> encrypted. This file must not exist prior to the conversion process, else <code>csv2yapet</code> will not start the conversion and abort.</dl>
<h2>EXAMPLES</h2>
<p> <code>Example 1. An example of a CSV file accepted by csv2yapet.</code> </p>
<p> The following example shows an excerpt of a CSV file as accepted for conversion by <code>csv2yapet</code>. </p>
<p> As the second line shows, fields can be blank but the separator may not be omitted. </p>
<dl>
<dt>
<dd>
<pre>
ssh host,host.example.org,johndoe,secret,Linux machine
mail account,imap.email.org,john_doe,secret,
...
</pre>
</dl>
<p> <code>Example 2. An example of a CSV file accepted by csv2yapet using double quotes.</code> </p>
<p> The following example shows an excerpt of a CSV file as accepted for conversion by <code>csv2yapet</code>. </p>
<p> The first line demonstrates how to double quote fields containing the separator character. The second line shows how to literally convert double quote characters. </p>
<dl>
<dt>
<dd>
<pre>
&quot;ssh, ftp, and http server&quot;,server.example.org,johndoe,secret,Linux machine
mail account,imap.email.org,john_doe,secret,&quot;John &quot;&quot;the Unknown&quot;&quot; Doe&quot;
...
</pre>
</dl>
<p> <code>Example 3. Invoking csv2yapet.</code> </p>
<p> The following example shows how to invoke <code>csv2yapet</code> in order to convert a CSV file to an YAPET file. If the <code>-s</code> option is not given, <code>csv2yapet</code> will ask for a password as shown: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>csv2yapet</code> passwords.csv passwords.pet
Please enter the password for passwords.pet:
Please re-type the password:
passwords.pet successfully created.
$
</pre>
</dl>
<h2>EXIT STATUS</h2>
<p> 0</p>
<dl>
<dt>
<dd> No error.</dl>
<p> 1</p>
<dl>
<dt>
<dd> Error while parsing command line argument.</dl>
<p> 2</p>
<dl>
<dt>
<dd> The passwords provided on the standard input do not match.</dl>
<p> 3</p>
<dl>
<dt>
<dd> The destination file <i>dst</i> already exists.</dl>
<p> 4</p>
<dl>
<dt>
<dd> An unexpected error occurred.</dl>
<h2>BUGS</h2>
<p> Please report bugs to m[blue]<code><a rel="nofollow" href="http://bugs.guengel.ch/">http://bugs.guengel.ch/</a></code>m[].</p>
<h2>AUTHOR</h2>
<p> Rafael Ostertag rafi [at] guengel.ch</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-yapet/">yapet</a></code>(1), <code><a href="/docs/linux/man/1-yapet2csv/">yapet2csv</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2008, 2009, 2010, 2011, 2013, 2014 Rafael Ostertag &lt;rafi [at] guengel.ch&gt; </p>
<h2>Index</h2>
