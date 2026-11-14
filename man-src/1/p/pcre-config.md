---
title: "pcre-config(1)"
name: "pcre-config"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcre-config/"
description: "pcre-config – program to return PCRE configuration"
---

<h2 class="name">NAME</h2>
<p> pcre-config &#8211; program to return PCRE configuration </p>
<h2>SYNOPSIS</h2>
<p> <code>pcre-config</code> [<code>&#8211;prefix</code>] [<code>&#8211;exec-prefix</code>] [<code>&#8211;version</code>] [<code>&#8211;libs</code>] [<code>&#8211;libs-posix</code>] [<code>&#8211;cflags</code>] [<code>&#8211;cflags-posix</code>] </p>
<h2>DESCRIPTION</h2>
<p> <code>pcre-config</code> returns the configuration of the installed PCRE libraries: the options required to compile a program to use them. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;prefix</code></p>
<dd> Writes the directory prefix used in the PCRE installation for architecture independent files (e.g. <i>/usr</i>) to standard output.</p>
<dt><code>&#8211;exec-prefix</code></p>
<dd> Writes the directory prefix used in the PCRE installation for architecture dependent files (normally the same as <code>&#8211;prefix</code>) to standard output.</p>
<dt><code>&#8211;version</code></p>
<dd> Writes the version of PCRE installed to standard output.</p>
<dt><code>&#8211;libs</code></p>
<dd> Writes to standard output the command line options required to link with PCRE (e.g. <i>-lpcre</i>).</p>
<dt><code>&#8211;libs-posix</code></p>
<dd> Writes to standard output the command line options required to link with the PCRE POSIX emulation library (e.g. <i>-lpcreposix -lpcre</i>).</p>
<dt><code>&#8211;cflags</code></p>
<dd> Writes to standard output the command line options required to compile files that use PCRE (this often includes some <i>-I</i> options, but is blank on debian systems).</p>
<dt><code>&#8211;cflags-posix</code></p>
<dd> Writes to standard output the command line options required to compile files that use the PCRE POSIX emulation library (this often includes some -I options, but is blank on debian systems). Suppress printing of filenames when searching multiple files.</p>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Mark Baker &lt;mark [at] mnb.org.uk&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-pcre/">pcre</a>(3) </p>
<p> </code></p>
<h2>Index</h2>
