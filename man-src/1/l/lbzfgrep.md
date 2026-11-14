---
title: "lbzfgrep(1)"
name: "lbzfgrep"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lbzfgrep/"
description: "lbzgrep – search possibly compressed files for a regular expression"
---

<h2>NAME</h2>
<p> lbzgrep &#8211; search possibly compressed files for a regular expression</p>
<h2>SYNOPSIS</h2>
<p> <code>lbzgrep</code> [ grep_options ] <code>[&nbsp;<wbr>-e&nbsp;<wbr>]</code><i> pattern</i> <i>filename</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <i>Zgrep</i> invokes <i>grep</i> on compressed or lbzip2ped files. All options specified are passed directly to <i>grep</i>. If no file is specified, then the standard input is decompressed if necessary and fed to grep. Otherwise the given files are uncompressed if necessary and fed to <i>grep</i>. </p>
<p> If the GREP environment variable is set, <i>lbzgrep</i> uses it as the <i>grep</i> program to be invoked.</p>
<h2>EXIT STATUS</h2>
<p> Exit status is 0 for a match, 1 for no matches, and 2 if trouble.</p>
<h2>BUGS</h2>
<p> The following <i>grep</i> options are not supported: <code>&#8211;dereference-recursive</code> (<code>-R</code>), <code>&#8211;directories</code> (<code>-d</code>), <code>&#8211;exclude</code>, <code>&#8211;exclude-from</code>, <code>&#8211;exclude-dir</code>, <code>&#8211;include</code>, <code>&#8211;null</code> (<code>-Z</code>), <code>&#8211;null-data</code> (<code>-z</code>), and <code>&#8211;recursive</code> (<code>-r</code>).</p>
<h2>AUTHOR</h2>
<p> Charles Levert (charles [at] comm.polymtl.ca)</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-grep/">grep</a>(1), <a href="/docs/linux/man/1-lbzexe/">lbzexe</a>(1), <a href="/docs/linux/man/1-lbzip2/">lbzip2</a>(1), <a href="/docs/linux/man/1-lbzdiff/">lbzdiff</a>(1), <a href="/docs/linux/man/1-lbzforce/">lbzforce</a>(1), <a href="/docs/linux/man/1-lbzmore/">lbzmore</a>(1) </p>
<h2>Index</h2>
