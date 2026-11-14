---
title: "autoheader(1)"
name: "autoheader"
section: "1"
letter: "a"
url: "/docs/linux/man/1-autoheader/"
description: "autoheader – Create a template header for configure"
---

<h2 class="name">NAME</h2>
<p> autoheader &#8211; Create a template header for configure </p>
<h2>SYNOPSIS</h2>
<p> <code>autoheader</code> [<i>,OPTION/</i>]&#8230; [<i>,TEMPLATE-FILE/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Create a template file of C &#8216;#define&#8217; statements for &#8216;configure&#8217; to use. To this end, scan TEMPLATE-FILE, or &#8216;configure.ac&#8217; if present, or else &#8216;configure.in&#8217;.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> print this help, then exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> print version number, then exit</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> verbosely report processing</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> don&#8217;t remove temporary files</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> consider all files obsolete</p>
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
<h3>Library directories:</h3>
<dl>
<dt><code>-B</code>, <code>&#8211;prepend-include</code>=<i>,DIR/</i></p>
<dd> prepend directory DIR to search path</p>
<dt><code>-I</code>, <code>&#8211;include</code>=<i>,DIR/</i></p>
<dd> append directory DIR to search path</dl>
<h2>AUTHOR</h2>
<p> Written by Roland McGrath and Akim Demaille.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-autoconf [at] gnu.org&gt;.<br />
 GNU Autoconf home page: &lt;<a rel="nofollow" href="https://www.gnu.org/software/autoconf/">https://www.gnu.org/software/autoconf/</a>&gt;.<br />
 General help using GNU software: &lt;<a rel="nofollow" href="https://www.gnu.org/gethelp/">https://www.gnu.org/gethelp/</a>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021 Free Software Foundation, Inc. License GPLv3+/Autoconf: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;, &lt;<a rel="nofollow" href="https://gnu.org/licenses/exceptions.html">https://gnu.org/licenses/exceptions.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-autoconf/">autoconf</a></code>(1), <code><a href="/docs/linux/man/1-automake/">automake</a></code>(1), <code><a href="/docs/linux/man/1-autoreconf/">autoreconf</a></code>(1), <code><a href="/docs/linux/man/1-autoupdate/">autoupdate</a></code>(1), <code><a href="/docs/linux/man/1-autoheader/">autoheader</a></code>(1), <code><a href="/docs/linux/man/1-autoscan/">autoscan</a></code>(1), <code><a href="/docs/linux/man/1-config-guess/">config.guess</a></code>(1), <code><a href="/docs/linux/man/1-config-sub/">config.sub</a></code>(1), <code><a href="/docs/linux/man/1-ifnames/">ifnames</a></code>(1), <code><a href="/docs/linux/man/1-libtool/">libtool</a></code>(1). </p>
<p> The full documentation for <code>autoheader</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>autoheader</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info autoheader</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
