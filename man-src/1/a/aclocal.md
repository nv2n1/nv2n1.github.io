---
title: "aclocal(1)"
name: "aclocal"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aclocal/"
description: "aclocal – manual page for aclocal 1.16.5"
---

<h2 class="name">NAME</h2>
<p> aclocal &#8211; manual page for aclocal 1.16.5 </p>
<h2>SYNOPSIS</h2>
<p> <code>aclocal</code> [<i>,OPTION/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Generate &#8216;aclocal.m4&#8217; by scanning &#8216;configure.ac&#8217; or &#8216;configure.in&#8217;</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;automake-acdir</code>=<i>,DIR/</i></p>
<dd> directory holding automake-provided m4 files</p>
<dt><code>&#8211;system-acdir</code>=<i>,DIR/</i></p>
<dd> directory holding third-party system-wide files</p>
<dt><code>&#8211;diff</code>[=<i>,COMMAND/</i>]</p>
<dd> run COMMAND [diff <code>-u]</code> on M4 files that would be changed (implies <code>&#8211;install</code> and <code>&#8211;dry-run</code>)</p>
<dt><code>&#8211;dry-run</code></p>
<dd> pretend to, but do not actually update any file</p>
<dt><code>&#8211;force</code></p>
<dd> always update output file</p>
<dt><code>&#8211;help</code></p>
<dd> print this help, then exit</p>
<dt><code>-I</code> DIR</p>
<dd> add directory to search list for .m4 files</p>
<dt><code>&#8211;install</code></p>
<dd> copy third-party files to the first <code>-I</code> directory</p>
<dt><code>&#8211;output</code>=<i>,FILE/</i></p>
<dd> put output in FILE (default aclocal.m4)</p>
<dt><code>&#8211;print-ac-dir</code></p>
<dd> print name of directory holding system-wide third-party m4 files, then exit</p>
<dt><code>&#8211;verbose</code></p>
<dd> don&#8217;t be silent</p>
<dt><code>&#8211;version</code></p>
<dd> print version number, then exit</p>
<dt><code>-W</code>, <code>&#8211;warnings</code>=<i>,CATEGORY/</i></p>
<dd> report the warnings falling in CATEGORY</dl>
<h3>Warning categories include:</h3>
<dl>
<dt>cross</p>
<dd> cross compilation issues</p>
<dt>gnu</p>
<dd> GNU coding standards (default in gnu and gnits modes)</p>
<dt>obsolete</p>
<dd> obsolete features or constructions (default)</p>
<dt>override</p>
<dd> user redefinitions of Automake rules or variables</p>
<dt>portability</p>
<dd> portability issues (default in gnu and gnits modes)</p>
<dt>portability-recursive</p>
<dd> nested Make variables (default with <code>-Wportability</code>)</p>
<dt>extra-portability</p>
<dd> extra portability issues related to obscure tools</p>
<dt>syntax</p>
<dd> dubious syntactic constructs (default)</p>
<dt>unsupported</p>
<dd> unsupported or incomplete features (default)</p>
<dt>all</p>
<dd> all the warnings</p>
<dt>no-CATEGORY</p>
<dd> turn off warnings in CATEGORY</p>
<dt>none</p>
<dd> turn off all the warnings</p>
<dt>error</p>
<dd> treat warnings as errors</dl>
<h2>AUTHOR</h2>
<p> Written by Tom Tromey &lt;tromey [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> and Alexandre Duret-Lutz &lt;adl [at] gnu.org&gt;.</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-automake [at] gnu.org&gt;.<br />
 GNU Automake home page: &lt;<a rel="nofollow" href="https://www.gnu.org/software/automake/">https://www.gnu.org/software/automake/</a>&gt;.<br />
 General help using GNU software: &lt;<a rel="nofollow" href="https://www.gnu.org/gethelp/">https://www.gnu.org/gethelp/</a>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021 Free Software Foundation, Inc. License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl-2.0.html">https://gnu.org/licenses/gpl-2.0.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>aclocal</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>aclocal</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info aclocal</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
