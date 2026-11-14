---
title: "kuipc(1)"
name: "kuipc"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kuipc/"
description: "kuipc – the CERN KUIP compiler"
---

<h2 class="name">NAME</h2>
<p> kuipc &#8211; the CERN KUIP compiler </p>
<h2>SYNOPSIS</h2>
<p> <code>kuipc</code> [ <i>options</i> ] [ <i>inputfile</i> [ <i>outputfile</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> <code>kuipc</code>, the Kit for a User Interface Package Compiler, is a tool to simplify the writing of a program&#8217;s user interface code. It takes as input a Command Definition File (CDF) that describes the commands to be understood by the program, and outputs C or FORTRAN code that makes the appropriate function calls to set up the user interface. This code can then be compiled and linked with the rest of the program. Since the generated code uses KUIP routines, the program must also be linked against the Packlib library that contains them. </p>
<p> If no output file is specified, kuipc will output generated code to a file whose name is the same as the input file&#8217;s, with the ending &#8216;.cdf&#8217; replaced by &#8216;.f&#8217; or &#8216;.c&#8217; as appropriate. If neither input nor output file are given, kuipc will prompt for them. Be careful because kuipc overwrites existing files with no warning.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Generate C code.</p>
<dt><code>-f</code></p>
<dd> Generate FORTRAN code (the default).</p>
<dt><code>-split</code></p>
<dd> Output several files, one for each time the &gt;Name control line is used in the CDF input. The names of the output files will correspond to the arguments given on the &gt;Name control lines.</dl>
<h2>SEE ALSO</h2>
<p> The KUIP manual: <a rel="nofollow" href="http://wwwasdoc.web.cern.ch/wwwasdoc/psdir/kuip.ps.gz">http://wwwasdoc.web.cern.ch/wwwasdoc/psdir/kuip.ps.gz</a> </p>
<h2>BUGS</h2>
<p> When the -split option is used, kuipc will still create an output file that it would have made if -split was not used; the file will be of zero size.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Kevin McCarty &lt;kmccarty [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
