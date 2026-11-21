---
title: "gxint(1)"
name: "gxint"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gxint/"
description: "gxint – load and run an interactive GEANT application"
---

<h2>SYNOPSIS</h2>
<p> <code>gxint</code> [<i>options</i>]<i> file(s)</i></p>
<h2>DESCRIPTION</h2>
<p> <code>gxint</code> is a script to load and run a GEANT application, which is usually in the form of Fortran source code. The desired routines are given in <i>file(s)</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d </code><i>driver</i></dt>
<dd> Specify a graphics driver. The available options on Linux are X11 and Motif (which should also work with lesstif). X11 is the default.</dd>
<dt><code>-g </code><i>geant_version</i></dt>
<dd> Specify the version of GEANT to use. Current default is 3.21. This option only makes sense if you have installed a GEANT version other than 3.21 (i.e. one not packaged by Debian).</dd>
<dt><code>-h </code><i>host</i></dt>
<dd> Useful with the -d X11 option only. Specifies the hostname used for the display; syntax is identical with that of $DISPLAY. If no hostname is specified, the value of $DISPLAY is used.</dd>
<dt><code>-l </code><i>library</i></dt>
<dd> Specify additional libraries. This option may be repeated to add several libs.</dd>
<dt><code>-L </code><i>path</i></dt>
<dd> Additional loader search path. Useful if additional libraries are specified with -l option. This option may be repeated with more than one pathname.</dd>
<dt><code>-m</code></dt>
<dd> Do NOT use main program from cernlib area.</dd>
<dt><code>-o </code><i>outputfile</i></dt>
<dd> Do not immediately run GEANT, but instead produce an executable file named <i>outputfile</i>. If &quot;-o&quot; is not given, the executable file will be created in $HOME, named GEANT<i>pid</i> (<i>pid</i> being the process ID of <code>gxint</code>), and run automatically.</dd>
<dt><code>-v </code><i>version</i></dt>
<dd> Specify version of $CERN_LEVEL. This is meaningless unless you have installed an upstream version of CERNLIB (i.e. not packaged by Debian); see the file <i>/usr/share/doc/cernlib-base/README.Debian</i>.</dd>
<dt><code>-?, &#8211;help</code></dt>
<dd> Show a summary of options.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cernlib/">cernlib</a></code>(1) &#8211; script to list required -l and -L options given a list of CERN libraries </p>
<p> <i>/usr/share/doc/cernlib-base/README.Debian</i> describes how one might use the -v flag with Debian&#8217;s versions of the cernlib and gxint scripts if one has an upstream version of CERNLIB installed. </p>
<p> CERNLIB documentation for all related libraries and programs is available at the following URL: <i><a rel="nofollow" href="http://cern.ch/cernlib/">http://cern.ch/cernlib/</a></i></p>
<h2>AUTHOR</h2>
<p> This manual page was written by Kevin McCarty &lt;kmccarty [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others).</p>
<h2>COPYRIGHT</h2>
<p> This manual page is (C) Copyright Kevin McCarty, 2002, 2003, 2004, 2005. </p>
