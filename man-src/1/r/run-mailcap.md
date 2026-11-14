---
title: "run-mailcap(1)"
name: "run-mailcap"
section: "1"
letter: "r"
url: "/docs/linux/man/1-run-mailcap/"
description: "run-mailcap, view, see, edit, compose, print – execute programs via entries in the mailcap file"
---

<h2 class="name">NAME</h2>
<p> run-mailcap, view, see, edit, compose, print &#8211; execute programs via entries in the <i>mailcap</i> file </p>
<h2>SYNOPSIS</h2>
<p> <code>run-mailcap</code> &#8211;action=ACTION [&#8211;option[=value]] [MIME-TYPE:[ENCODING:]]FILE [&#8230;] </p>
<p> The <code>see</code>, <code>edit</code>, <code>compose</code> and <code>print</code> versions are just aliases that default to the view, edit, compose, and print actions (respectively). </p>
<h2>DESCRIPTION</h2>
<p> <code>run-mailcap</code> (or any of its aliases) will use the given action to process each mime-type/file in turn. Each file is specified as its mime-type, its encoding (e.g. compression), and filename together, separated by colons. If the mime-type is omitted, an attempt to determine the type is made by trying to match the file&#8217;s extension with those in the <i>mime.types</i> files. If no mime-type is found, a last attempt will be done by running the <code>file</code> command, if available. If the encoding is omitted, it will also be determined from the file&#8217;s extensions. Currently supported encodings are <code>gzip</code> (.gz), <code>bzip2</code> (.bz2), <code>xz</code> (.xz), and <code>compress</code> (.Z). A filename of &quot;-&quot; can be used to mean &quot;standard input&quot;, but then a mime-type <code>must</code> be specified. </p>
<p> Both the user&#8217;s files (~/.mailcap; ~/.mime.types) and the system files (/etc/mailcap; /etc/mime.types) are searched in turn for information.</p>
<h3>EXAMPLES</h3>
<p>&nbsp;<wbr>&nbsp;see picture.jpg<br />
&nbsp;<wbr>&nbsp;print output.ps.gz<br />
&nbsp;<wbr>&nbsp;compose text/html:index.htm<br />
&nbsp;<wbr>&nbsp;extract-mail-attachment msg.txt | see image/tiff:gzip:-</p>
<h3>OPTIONS</h3>
<p> All options are in the form &#8211;&lt;opt&gt;=&lt;value&gt;.</p>
<dl>
<dt><code>&#8211;action=&lt;action&gt;</code></p>
<dd> Performs the specified action on the files. Valid actions are <i>view</i>, <i>cat</i> (uses only &quot;copiousoutput&quot; rules and sends output to STDOUT) , <i>compose</i>, <i>composetyped</i>, <i>edit</i> and <i>print</i>. If no action is specified, the action will be determined by how the program was called.</p>
<dt><code>&#8211;debug</code></p>
<dd> Turns on extra information to find out what is happening.</p>
<dt><code>&#8211;nopager</code></p>
<dd> Ignores any &quot;copiousoutput&quot; directive and sends output to STDOUT.</p>
<dt><code>&#8211;norun</code></p>
<dd> Displays the found command without actually executing it.</dl>
<h2>SECURITY</h2>
<p> A temporary symbolic link to the file is opened if the file name matches the Perl regular expression &quot;[^[:alnum:],.:/@%^+=_-]&quot;, in order to protect from the injection of shell commands, and to make sure that the name can always be displayed in the current locale. In addition, the file is opened using its absolute path to prevent the injection of command-line arguments, for instance using file names starting with dashes.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-file/">file</a></code>(1) <code><a href="/docs/linux/man/5-mailcap/">mailcap</a></code>(5) <code><a href="/docs/linux/man/5-mailcap-order/">mailcap.order</a></code>(5) <code><a href="/docs/linux/man/8-update-mime/">update-mime</a></code>(8)</p>
<h2>AUTHOR</h2>
<p> <code>run-mailcap</code> (and its aliases) was written by Brian White &lt;bcwhite [at] pobox.com&gt;.</p>
<h2>COPYRIGHT</h2>
<p> <code>run-mailcap</code> (and its aliases) is in the public domain (the only true &quot;free&quot;). </p>
<h2>Index</h2>
