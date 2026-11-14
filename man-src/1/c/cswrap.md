---
title: "cswrap(1)"
name: "cswrap"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cswrap/"
description: "cswrap – generic compiler wrapper"
---

<h2 class="name">NAME</h2>
<p> cswrap &#8211; generic compiler wrapper </p>
<h2>SYNOPSIS</h2>
<p> <code>cswrap</code> [<i>&#8211;help</i> | <i>&#8211;print-path-to-wrap</i>]</p>
<h2>DESCRIPTION</h2>
<p> cswrap is a generic compiler wrapper that translates relative paths to absolute paths in diagnostic messages. Create a symbolic link to cswrap named as your compiler (gcc, g++, &#8230;) and put it to your $PATH. </p>
<p> Translated diagnostic messages are decorated by suffix <code>&lt;&#8211;[TOOL]</code> if they are produced by a tool named <code>TOOL</code> (given by cswrap invokation via symlink named <code>TOOL</code>). This only applies to translated diagnostic messages, which does not include code snippets, for instance. </p>
<p> If cswrap is installed on system, the following command activates the wrapper: </p>
<dl>
<dt>
<dd>
<pre>
export PATH=&quot;`cswrap --print-path-to-wrap`:$PATH&quot;
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Prints basic usage information.</dl>
<p> <code>&#8211;print-path-to-wrap</code></p>
<dl>
<dt>
<dd> Prints path to the directory with symlinks to the cswrap executable.</dl>
<h2>EXIT STATUS</h2>
<p> cswrap propagates the exit status returned by the compiler (in case cswrap succeeds to run the compiler).</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code>CSWRAP_CAP_FILE</code></p>
<dl>
<dt>
<dd> If set to a non-empty string, cswrap captures diagnostic messages into a file named <code>$CSWRAP_CAP_FILE</code>. In this case, the capture file is protected by a lock named <code>/cswrap_cap_file_lock</code> in order to obtain consistent output when running multiple compiler processes in parallel.</dl>
<p> <code>CSWRAP_TIMEOUT</code></p>
<dl>
<dt>
<dd> If set to a positive integer, cswrap installs a timeout for the compiler being wrapped. If the specified amount of time (given in seconds) elapses the compiler process is signalled by SIGTERM. Note the cswrap process waits till the compiler process finishes in any case.</dl>
<p> <code>CSWRAP_TIMEOUT_FOR</code></p>
<dl>
<dt>
<dd> Colon-separated list of programs (compilers) that <code>$CSWRAP_TIMEOUT</code> should be applied to. If <code>$CSWRAP_TIMEOUT_FOR</code> is unset or empty, <code>$CSWRAP_TIMEOUT</code> applies to all programs.</dl>
<p> <code>CSWRAP_DEL_CFLAGS</code>, <code>CSWRAP_DEL_CXXFLAGS</code></p>
<dl>
<dt>
<dd> cswrap expects a colon-separated list of compiler flags that should be removed from command line prior to invoking the compiler. The parameters are matched for exact match and they are case-sensitive. If a compiler flag appears in the command line multiple times, all its occurrences are removed. <code>$CSWRAP_DEL_CFLAGS</code> applies to compilation of C sources only. <code>$CSWRAP_DEL_CXXFLAGS</code> applies to compilation of C++ sources only. Flags to be removed can be specified by shell wildcard patterns (using the format accepted by <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3)).</dl>
<p> <code>CSWRAP_ADD_CFLAGS</code>, <code>CSWRAP_ADD_CXXFLAGS</code></p>
<dl>
<dt>
<dd> cswrap expects a colon-separated list of compiler flags that should be appended to command line prior to invoking the compiler. The flags are appended even if they already appear in the command line and they are always appended at the end of the command line. <code>$CSWRAP_ADD_CFLAGS</code> applies to compilation of C sources only. <code>$CSWRAP_ADD_CXXFLAGS</code> applies to compilation of C++ sources only.</dl>
<h2>BUGS</h2>
<p> Please report bugs and feature requests to the following mailing-list: </p>
<dl>
<dt>
<dd>
<pre>
<a rel="nofollow" href="https://fedorahosted.org/mailman/listinfo/cswrap-devel">https://fedorahosted.org/mailman/listinfo/cswrap-devel</a>
</pre>
</dl>
<h2>AUTHOR</h2>
<p> Written by Kamil Dudka.</p>
<h2>COPYING</h2>
<p> Copyright (C) 2013-2014 Red Hat, Inc. Free use of this software is granted under the terms of the GNU General Public License (GPL). See the COPYING file for details. </p>
<h2>Index</h2>
