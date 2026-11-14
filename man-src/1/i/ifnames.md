---
title: "ifnames(1)"
name: "ifnames"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ifnames/"
description: "ifnames – Extract CPP conditionals from a set of files"
---

<h2 class="name">NAME</h2>
<p> ifnames &#8211; Extract CPP conditionals from a set of files </p>
<h2>SYNOPSIS</h2>
<p> <code>ifnames</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Scan all of the C source FILES (or the standard input, if none are given) and write to the standard output a sorted list of all the identifiers that appear in those files in &#8216;#if&#8217;, &#8216;#elif&#8217;, &#8216;#ifdef&#8217;, or &#8216;#ifndef&#8217; directives. Print each identifier on a line, followed by a space-separated list of the files in which that identifier occurs.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> print this help, then exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> print version number, then exit</dl>
<h2>AUTHOR</h2>
<p> Written by David J. MacKenzie and Paul Eggert.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-autoconf [at] gnu.org&gt;.<br />
 GNU Autoconf home page: &lt;<a rel="nofollow" href="https://www.gnu.org/software/autoconf/">https://www.gnu.org/software/autoconf/</a>&gt;.<br />
 General help using GNU software: &lt;<a rel="nofollow" href="https://www.gnu.org/gethelp/">https://www.gnu.org/gethelp/</a>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021 Free Software Foundation, Inc. License GPLv3+/Autoconf: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;, &lt;<a rel="nofollow" href="https://gnu.org/licenses/exceptions.html">https://gnu.org/licenses/exceptions.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-autoconf/">autoconf</a></code>(1), <code><a href="/docs/linux/man/1-automake/">automake</a></code>(1), <code><a href="/docs/linux/man/1-autoreconf/">autoreconf</a></code>(1), <code><a href="/docs/linux/man/1-autoupdate/">autoupdate</a></code>(1), <code><a href="/docs/linux/man/1-autoheader/">autoheader</a></code>(1), <code><a href="/docs/linux/man/1-autoscan/">autoscan</a></code>(1), <code><a href="/docs/linux/man/1-config-guess/">config.guess</a></code>(1), <code><a href="/docs/linux/man/1-config-sub/">config.sub</a></code>(1), <code><a href="/docs/linux/man/1-ifnames/">ifnames</a></code>(1), <code><a href="/docs/linux/man/1-libtool/">libtool</a></code>(1). </p>
<p> The full documentation for <code>ifnames</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>ifnames</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info ifnames</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
