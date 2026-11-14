---
title: "ctie(1)"
name: "ctie"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ctie/"
description: "ctie – merge or apply CWEB change files"
---

<h2 class="name">NAME</h2>
<p> ctie &#8211; merge or apply CWEB change files </p>
<h2>SYNOPSIS</h2>
<p> <code>ctie</code> <code>-c</code>|<code>-m</code> <i>outputfile masterfile</i> <i>changefile</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>ctie</code> program is used to process multiple change files used with the CWEB system for literate programming. The CWEB programs allow one to apply patches to a source file (the <i>masterfile</i>) by means of a single change file. <code>ctie</code> can be used to either merge up to 32 change files into a single one or to apply the changes to the <i>masterfile</i> in order to create a new master file. Output of either the new change file or the patched master file goes into <i>outputfile</i>. Any include files (indicated using the CWEB <code>@i</code> command) are fully expanded during <code>ctie</code> processing, which means that the change files are able to modify the contents of any included files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Create a single change file from the given <i>changefile</i>s.</p>
<dt><code>-m</code></p>
<dd> Create a new master file by applying the given <i>changefile</i>s.</dl>
<h2>ENVIRONMENT</h2>
<p> The environment variable CWEBINPUTS is used to search for the input files, or the system default if CWEBINPUTS is not set. See <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) for the details of the searching. To avoid conflicts with other programs that also use the CWEBINPUTS environment, you can be more specific and use CWEBINPUTS_ctie for special requirements in CTIE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cweb/">cweb</a></code>(1), <i>ctiedoc.tex</i>, <code><a href="/docs/linux/man/1-tie/">tie</a></code>(1), <code><a href="/docs/linux/man/1-web/">web</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> Julian Gilbey, jdg [at] debian.org. The original TIE program was by Klaus Guntermann, TH Darmstadt, Institut f. Theoretische Informatik. The TIE man page was by Joachim Schnitter, TH Darmstadt, Phys. Chemie I, and was modified for CTIE by Julian Gilbey. </p>
<h2>Index</h2>
