---
title: "gforth(1)"
name: "gforth"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gforth/"
description: "gforth, gforth-fast, gforthmi – a fast and portable Forth system"
---

<h2>NAME</h2>
<p> gforth, gforth-fast, gforthmi &#8211; a fast and portable Forth system</p>
<h2>SYNOPSIS</h2>
<p> gforth [initialization options] [image-specific options] gforth-fast [initialization options] [image-specific options] </p>
<p> gforthmi <i>filename</i> [initialization options] [image-specific options]</p>
<h2>DESCRIPTION</h2>
<p> <code>GForth</code> is a fast and portable implementation of the Forth programming language. For details read the manual.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> GFORTHPATH contains the search path for source and image files. </p>
<p> GFORTHD gives the gforth executable used by gforthmi for creating the base images. It should be a double indirect threaded system. Default: gforth-ditc. </p>
<p> GFORTH gives the gforth executable used by gforthmi for computing the relocatable image from the base images. Default: gforth. </p>
<p> GFORTHHIST gives the location of the history file used by gforth to allow command-line recall. Default: $HOME. (The history file is named .gforth-history). </p>
<h2>EXAMPLES</h2>
<p> gforth </p>
<p> starts the system and goes into interactive mode. </p>
<p> gforth file1 file2 -e bye </p>
<p> loads and interprets the files file1 and file2, then exits. </p>
<p> gforth-fast </p>
<p> is the same as gforth, except that it does not support accurate backtraces for signals, and is faster by up to a factor of 2. Use it for debugged, performance-critical programs such as benchmarks. </p>
<p> gforthmi asm.fi -m 1M asm.fs </p>
<p> creates an image asm.fi that has a default dictionary size of 1MB and has the file asm.fs loaded. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code> </p>
<dl>
<dt><code>-h</code><i></p>
<dd> Lists the available options, including some not described here (see also the manual).</p>
<dt></i><code>&#8211;image-file </code><i>file</i></p>
<dd>
<dt><code>-i </code><i>file</p>
<dd> Loads the Forth image file</i> instead of the default gforth.fi.</p>
<dt><code>&#8211;path </code><i>path</i></p>
<dd>
<dt><code>-p </code><i>path</p>
<dd> Uses path</i> for searching the image file and Forth source code files instead of the default in the environment variable GFORTHPATH or the path specified at installation time (typically /usr/local/lib/gforth:.. A path is given as a <code>:</code>-separated list.</p>
<dt><code>&#8211;dictionary-size </code><i>size</i></p>
<dd>
<dt><code>-m </code><i>size</p>
<dd> Allocate size</i> space for the Forth dictionary space instead of using the default specified in the image (typically 256K). The <i>size</i> specification consists of an integer and a unit (e.g., 4M). The unit can be one of b (bytes), e (element size, in this case Cells), k (kilobytes), and M (Megabytes). If no unit is specified, e is used.</p>
<dt><code>&#8211;data-stack-size </code><i>size</i></p>
<dd>
<dt><code>-d </code><i>size</p>
<dd> Allocate size</i> space for the data stack instead of using the default specified in the image (typically 16K).</p>
<dt><code>&#8211;return-stack-size </code><i>size</i></p>
<dd>
<dt><code>-r </code><i>size</p>
<dd> Allocate size</i> space for the return stack instead of using the default specified in the image (typically 16K).</p>
<dt><code>&#8211;fp-stack-size </code><i>size</i></p>
<dd>
<dt><code>-f </code><i>size</p>
<dd> Allocate size</i> space for the floating point stack instead of using the default specified in the image (typically 16K). In this case the unit specifier e refers to floating point numbers.</p>
<dt><code>&#8211;locals-stack-size </code><i>size</i></p>
<dd>
<dt><code>-l </code><i>size</p>
<dd> Allocate size</i> space for the locals stack instead of using the default specified in the image (typically 16K). </p>
<dt><code>&#8211;evaluate </code><i>forth</i></p>
<dd>
<dt><code>-e </code><i>forth</p>
<dd> Evaluates the forth</i> code. This option takes only one argument; if you want to evaluate more Forth words, you have to quote them or use several -es. To exit after processing the command line (instead of entering interactive mode) append -e bye to the command line. This is an image-specific option of the default image.</dl>
<h2>FILES</h2>
<pre>
.../gforth.fi    default Forth image
*.fi             Forth loadable image
*.fs             Forth source (sequential)
*.fb             Forth source (block)
*.fd             generated with makedoc.fs
*.i              C include files
*.ds             documentation source
*TAGS            etags files
</pre>
<h2>SEE ALSO</h2>
<p> The Gforth manual &#8211; available in hypertext (Info, HTML) and printable (TeX, PS, ASCII) forms. </p>
<p> The ANSI document X3.215-1994 (i.e., the ANS Forth standard). </p>
<p> More information on Gforth (e.g., pointers to new versions, to the manual on the WWW and to papers about Gforth) is available through <a rel="nofollow" href="http://www.complang.tuwien.ac.at/projects/forth.html.">http://www.complang.tuwien.ac.at/projects/forth.html.</a></p>
<h2>AUTHORS</h2>
<p> <code>Gforth</code> was written by Anton Ertl, Bernd Paysan, Jens Wilke and others. </p>
<h2>Index</h2>
