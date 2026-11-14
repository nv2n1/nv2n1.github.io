---
title: "gjar(1)"
name: "gjar"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gjar/"
description: "gjar – – Archive tool for Java archives"
---

<h2 class="name">NAME</h2>
<p> gjar &#8211; &#8211; Archive tool for Java archives </p>
<h2>SYNOPSIS</h2>
<p> gjar <code>-ctxui</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] <i>jar-file</i> [<code>-C</code> <i></i><font SIZE="-1"><i>DIR</i></font><i></i> <i></i><font SIZE="-1"><i>FILE</i></font><i></i>] <i></i><font SIZE="-1"><i>FILE</i></font><i></i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>gjar</code> is an implementation of Sun&#8217;s jar utility that comes with the <font SIZE="-1">JDK</font>. </p>
<p> If any file is a directory then it is processed recursively. The manifest file name and the archive file name needs to be specified in the same order the <code>-m</code> and <code>-f</code> flags are specified.</p>
<h2>OPTIONS</h2>
<p> Operation mode:</p>
<dl>
<dt><code>-c</code></p>
<dd> Create new archive.</p>
<dt><code>-t</code></p>
<dd> List table of contents for archive.</p>
<dt><code>-x</code></p>
<dd> Extract named (or all) files from archive.</p>
<dt><code>-u</code></p>
<dd> Update existing archive.</p>
<dt><code>-i</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Compute archive index.</dl>
<p> Operation modifiers:</p>
<dl>
<dt><code>-f</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Specify archive file name.</p>
<dt><code>-0</code></p>
<dd> Store only; use no <font SIZE="-1">ZIP</font> compression.</p>
<dt><code>-v</code></p>
<dd> Generate verbose output on standard output.</p>
<dt><code>-M</code></p>
<dd> Do not create a manifest file for the entries.</p>
<dt><code>-m</code> <i>manifest</i></p>
<dd> Include manifest information from specified <i>manifest</i> file.</dl>
<p> File name selection:</p>
<dl>
<dt><code>-C</code> <i></i><font SIZE="-1"><i>DIR</i></font><i></i><i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Change to the <i></i><font SIZE="-1"><i>DIR</i></font><i></i> and include the following <i></i><font SIZE="-1"><i>FILE</i></font><i></i>.</p>
<dt><code>-@</code></p>
<dd> Read the names of the files to add to the archive from stdin. This option is supported only in combination with <code>-c</code> or <code>-u</code>. Non standard option added in the <font SIZE="-1">GCC</font> version.</dl>
<p> Standard options:</p>
<dl>
<dt><code>-help</code></p>
<dd> Print help text, then exit.</p>
<dt><code>-version</code></p>
<dd> Print version number, then exit.</p>
<dt><code>-J</code><i></i><font SIZE="-1"><i>OPTION</i></font><i></i></p>
<dd> Pass argument to the Java runtime.</dl>
<h2>BUGS</h2>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-java/">java</a></i>(1), &#8230;</p>
<h2>AUTHOR</h2>
<h2>Index</h2>
