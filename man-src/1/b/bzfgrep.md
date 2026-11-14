---
title: "bzfgrep(1)"
name: "bzfgrep"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bzfgrep/"
description: "bzgrep, bzfgrep, bzegrep – search possibly bzip2 compressed files for a regular expression"
---

<h2 class="name">NAME</h2>
<p> bzgrep, bzfgrep, bzegrep &#8211; search possibly bzip2 compressed files for a regular expression </p>
<h2>SYNOPSIS</h2>
<p> <code>bzgrep</code> [ grep_options ] <code>[&nbsp;-e&nbsp;]</code><i> pattern</i> <i>filename</i>&#8230;<br />
 <code>bzegrep</code> [ egrep_options ] <code>[&nbsp;-e&nbsp;]</code><i> pattern</i> <i>filename</i>&#8230;<br />
 <code>bzfgrep</code> [ fgrep_options ] <code>[&nbsp;-e&nbsp;]</code><i> pattern</i> <i>filename</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <i>Bzgrep</i> is used to invoke the <i>grep</i> on bzip2-compressed files. All options specified are passed directly to <i>grep.</i> If no file is specified, then the standard input is decompressed if necessary and fed to grep. Otherwise the given files are uncompressed if necessary and fed to <i>grep.</i> </p>
<p> If <i>bzgrep</i> is invoked as <i>bzegrep</i> or <i>bzfgrep</i> then <i>egrep</i> or <i>fgrep</i> is used instead of <i>grep.</i> If the GREP environment variable is set, <i>bzgrep</i> uses it as the <i>grep</i> program to be invoked. For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for sh:&nbsp;<wbr>&nbsp;GREP=fgrep&nbsp;<wbr>&nbsp;bzgrep string files<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for csh:&nbsp;(setenv GREP fgrep;&nbsp;bzgrep string files)</p>
<h2>AUTHOR</h2>
<p> Charles Levert (charles [at] comm.polymtl.ca). Adapted to bzip2 by Philippe Troin &lt;phil [at] fifi.org&gt; for Debian GNU/Linux.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-grep/">grep</a>(1), <a href="/docs/linux/man/1-egrep/">egrep</a>(1), <a href="/docs/linux/man/1-fgrep/">fgrep</a>(1), <a href="/docs/linux/man/1-bzdiff/">bzdiff</a>(1), <a href="/docs/linux/man/1-bzmore/">bzmore</a>(1), <a href="/docs/linux/man/1-bzless/">bzless</a>(1), <a href="/docs/linux/man/1-bzip2/">bzip2</a>(1) </p>
<h2>Index</h2>
