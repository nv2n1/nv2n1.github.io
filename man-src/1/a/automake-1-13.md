---
title: "automake-1-13(1)"
name: "automake-1-13"
section: "1"
letter: "a"
url: "/docs/linux/man/1-automake-1-13/"
description: "automake – manual page for automake 1.13.4"
---

<p>automake &#8211; manual page for automake 1.13.4</p>
<h2>Synopsis</h2>
<p><code>automake-1.13</code> [<i>OPTION</i>]&#8230; [<i>Makefile</i>]&#8230;</p>
<h2>Description</h2>
<p>Generate Makefile.in for configure from Makefile.am.</p>
<h3>Operation modes:</h3>
<dl>
<dt><code>&#8211;help</code></dt>
<dd>print this help, then exit</dd>
<dt><code>&#8211;version</code></dt>
<dd>print version number, then exit</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd>verbosely list files processed</dd>
<dt><code>&#8211;no-force</code></dt>
<dd>only update Makefile.in&#8217;s that are out of date</dd>
<dt><code>-W</code>, <code>&#8211;warnings</code>=<i>CATEGORY</i></dt>
<dd>report the warnings falling in CATEGORY</dd></dl>
<h3>Dependency tracking:</h3>
<dl>
<dt><code>-i</code>, <code>&#8211;ignore-deps</code></dt>
<dd>disable dependency tracking code</dd>
<dt><code>&#8211;include-deps</code></dt>
<dd>enable dependency tracking code</dd></dl>
<h3>Flavors:</h3>
<dl>
<dt><code>&#8211;foreign</code></dt>
<dd>set strictness to foreign</dd>
<dt><code>&#8211;gnits</code></dt>
<dd>set strictness to gnits</dd>
<dt><code>&#8211;gnu</code></dt>
<dd>set strictness to gnu</dd></dl>
<h3>Library files:</h3>
<dl>
<dt><code>-a</code>, <code>&#8211;add-missing</code></dt>
<dd>add missing standard files to package</dd>
<dt><code>&#8211;libdir</code>=<i>DIR</i></dt>
<dd>set directory storing library files</dd>
<dt><code>&#8211;print-libdir</code></dt>
<dd>print directory storing library files</dd>
<dt><code>-c</code>, <code>&#8211;copy</code></dt>
<dd>with <code>-a</code>, copy missing files (default is symlink)</dd>
<dt><code>-f</code>, <code>&#8211;force-missing</code></dt>
<dd>force update of standard files</dd></dl>
<h3>Warning categories include:</h3>
<dl>
<dt>gnu</dt>
<dd>GNU coding standards (default in gnu and gnits modes)</dd>
<dt>obsolete</dt>
<dd>obsolete features or constructions</dd>
<dt>override</dt>
<dd>user redefinitions of Automake rules or variables</dd>
<dt>portability</dt>
<dd>portability issues (default in gnu and gnits modes)</dd>
<dt>extra-portability</dt>
<dd>extra portability issues related to obscure tools</dd>
<dt>syntax</dt>
<dd>dubious syntactic constructs (default)</dd>
<dt>unsupported</dt>
<dd>unsupported or incomplete features (default)</dd>
<dt>all</dt>
<dd>all the warnings</dd>
<dt>no-CATEGORY</dt>
<dd>turn off warnings in CATEGORY</dd>
<dt>none</dt>
<dd>turn off all the warnings</dd>
<dt>error</dt>
<dd>treat warnings as errors</dd></dl>
<h3>Files automatically distributed if found (always):</h3>
<dl>
<dt>ABOUT-GNU</dt>
<dd>INSTALL config.rpath ltconfig</dd>
<dt>ABOUT-NLS</dt>
<dd>NEWS config.sub ltmain.sh</dd>
<dt>AUTHORS</dt>
<dd>README depcomp mdate-sh</dd>
<dt>BACKLOG</dt>
<dd>THANKS install-sh missing</dd>
<dt>COPYING</dt>
<dd>TODO libversion.in mkinstalldirs</dd>
<dt>COPYING.DOC</dt>
<dd>ar-lib ltcf-c.sh py-compile</dd>
<dt>COPYING.LESSER</dt>
<dd>compile ltcf-cxx.sh texinfo.tex</dd>
<dt>COPYING.LIB</dt>
<dd>config.guess ltcf-gcj.sh ylwrap</dd>
<dd>ChangeLog</dd></dl>
<h3>Files automatically distributed if found (under certain conditions):</h3>
<dl>
<dt>acconfig.h</dt>
<dd>config.h.bot configure configure.in</dd>
<dt>aclocal.m4</dt>
<dd>config.h.top configure.ac stamp-vti</dd></dl>
<h2>Author</h2>
<p>Written by Tom Tromey &lt;tromey [at] redhat.com&gt;</p>
<dl>
<dd>and Alexandre Duret-Lutz &lt;adl [at] gnu.org&gt;.</dd></dl>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;bug-automake [at] gnu.org&gt;.<br />
 GNU Automake home page: &lt;<a rel="nofollow" href="http://www.gnu.org/software/automake/">http://www.gnu.org/software/automake/</a>&gt;.<br />
 General help using GNU software: &lt;<a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a>&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Free Software Foundation, Inc. License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl-2.0.html">http://gnu.org/licenses/gpl-2.0.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>See Also</h2>
<p>The full documentation for <code>automake</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>automake</code> programs are properly installed at your site, the command</p>
<dl>
<dd><code>info automake</code></dd></dl>
<p> should give you access to the complete manual.</p>
