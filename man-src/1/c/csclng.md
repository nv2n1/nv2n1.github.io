---
title: "csclng(1)"
name: "csclng"
section: "1"
letter: "c"
url: "/docs/linux/man/1-csclng/"
description: "csclng – a compiler wrapper that runs the Clang analyzer in background"
---

<h2 class="name">NAME</h2>
<p> csclng &#8211; a compiler wrapper that runs the Clang analyzer in background </p>
<h2>SYNOPSIS</h2>
<p> <code>csclng</code> [<i>&#8211;help</i> | <i>&#8211;print-path-to-wrap</i>]</p>
<h2>DESCRIPTION</h2>
<p> csclng is a compiler wrapper that runs clang in background. Create a symbolic link to csclng named as your compiler (gcc, g++, &#8230;) and put it to your $PATH. </p>
<p> The following parameters are given to clang by default: </p>
<dl>
<dt>
<dd> &bull; &#8211;analyze</dl>
<p> The following parameters are passed to clang from compiler&#8217;s command line: </p>
<dl>
<dt>
<dd> &bull; -D&#8230;</dl>
<dl>
<dt>
<dd> &bull; -I&#8230;</dl>
<dl>
<dt>
<dd> &bull; -include &#8230;</dl>
<dl>
<dt>
<dd> &bull; -iquote &#8230;</dl>
<dl>
<dt>
<dd> &bull; -isystem &#8230;</dl>
<p> The following file extensions are recognized as C/C++ source files: </p>
<dl>
<dt>
<dd> &bull; c</dl>
<dl>
<dt>
<dd> &bull; C</dl>
<dl>
<dt>
<dd> &bull; cc</dl>
<dl>
<dt>
<dd> &bull; cpp</dl>
<dl>
<dt>
<dd> &bull; cxx</dl>
<p> The following path substrings are black-listed from being scanned by clang: </p>
<dl>
<dt>
<dd> &bull; conftest.c</dl>
<dl>
<dt>
<dd> &bull; _configtest.c</dl>
<dl>
<dt>
<dd> &bull; /CMakeTmp/</dl>
<dl>
<dt>
<dd> &bull; ../test.c</dl>
<p> If csclng is installed on system, the following command activates the wrapper: </p>
<dl>
<dt>
<dd>
<pre>
export PATH=&quot;`csclng --print-path-to-wrap`:$PATH&quot;
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
<dd> Prints path to the directory with symlinks to the csclng executable.</dl>
<h2>EXIT STATUS</h2>
<p> csclng propagates the exit status returned by the compiler (in case csclng succeeds to run the compiler). The exit status returned by clang does not affect the resulting exit status.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code>DEBUG_CSCLNG</code></p>
<dl>
<dt>
<dd> If set to a non-empty string, csclng outputs the list of parameters given to clang to the standard output.</dl>
<p> <code>CSCLNG_ADD_OPTS</code></p>
<dl>
<dt>
<dd> csclng expects a colon-separated list of Clang options that should be appended to command line prior to invoking Clang. The options are appended even if they already appear in the command line and they are always appended at the end of the command line.</dl>
<h2>BUGS</h2>
<p> Please report bugs and feature requests to the following mailing-list: </p>
<dl>
<dt>
<dd>
<pre>
<a rel="nofollow" href="https://fedorahosted.org/mailman/listinfo/cscppc-devel">https://fedorahosted.org/mailman/listinfo/cscppc-devel</a>
</pre>
</dl>
<h2>AUTHOR</h2>
<p> Written by Kamil Dudka.</p>
<h2>COPYING</h2>
<p> Copyright (C) 2013-2014 Red Hat, Inc. Free use of this software is granted under the terms of the GNU General Public License (GPL). See the COPYING file for details. </p>
<h2>Index</h2>
