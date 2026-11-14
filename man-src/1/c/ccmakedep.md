---
title: "ccmakedep(1)"
name: "ccmakedep"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ccmakedep/"
description: "ccmakedep – create dependencies in makefiles using a C compiler"
---

<h2>NAME</h2>
<p> ccmakedep &#8211; create dependencies in makefiles using a C compiler</p>
<h2>SYNOPSIS</h2>
<p> <code>ccmakedep</code> [ <code>cpp-flags</code> ] [ <code>-w</code><i>width</i> ] [ <code>-s</code><i>magic-string</i> ] [ <code>-f</code><i>makefile</i> ] [ <code>-o</code><i>object-suffix</i> ] [ <code>-v</code> ] [ <code>-a</code> ] [ <code>-cc</code><i>compiler</i> ] [ &#8212; <i>options</i> &#8212; ] <i>sourcefile</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>ccmakedep</code> program calls a C compiler to preprocess each <i>sourcefile</i>, and uses the output to construct <i>makefile</i> rules describing their dependencies. These rules instruct <code><a href="/docs/linux/man/1-make/">make</a></code>(1) on which object files must be recompiled when a dependency has changed. </p>
<p> By default, <code>ccmakedep</code> places its output in the file named <i>makefile</i> if it exists, otherwise <i>Makefile.</i> An alternate makefile may be specified with the <code>-f</code> option. It first searches the makefile for a line beginning with </p>
<p> # DO NOT DELETE </p>
<p> or one provided with the <code>-s</code> option, as a delimiter for the dependency output. If it finds it, it will delete everything following this up to the end of the makefile and put the output after this line. If it doesn&#8217;t find it, the program will append the string to the makefile and place the output after that.</p>
<h2>EXAMPLE</h2>
<p> Normally, <code>ccmakedep</code> will be used in a makefile target so that typing &#8216;make depend&#8217; will bring the dependencies up to date for the makefile. For example, </p>
<pre><code>
SRCS &amp;nbsp;
= &amp;nbsp;
file1.c file2.c... CFLAGS &amp;nbsp;
= &amp;nbsp;
- O - DHACK - I../ foobar - xyz
    depend:
        ccmakedep-- &amp;nbsp;
$(CFLAGS) &amp; nbsp;
--&amp;nbsp;
$(SRCS)
</code></pre>
<h2>OPTIONS</h2>
<p> The program will ignore any option that it does not understand, so you may use the same arguments that you would for <code><a href="/docs/linux/man/1-cc/">cc</a></code>(1), including <code>-D</code> and <code>-U</code> options to define and undefine symbols and <code>-I</code> to set the include path.</p>
<dl>
<dt><code>-a</code></p>
<dd> Append the dependencies to the file instead of replacing existing dependencies.</p>
<dt><code>-cc</code><i>compiler</i></p>
<dd> Use this compiler to generate dependencies.</p>
<dt><code>-f</code><i>makefile</i></p>
<dd> Filename. This allows you to specify an alternate makefile in which <code>ccmakedep</code> can place its output. Specifying &#8220;-&#8221; as the file name (that is, <code>-f-</code>) sends the output to standard output instead of modifying an existing file.</p>
<dt><code>-s</code><i>string</i></p>
<dd> Starting string delimiter. This option permits you to specify a different string for <code>ccmakedep</code> to look for in the makefile. The default is &#8220;# DO NOT DELETE&#8221;.</p>
<dt><code>-v</code></p>
<dd> Be verbose: display the C compiler command before running it.</p>
<dt><code>&#8212;</code><i> options </i><code>&#8212;</code></p>
<dd> If <code>ccmakedep</code> encounters a double hyphen (&#8211;) in the argument list, then any unrecognized arguments following it will be silently ignored. A second double hyphen terminates this special treatment. In this way, <code>ccmakedep</code> can be made to safely ignore esoteric compiler arguments that might normally be found in a CFLAGS <code>make</code> macro (see the <code>EXAMPLE</code> section above). <code>-D</code>, <code>-I</code>, and <code>-U</code> options appearing between the pair of double hyphens are still processed normally.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cc/">cc</a></code>(1), <code><a href="/docs/linux/man/1-make/">make</a></code>(1), <code><a href="/docs/linux/man/1-makedepend/">makedepend</a></code>(1), <code><a href="/docs/linux/man/1-ccmakedep/">ccmakedep</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> <code>ccmakedep</code> was written by the X Consortium. </p>
<p> Colin Watson wrote this manual page, originally for the Debian Project, based partly on the manual page for <code><a href="/docs/linux/man/1-makedepend/">makedepend</a></code>(1). </p>
<h2>Index</h2>
