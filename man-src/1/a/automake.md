---
title: "automake(1)"
name: "automake"
section: "1"
letter: "a"
url: "/docs/linux/man/1-automake/"
description: "automake – manual page for automake 1.16.5"
---

<h2 class="name">NAME</h2>
<p> automake &#8211; manual page for automake 1.16.5 </p>
<h2>SYNOPSIS</h2>
<p> <code>automake-1.16</code> [<i>,OPTION/</i>]&#8230; [<i>,Makefile/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Generate Makefile.in for configure from Makefile.am.</p>
<h3>Operation modes:</h3>
<dl>
<dt><code>&#8211;help</code></p>
<dd> print this help, then exit</p>
<dt><code>&#8211;version</code></p>
<dd> print version number, then exit</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> verbosely list files processed</p>
<dt><code>&#8211;no-force</code></p>
<dd> only update Makefile.in&#8217;s that are out of date</p>
<dt><code>-W</code>, <code>&#8211;warnings</code>=<i>,CATEGORY/</i></p>
<dd> report the warnings falling in CATEGORY</dl>
<h3>Dependency tracking:</h3>
<dl>
<dt><code>-i</code>, <code>&#8211;ignore-deps</code></p>
<dd> disable dependency tracking code</p>
<dt><code>&#8211;include-deps</code></p>
<dd> enable dependency tracking code</dl>
<h3>Flavors:</h3>
<dl>
<dt><code>&#8211;foreign</code></p>
<dd> set strictness to foreign</p>
<dt><code>&#8211;gnits</code></p>
<dd> set strictness to gnits</p>
<dt><code>&#8211;gnu</code></p>
<dd> set strictness to gnu</dl>
<h3>Library files:</h3>
<dl>
<dt><code>-a</code>, <code>&#8211;add-missing</code></p>
<dd> add missing standard files to package</p>
<dt><code>&#8211;libdir</code>=<i>,DIR/</i></p>
<dd> set directory storing library files</p>
<dt><code>&#8211;print-libdir</code></p>
<dd> print directory storing library files</p>
<dt><code>-c</code>, <code>&#8211;copy</code></p>
<dd> with <code>-a</code>, copy missing files (default is symlink)</p>
<dt><code>-f</code>, <code>&#8211;force-missing</code></p>
<dd> force update of standard files</dl>
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
<h3>Files automatically distributed if found (always):</h3>
<dl>
<dt>ABOUT-GNU</p>
<dd> TODO install-sh mdate-sh</p>
<dt>ABOUT-NLS</p>
<dd> ar-lib libversion.in missing</p>
<dt>BACKLOG</p>
<dd> compile ltcf-c.sh mkinstalldirs</p>
<dt>COPYING</p>
<dd> config.guess ltcf-cxx.sh py-compile</p>
<dt>COPYING.DOC</p>
<dd> config.rpath ltcf-gcj.sh texinfo.tex</p>
<dt>COPYING.LESSER</p>
<dd> config.sub ltconfig ylwrap</p>
<dt>COPYING.LIB</p>
<dd> depcomp ltmain.sh</dl>
<h3>Files automatically distributed if found (as .md if needed):</h3>
<dl>
<dt>AUTHORS[.md]</p>
<dd> INSTALL[.md] README[.md] THANKS[.md]</p>
<dt>ChangeLog[.md]</p>
<dd> NEWS[.md]</dl>
<h3>Files automatically distributed if found (under certain conditions):</h3>
<dl>
<dt>README-alpha[.md]</p>
<dd> config.h.bot configure configure.in</p>
<dt>acconfig.h</p>
<dd> config.h.top configure.ac stamp-vti</p>
<dt>
<dd> aclocal.m4</dl>
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
<p> The full documentation for <code>automake</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>automake</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info automake</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
