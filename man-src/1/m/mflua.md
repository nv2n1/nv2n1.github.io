---
title: "mflua(1)"
name: "mflua"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mflua/"
description: "mflua, mflua-nowin, mfluajit, mfluajit-nowin – implementation of META-FONT with Lua embedded for better extraction of information from METAFONT."
---

<h2 class="name">NAME</h2>
<p> mflua, mflua-nowin, mfluajit, mfluajit-nowin &#8211; implementation of META-FONT with Lua embedded for better extraction of information from METAFONT. </p>
<h2>SYNOPSIS</h2>
<p> <code>mflua</code> [<i>,OPTION/</i>]&#8230; [<i>,MFNAME/</i>[<i>,.mf/</i>]] [<i>,COMMANDS/</i>]<br />
 <code>mflua</code> [<i>,OPTION/</i>]&#8230; <i>,FIRST-LINE/</i><br />
 <code>mflua</code> [<i>,OPTION/</i>]&#8230; <i>,&amp;BASE ARGS/</i></p>
<h2>DESCRIPTION</h2>
<dl>
<dt>
<dd> Run MFLua on MFNAME, usually creating MFNAME.tfm and MFNAME.NNNNgf, where NNNN is the resolution of the specified mode (2602 by default). Any following COMMANDS are processed as Metafont input, after MFNAME is read. If the first line of MFNAME is %&amp;BASE, and BASE is an existing .base file, use it. Else use `NAME.base&#8217;, where NAME is the program invocation name, most commonly `mf&#8217;.</p>
<dt>
<dd> Alternatively, if the first non-option argument begins with a backslash, interpret all non-option arguments as a line of Metafont input.</p>
<dt>
<dd> Alternatively, if the first non-option argument begins with a &amp;, the next word is taken as the BASE to read, overriding all else. Any remaining arguments are processed as above.</p>
<dt>
<dd> If no arguments or options are specified, prompt for input.</dl>
<p> <code>-base</code>=<i>,BASENAME/</i> use BASENAME instead of program name or a %&amp; line </p>
<p> <code>[-no]-file-line-error</code> disable/enable file:line:error style messages </p>
<p> <code>-halt-on-error</code> stop processing at the first error </p>
<p> <code>-ini</code> be inimf, for dumping bases; this is implicitly true if the program name is `inimf&#8217; </p>
<p> <code>-interaction</code>=<i>,STRING/</i> set interaction mode (STRING=batchmode/nonstopmode/scrollmode/errorstopmode) </p>
<p> <code>-jobname</code>=<i>,STRING/</i> set the job name to STRING </p>
<p> <code>-kpathsea-debug</code>=<i>,NUMBER/</i> set path searching debugging flags according to the bits of NUMBER </p>
<p> <code>[-no]-mktex</code>=<i>,FMT</i> disable/enable mktexFMT generation (FMT=mflua) </p>
<p> <code>-output-directory</code>=<i>,DIR/</i> use existing DIR as the directory to write files in </p>
<p> <code>[-no]-parse-first-line</code> disable/enable parsing of first line of input file </p>
<p> <code>-progname</code>=<i>,STRING/</i> set program (and base) name to STRING </p>
<p> <code>-recorder</code> enable filename recorder </p>
<p> <code>-translate-file</code>=<i>,TCXNAME/</i> use the TCX file TCXNAME </p>
<p> <code>-8bit</code> make all characters printable by default </p>
<p> <code>-help</code> display this help and exit </p>
<p> <code>-version</code> output version information and exit</p>
<h2>REPORTING BUGS</h2>
<p> Email bug reports to luigi.scarso [at] gmail.com. </p>
<p> kpathsea version 6.3.2<br />
 Copyright 2020 L. Scarso.<br />
 There is NO warranty. Redistribution of this software is covered by the terms of both the MFLua copyright and the Lesser GNU General Public License.<br />
 For more information about these matters, see the file named COPYING and the MFLua source.<br />
 Primary author of MFLua: L. Scarso. </p>
<h2>Index</h2>
