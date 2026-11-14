---
title: "fastjar(1)"
name: "fastjar"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fastjar/"
description: "fastjar – archive tool for Java archives"
---

<h2 class="name">NAME</h2>
<p> fastjar &#8211; archive tool for Java archives </p>
<h2>SYNOPSIS</h2>
<p> fastjar <code>-ctxu</code> [<font SIZE="-1"><code>OPTIONS</code></font>] [<i>jar-file</i>] [<i>manifest-file</i>] [<code>-C</code> <i>dir</i>] <i>files</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;fastjar&quot;</tt> is an implementation of Sun&#8217;s jar utility that comes with the <font SIZE="-1">JDK</font>, written entirely in C, and runs in a fraction of the time while being feature compatible. </p>
<p> If any file is a directory then it is processed recursively. The manifest file name and the archive file name needs to be specified in the same order the <code>-m</code> and <code>-f</code> flags are specified.</p>
<h2>OPTIONS</h2>
<p> Exactly one of the following actions must be specified:</p>
<dl>
<dt><code>-c</code></p>
<dd> Create new archive.</p>
<dt><code>-t</code></p>
<dd> List table of contents for archive.</p>
<dt><code>-x</code></p>
<dd> Extract named (or all) files from archive.</p>
<dt><code>-u</code></p>
<dd> Update existing archive.</dl>
<p> The following parameters are optional:</p>
<dl>
<dt><code>-@</code></p>
<dd> Read the names of the files to add to the archive from stdin. This option is supported only in combination with <code>-c</code> or <code>-u</code>. Non standard option added in the <font SIZE="-1">GCC</font> version.</p>
<dt><code>-C</code> <i>directory</i></p>
<dd> Change to the <i>directory</i> and include the following file.</p>
<dt><code>-E</code></p>
<dd> Prevent fastjar from reading the content of a directory when specifying one (and instead relying on the provided list of files to populate the archive with regard to the directory entry). Non standard option added in the <font SIZE="-1">GCC</font> version.</p>
<dt><code>-M</code></p>
<dd> Do not create a manifest file for the entries.</p>
<dt><code>-i</code></p>
<dd> Generate an index of the packages in this jar and its Class-Path.</p>
<dt><code>-J</code></p>
<dd> All options starting with <code>-J</code> are ignored.</p>
<dt><code>-0</code></p>
<dd> Store only; use no <font SIZE="-1">ZIP</font> compression.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display version information.</p>
<dt><code>-f</code> <i>archive</i></p>
<dd> Specify archive file name.</p>
<dt><code>-m</code> <i>manifest</i></p>
<dd> Include manifest information from specified <i>manifest</i> file.</p>
<dt><code>-v</code></p>
<dd> Generate verbose output on standard output.</dl>
<p> Parameters of the form <tt>@option</tt>{@}<i></i><font SIZE="-1"><i>FILE</i></font><i></i> are considered to be names of files, and are expanded with the contents of the file. </p>
<p> All remaining options are considered to be names of files.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gcj/">gcj</a></i>(1), <i><a href="/docs/linux/man/1-gij/">gij</a></i>(1), <i><a href="/docs/linux/man/1-grepjar/">grepjar</a></i>(1) and the Info entry for <i>gcj</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2002, 2007, 2008 Matthias Klose </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version. A copy of the license is included in the man page <i><a href="/docs/linux/man/7-gfdl/">gfdl</a></i>(7). </p>
<h2>Index</h2>
