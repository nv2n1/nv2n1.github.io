---
title: "lksh(1)"
name: "lksh"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lksh/"
description: "lksh – Legacy Korn shell built on mksh"
---

<h2 class="name">NAME</h2>
<p> <code>lksh</code> &#8211; Legacy Korn shell built on mksh </p>
<h2>SYNOPSIS</h2>
<p> -words [-<code>+abCefhiklmnprUuvXx </code>[-<code>+o </code><i>opt</i> ] ] [-<code>c </code><i>string |</i> &#8211;<code>s |</code> <i>file</i> [<i>args &#8230;</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> is a command interpreter intended exclusively for running legacy shell scripts. It is built on <code>mksh</code> refer to its manual page for details on the scripting language. It is recommended to port scripts to <code>mksh</code> instead of relying on legacy or idiotic POSIX-mandated behaviour, since the MirBSD Korn Shell scripting language is much more consistent.</p>
<h2>LEGACY MODE</h2>
<p> has the following differences from <code>mksh</code> </p>
<ul>
<li> is not suitable for use as /bin/sh
<li> There is no explicit support for interactive use, nor any command line editing or history code. Hence, is not suitable as a user&#8217;s login shell, either; use <code>mksh</code> instead.
<li> The <code>KSH_VERSION</code> string identifies as &#8220;LEGACY KSH&#8221; instead of &#8220;MIRBSD KSH&#8221;
<li> only offers the traditional ten file descriptors to scripts.
<li> uses <code>POSIX</code> arithmetics, which has quite a few implications: The data type for arithmetics is the host ISO C Vt long data type. Signed integer wraparound is Undefined Behaviour. The sign of the result of a modulo operation with at least one negative operand is unspecified. Shift operations on negative numbers are unspecified. Division of the largest negative number by -1 is Undefined Behaviour. The compiler is permitted to delete all data and crash the system if Undefined Behaviour occurs.
<li> The rotation arithmetic operators are not available.
<li> The shift arithmetic operators take all bits of the second operand into account; if they exceed permitted precision, the result is unspecified.
<li> The <code>GNU</code> <code>bash</code> extension &amp;&gt; to redirect stdout and stderr in one go is not parsed.
<li> The <code>mksh</code> command line option &#8211;<code>T</code> is not available.
<li> Unless <code>set -o posix</code> is active, always uses traditional mode for constructs like:<br />
<blockquote>
<pre>
$ set -- $(getopt ab:c &quot;$@&quot;)
$ echo $?
</pre>
</blockquote>
<p> POSIX mandates this to show 0, but traditional mode passes through the errorlevel from the <a href="/docs/linux/man/1-getopt/">getopt</a>(1) command. </p>
<li> <code>lksh</code> unlike AT&amp;T System <code>ksh</code> does not keep file descriptors &gt; 2 private. </ul>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mksh/">mksh</a>(1) </p>
<p> <a rel="nofollow" href="https://www.mirbsd.org/mksh.htm">https://www.mirbsd.org/mksh.htm</a> </p>
<p> <a rel="nofollow" href="https://www.mirbsd.org/ksh-chan.htm">https://www.mirbsd.org/ksh-chan.htm</a></p>
<h2>CAVEATS</h2>
<p> tries to make a cross between a legacy bourne/posix compatibl-ish shell and a legacy pdksh-alike but &#8220;legacy&#8221; is not exactly specified. </p>
<p> The <code>set</code> built-in command does not have all options one would expect from a full-blown <code>mksh</code> or <code>pdksh</code> </p>
<p> Talk to the MirOS development team using the mailing list at Aq miros-mksh [at] mirbsd.org or the <code>#!/bin/mksh</code> (or <code>#ksh</code> ) IRC channel at irc.freenode.net (Port 6697 SSL, 6667 unencrypted) if you need any further quirks or assistance, and consider migrating your legacy scripts to work with <code>mksh</code> instead of requiring <code>.</code> </p>
<h2>Index</h2>
