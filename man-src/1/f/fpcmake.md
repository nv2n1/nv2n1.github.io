---
title: "fpcmake(1)"
name: "fpcmake"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fpcmake/"
description: "fpcmake – The Free Pascal makefile constructor program."
---

<h2>NAME</h2>
<p> fpcmake &#8211; The Free Pascal makefile constructor program. </p>
<h2>SYNOPSIS</h2>
<p> <code>fpcmake [-Ttarget] [-pwhrqvV] [filename [filename [filename]]]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>fpcmake</code> reads a <i>Makefile.fpc</i> and converts it to a <i>Makefile</i> suitable for reading by GNU <i>make</i> to compile your projects. It is similar in functionality to GNU <i>autoconf </i> or <i>Imake</i> for making X projects. </p>
<h2>USAGE</h2>
<p> <code>fpcmake</code> accepts filenames of makefile description files as it&#8217;s command-line arguments. For each of these files it will create a <i>Makefile </i> in the same directory where the file is located, overwriting any existing file with the same name. </p>
<p> If no options are given, it just attempts to read the file <i>Makefile.fpc</i> in the current directory and tries to construct a Makefile from it. any previously existing <i>Makefile</i> will be erased. See <code><a href="/docs/linux/man/5-fpcmake/">fpcmake</a></code>(5) for a description of the format of the <i>Makefile.fpc</i> file. </p>
<h2>OPTIONS</h2>
<p> fpcmake has a small number of options to control it&#8217;s behaviour: </p>
<dl>
<dt><code>-h</code></p>
<dd> Emit a short help text describing the use of <code>fpcmake</code></p>
<dt><code>-p</code></p>
<dd> If this option is given, a package description file is generated as well as a makefile.</p>
<dt><code>-q</code></p>
<dd> Tells <code>fpcmake</code> to be more quiet, i.e. emit less messages.</p>
<dt><code>-r</code></p>
<dd> If this option is given, <code>fpcmake</code> will recursively scan subdirectories for <code>makefile.fpc</code> files and generate makefiles for them.</p>
<dt><code>-T</code></p>
<dd> Specifies the targets for which <code>fpcmake </code> should generate makefiles. This can be a comma-separated list of target systems, or the special identifier <i>all</i> which indicates that a makefile should be generated for all supported platforms.</p>
<dt><code>-v</code></p>
<dd> This option instructs <code>fpcmake</code> to be more verbose.</p>
<dt><code>-V</code></p>
<dd> Print <code>fpcmake</code> version and exit.</p>
<dt><code>-w</code></p>
<dd> This is the standard option and tells <code>fpcmake</code> to generate a makefile. </p>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/5-fpcmake/">fpcmake</a></code>(5) <code><a href="/docs/linux/man/1-ppc386/">ppc386</a></code>(1) <code><a href="/docs/linux/man/1-make/">make</a></code>(1) </p>
</dl>
<h2>Index</h2>
