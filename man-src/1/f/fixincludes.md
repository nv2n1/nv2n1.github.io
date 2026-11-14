---
title: "fixincludes(1)"
name: "fixincludes"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fixincludes/"
description: "fixincludes – Reduce the number of #includes in KDE source files"
---

<h2 class="name">NAME</h2>
<p> fixincludes &#8211; Reduce the number of #includes in KDE source files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>fixincludes</code> [<code>-v, &#8211;verbose</code>] [<code>-e, &#8211;experimental</code>] [<code>-m, &#8211;modify</code>] [<i>file</i>] [<code>&#8211;help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>fixincludes</code></p>
<dd>tries to reduce the number of #includes in C++ source files. Much of it&#8217;s processing is specific to KDE sources and so it might not work so well with sources for non-KDE applications. </p>
<p> The following problems are identified by <code>fixincludes</code>: </p>
<dl>
<dt>
<dd> &bull; Including headers that are no longer supported but which exist for compatibility with older Qt/KDE versions;</dl>
<dl>
<dt>
<dd> &bull; Including the same file multiple times.</dl>
<p> There is also an experimental mode which tries removing each #include one at a time (with a few exceptions) to see whether the source still compiles. Note that this experimental mode will modify the original sources. </p>
<p> By default the sources will not be modified; the identified problems will simply be written to standard output. </p>
<p> The list of C++ sources to examine should be given on the command-line. If no files are given, all C++ sources in or beneath the current directory will be examined (with the exception of directories whose Makefile.am contains <code>-UQT_NO_COMPAT</code> or <code>-UKDE_NO_COMPAT</code>) </p>
<p> This utility is part of the KDE Software Development Kit.</p>
<h2>OPTIONS</h2>
<p> <code>-v, &#8211;verbose</code></p>
<dl>
<dt>
<dd> Verbose mode. Additional debugging output is written to standard output.</dl>
<p> <code>-e, &#8211;experimental</code></p>
<dl>
<dt>
<dd> Experimental mode, as described above in detail. Note that this option implies <code>&#8211;modify</code>.</dl>
<p> <code>-m, &#8211;modify</code></p>
<dl>
<dt>
<dd> As well as writing messages to standard output, actually modify the original sources to fix any problems that were found.</dl>
<h2>AUTHORS</h2>
<p> <code>fixincludes</code> was written by Dirk Mueller &lt;mueller [at] kde.org&gt;.</p>
<h2>AUTHOR</h2>
<p> <code>Ben Burton</code> &lt;bab [at] debian.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
