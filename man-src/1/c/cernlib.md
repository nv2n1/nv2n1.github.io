---
title: "cernlib(1)"
name: "cernlib"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cernlib/"
description: "cernlib – print CERN library dependencies"
---

<h2 class="name">NAME</h2>
<p> cernlib &#8211; print CERN library dependencies </p>
<h2>SYNOPSIS</h2>
<p> <code>cernlib</code> [<i>options</i>]<i> libraries</i></p>
<h2>DESCRIPTION</h2>
<p> <code>cernlib</code> is a tool to list the compiler and linker options necessary to compile a CERNLIB program that has the given library dependencies. It is generally used within a command substitution, as in the following example: </p>
<p> gfortran -o myprogram myprogram.F `cernlib -G Motif pawlib` </p>
<p> This version of cernlib has been completely rewritten from the original script provided by CERN. It now does recursive library dependency checking and removes duplicate entries. </p>
<p> Note that by default, the cernlib script assumes that the CERN libraries are to be linked against statically; if the environment variables $CERN or $CERN_ROOT are specified, it looks for the libraries only in the &quot;lib&quot; subdirectory of those locations, not any &quot;shlib&quot; subdirectory. Furthermore, the script brackets the CERN libraries with linker instructions to link statically. This is done to preserve the original upstream behavior, in which all CERNLIB libraries exist only in static form. For instance, &quot;cernlib packlib&quot; outputs: </p>
<p> -Wl,-static -lpacklib -lkernlib -Wl,-dy -lm -lnsl -lcrypt -ldl -lg2c </p>
<p> If you want to link against ALL libraries (including CERNLIB) either statically or dynamically, call the cernlib script with its -safe flag to omit these bracketing linker flags. That is: if you want to link against all libraries (not just CERNLIB) statically, use the -static compiler flag and call cernlib with its -safe flag: </p>
<p> gfortran -o myprogram myprogram.F -static `cernlib -safe -G Motif pawlib` </p>
<p> and if you want to link against all libraries (including the CERN libraries) dynamically, use the same command without the -static compiler flag (the linker assumes dynamic linking by default): </p>
<p> gfortran -o myprogram myprogram.F `cernlib -safe -G Motif pawlib`</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a </code><i>arch</i></p>
<dd> Specify a system architecture, e.g. Linux (default), AIX, HP-UX, etc.</p>
<dt><code>-dy</code></p>
<dd> Equivalent to -safe; for backwards compatibility.</p>
<dt><code>-G </code><i>driver</i></p>
<dd> Specify a graphics driver. The available options on Linux are X11 and Motif (the latter option will also work when the Lesstif library is present).</p>
<dt><code>-P, -s</code></p>
<dd> Ignored; for backwards compatibility.</p>
<dt><code>-safe</code></p>
<dd> Do not make any assumptions about whether the CERN libraries should be linked against dynamically or statically. (The default behavior, if this flag is not used, is to link them statically.)</p>
<dt><code>-u</code></p>
<dd> Do not include architecture-specific libraries in the output.</p>
<dt><code>-v </code><i>version</i></p>
<dd> Specify version of $CERN_LEVEL. This is meaningless unless you have installed an upstream version of CERNLIB (i.e. not packaged by Debian); see the file <i>/usr/share/doc/cernlib-base/README.Debian</i>.</p>
<dt><code>-?, &#8211;help</code></p>
<dd> Show a summary of options.</p>
<dt><code>&#8212;</code></p>
<dd> Tell cernlib that this marks the end of cernlib-specific flags, and all following arguments are to be parsed as described in the <code>LIBRARIES</code> section below. If &#8212; is not given, the first word parsed as a library name will be the first word not starting with a hyphen &quot;-&quot; that is not an argument to a preceding cernlib flag.</dl>
<h2>LIBRARIES</h2>
<p> The following library names are recognized by this version of the cernlib script. These names may be used exactly as shown here, or prefixed by &quot;-l&quot;.</p>
<dl>
<dt><code>Core CERN libraries</code></p>
<dd> mathlib, packlib, kernlib</p>
<dt><code>Graphics and PAW libraries</code></p>
<dd> graflib, pawlib</p>
<dt><code>Monte Carlo and GEANT libraries</code></p>
<dd> cojets, eurodec, geant321, herwig59, isajet758, pdflib804, photos202, phtools</p>
<dt><code>Additional Monte Carlo libraries</code></p>
<dd> (to obtain these, see /usr/share/doc/montecarlo-base/README.Debian)<br />
 ariadne, ariadne-p5, fritiof, jetset, lepto, pythia5, pythia6</p>
<dt><code>Aliases</code></p>
<dd> The numerals at the end may be left off most of the library names above.</p>
<dt><code>Other library names</code></p>
<dd> Various other names are recognized for backwards compatibility, internal use, and non-Linux architectures. For the complete list, please see the cernlib script.</p>
<dt><code>Other</code></p>
<dd> Any names not recognized by cernlib that start with &quot;-l&quot; or with any character other than a hyphen (&quot;-&quot;) are output as -l${name#-l} (<i>i.e.</i>, are assumed to be a library). Names starting with a hyphen for which the second character is not &quot;l&quot; are assumed to be compiler flags, and are output at the beginning of the line before all other output.</dl>
<h2>SEE ALSO</h2>
<p> <i>/usr/share/doc/cernlib-base/README.Debian</i> describes some of the changes that have been made to the CERN libraries in order to comply with Debian policy and the Filesystem Hierarchy Standard. </p>
<p> CERNLIB documentation for all related libraries and programs is available at the following URL: <i><a rel="nofollow" href="http://cern.ch/cernlib/">http://cern.ch/cernlib/</a></i></p>
<h2>AUTHOR</h2>
<p> This manual page and the version of the cernlib script that it describes were written by Kevin McCarty &lt;kmccarty [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others). They are licensed under the GNU General Public License, version 2 or later (at your choice).</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) Kevin B. McCarty, 2002, 2003, 2004, 2005, 2006. </p>
<h2>Index</h2>
