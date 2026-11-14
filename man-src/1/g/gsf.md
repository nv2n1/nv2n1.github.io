---
title: "gsf(1)"
name: "gsf"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gsf/"
description: "gsf – archiving utility using the G Structured File library"
---

<h2 class="name">NAME</h2>
<p> gsf &#8211; archiving utility using the G Structured File library</p>
<h2>SYNOPSIS</h2>
<p> <code>gsf</code> [<i>OPTION&#8230;</i>] <i>SUBCOMMAND</i> <i>ARCHIVE&#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> This manual page briefly documents the <code>gsf</code> command. </p>
<p> <code>gsf</code> is a simple archive utility, somewhat similar to <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1). It operates on files following one of the structured file formats understood by the G Structured File library, for example, Microsoft Excel(TM) files. </p>
<h2>OPTIONS</h2>
<h3>Options</h3>
<dl>
<dt><code>-?, &#8211;help</code></p>
<dd> Show help options</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Display gsf&#8217;s version </p>
</dl>
<h3>Subcommands</h3>
<dl>
<dt><code>cat</code></p>
<dd> Output one or more files in archive</p>
<dt><code>dump</code></p>
<dd> Dump one or more files in archive as formatted hexadecimal</p>
<dt><code>help</code></p>
<dd> List subcommands</p>
<dt><code>list</code></p>
<dd> List files in archive</p>
<dt><code>props</code></p>
<dd> Archive list of property names </p>
</dl>
<h2>EXAMPLES</h2>
<p> To list the content structure of a Microsoft Excel(TM) file <i>arrays.xls</i>: </p>
<p> gsf list arrays.xls </p>
<p> To dump Workbook, an individual data stream in arrays.xls: </p>
<p> gsf dump arrays.xls Workbook </p>
<h2>AUTHORS</h2>
<p> <code>gsf</code>&#8216;s primary authors are Morten Welinder &lt;terra [at] gnome.org&gt; and Jody Goldberg &lt;jody [at] gnome.org&gt;. </p>
<p> The initial version of this manpage was written by J.H.M. Dassen (Ray) &lt;jdassen [at] debian.org&gt;. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gnumeric/">gnumeric</a></code>(1) </p>
<p> The Gnumeric homepage &lt;URL: <a rel="nofollow" href="http://www.gnome.org/projects/gnumeric/">http://www.gnome.org/projects/gnumeric/</a> &gt; </p>
<p> The GNOME project page &lt;URL: <a rel="nofollow" href="http://www.gnome.org/">http://www.gnome.org/</a> &gt; </p>
<h2>Index</h2>
