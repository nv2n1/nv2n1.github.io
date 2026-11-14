---
title: "automake-1-15(1)"
name: "automake-1-15"
section: "1"
letter: "a"
url: "/docs/linux/man/1-automake-1-15/"
description: "automake – manual page for automake 1.15.1"
---

<p>automake &#8211; manual page for automake 1.15.1 </p>
<h2>Synopsis</h2>
<p><code>automake-1.15</code> [<i>,OPTION/</i>]&#8230; [<i>,Makefile/</i>]&#8230;</p>
<h2>Description</h2>
<p>Generate Makefile.in for configure from Makefile.am.</p>
<h3>Operation modes:</h3>
<dl>
<dt><code>&#8211;help</code></p>
<dd>print this help, then exit</p>
<dt><code>&#8211;version</code></p>
<dd>print version number, then exit</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>verbosely list files processed</p>
<dt><code>&#8211;no-force</code></p>
<dd>only update Makefile.in&#8217;s that are out of date</p>
<dt><code>-W</code>, <code>&#8211;warnings</code>=<i>,CATEGORY/</i></p>
<dd>report the warnings falling in CATEGORY</dl>
<h3>Dependency tracking:</h3>
<dl>
<dt><code>-i</code>, <code>&#8211;ignore-deps</code></p>
<dd>disable dependency tracking code</p>
<dt><code>&#8211;include-deps</code></p>
<dd>enable dependency tracking code</dl>
<h3>Flavors:</h3>
<dl>
<dt><code>&#8211;foreign</code></p>
<dd>set strictness to foreign</p>
<dt><code>&#8211;gnits</code></p>
<dd>set strictness to gnits</p>
<dt><code>&#8211;gnu</code></p>
<dd>set strictness to gnu</dl>
<h3>Library files:</h3>
<dl>
<dt><code>-a</code>, <code>&#8211;add-missing</code></p>
<dd>add missing standard files to package</p>
<dt><code>&#8211;libdir</code>=<i>,DIR/</i></p>
<dd>set directory storing library files</p>
<dt><code>&#8211;print-libdir</code></p>
<dd>print directory storing library files</p>
<dt><code>-c</code>, <code>&#8211;copy</code></p>
<dd>with <code>-a</code>, copy missing files (default is symlink)</p>
<dt><code>-f</code>, <code>&#8211;force-missing</code></p>
<dd>force update of standard files</dl>
<h3>Warning categories include:</h3>
<dl>
<dt>gnu</p>
<dd>GNU coding standards (default in gnu and gnits modes)</p>
<dt>obsolete</p>
<dd>obsolete features or constructions</p>
<dt>override</p>
<dd>user redefinitions of Automake rules or variables</p>
<dt>portability</p>
<dd>portability issues (default in gnu and gnits modes)</p>
<dt>extra-portability</p>
<dd>extra portability issues related to obscure tools</p>
<dt>syntax</p>
<dd>dubious syntactic constructs (default)</p>
<dt>unsupported</p>
<dd>unsupported or incomplete features (default)</p>
<dt>all</p>
<dd>all the warnings</p>
<dt>no-CATEGORY</p>
<dd>turn off warnings in CATEGORY</p>
<dt>none</p>
<dd>turn off all the warnings</p>
<dt>error</p>
<dd>treat warnings as errors</dl>
<h3>Files automatically distributed if found (always):</h3>
<dl>
<dt>ABOUT-GNU</p>
<dd>INSTALL config.rpath ltconfig</p>
<dt>ABOUT-NLS</p>
<dd>NEWS config.sub ltmain.sh</p>
<dt>AUTHORS</p>
<dd>README depcomp mdate-sh</p>
<dt>BACKLOG</p>
<dd>THANKS install-sh missing</p>
<dt>COPYING</p>
<dd>TODO libversion.in mkinstalldirs</p>
<dt>COPYING.DOC</p>
<dd>ar-lib ltcf-c.sh py-compile</p>
<dt>COPYING.LESSER</p>
<dd>compile ltcf-cxx.sh texinfo.tex</p>
<dt>COPYING.LIB</p>
<dd>config.guess ltcf-gcj.sh ylwrap</p>
<dd>ChangeLog</dl>
<h3>Files automatically distributed if found (under certain conditions):</h3>
<dl>
<dt>acconfig.h</p>
<dd>config.h.bot configure configure.in</p>
<dt>aclocal.m4</p>
<dd>config.h.top configure.ac stamp-vti</dl>
<h2>Author</h2>
<p>Written by Tom Tromey &lt;tromey [at] redhat.com&gt;</p>
<dl>
<dd>and Alexandre Duret-Lutz &lt;adl [at] gnu.org&gt;.</dl>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;bug-automake [at] gnu.org&gt;.<br />
 GNU Automake home page: &lt;<a rel="nofollow" href="http://www.gnu.org/software/automake/">http://www.gnu.org/software/automake/</a>&gt;.<br />
 General help using GNU software: &lt;<a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a>&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2017 Free Software Foundation, Inc. License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl-2.0.html">http://gnu.org/licenses/gpl-2.0.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>See Also</h2>
<p>The full documentation for <code>automake</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>automake</code> programs are properly installed at your site, the command</p>
<dl>
<dd><code>info automake</code></dl>
<p> should give you access to the complete manual.</p>
