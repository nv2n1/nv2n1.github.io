---
title: "xmkmf(1)"
name: "xmkmf"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmkmf/"
description: "xmkmf – create a Makefile from an Imakefile"
---

<h2>NAME</h2>
<p> xmkmf &#8211; create a Makefile from an Imakefile</p>
<h2>SYNOPSIS</h2>
<p> <code>xmkmf</code> [ -a ] [ <i>topdir</i> [ <i>curdir</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xmkmf</i> command is the normal way to create a <i>Makefile</i> from an <i>Imakefile</i> shipped with third-party software. </p>
<p> When invoked with no arguments in a directory containing an <i>Imakefile,</i> the <i>imake</i> program is run with arguments appropriate for your system (configured into <i>imake</i> when it was built) and generates a <i>Makefile.</i> </p>
<p> When invoked with the <i>-a</i> option, <i>xmkmf</i> builds the <i>Makefile</i> in the current directory, and then automatically executes &#8220;make Makefiles&#8221; (in case there are subdirectories), &#8220;make includes&#8221;, and &#8220;make depend&#8221; for you. </p>
<p> If a <i>topdir</i> is given, <i>xmkmf</i> assumes nothing is installed on your system and looks for files in the build tree instead of using the installed versions. Optionally, <i>curdir</i> may be specified as a relative pathname from the top of the build tree to the current directory. It is necessary to supply <i>curdir</i> if the current directory has subdirectories, or the <i>Makefile</i> will not be able to build the subdirectories.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-imake/">imake</a>(1) </p>
<h2>Index</h2>
