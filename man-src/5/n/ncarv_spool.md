---
title: "ncarv_spool(5)"
name: "ncarv_spool"
section: "5"
letter: "n"
url: "/docs/linux/man/5-ncarv_spool/"
description: "ncarv_spool – spooled device configuration table for interactive metafile translator ictrans"
---

<p>ncarv_spool &#8211; spooled device configuration table for interactive metafile translator <code>ictrans</code></p>
<h2>Synopsis</h2>
<p><code>$NCARG_ROOT/lib/ncarg/ncarv_spool</code><br />
 <code>~/.ncarv_spool</code></p>
<h2>Description</h2>
<p>The <code>ncarv_spool</code> file contains definitions for spooled devices to be used by <code>ictrans</code>. Each definition describes a rule used for sending a set of metafile frames to a spooled device. </p>
<p> Each entry consists of a line of the form:</p>
<dl>
<dd><i>alias_name </i><code>:</code><i> translator_args </i><code>:</code><i> filter_chain</i> </p>
<dt><i>alias_name</i></p>
<dd>an identifier unique to the file. It is the alias by which the definition may be referenced.</p>
<dt><i>translator_args</i></p>
<dd><i>translator_args</i> is a list of valid <code>ctrans</code> command line arguments to be passed to <code>ctrans</code>. Metafile frames are translated by <code>ctrans</code> and the output of this translation is made available for further processing as specified by the remaining spooler definition.</p>
<dt><i>filter_chain</i></p>
<dd>is a set of simple commands separated by the UNIX pipe symbol <code>|</code>. <i>filter_chain</i> may be terminated by the UNIX file redirection symbols <code>&gt; </code> or <code>&gt;&gt;</code> <i>filename</i>. Output from <code>ctrans</code> is made available to the processes defined in <i>filter_chain</i>.</dl>
<p> A pound-sign (<code>#</code>) as the first character indicates a comment line which is ignored by routines that read this file. The order of entries in <code>ncarv_spool</code> is important. If an alias name conflict arises the last definition encountered is given precedence. Any previous definition for the same alias name is discarded.</p>
<h2>Examples</h2>
<p>The following is an example <code>ncarv_spool</code> file. The first entry describes a device named <code>postscript</code>. When <code>postscript</code> is named as the spooling device, metafile frames are translated by <code>ctrans</code> into the format described by the <code>ps.mono</code> graphcap. The font <code>font1</code> is used for CGM text elements. The result of this translation will be piped to <code>lpr</code>. The second entry is named <code>dicomed</code>. The <code>dicomed </code> entry specifies that metafile frames will be rasterized at a 1857 by 1183 pixel resolution and output in X11 xwd format. The result of this rasterization is piped to a program <code>x11tonrif</code> which in turn sends its output to a program called <code>rasttg</code>. In the third example the final output is directed to a file called <code>sunfile</code>. </p>
<dl>
<dd>
<pre>#
# example ncarv_spool file
#
postscript : -d ps.mono -f font1 : | lpr -Pprinter0
dicomed : -d xwd -geom 1857x1183 : | x11tonrif | rasttg -tc
sunraster : -d xwd -geom 1152x900 : | x11tosun &gt; sunfile</pre>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>NCARG_ROOT</code></p>
<dd>Path to root of NCAR Graphics installation.</p>
<dt><code>NCARG_LIB</code></p>
<dd>If set this variable contains the path to the installed NCAR Graphics libraries. <code>NCARG_LIB</code> overrides <code>NCARG_ROOT</code>.</dl>
<h2>Files</h2>
<dl>
<dt>$NCARG_ROOT/lib/ncarg/ncarv_spool</p>
<dd>&#8211; System spooler configuration file</p>
<dt>$HOME/.ncarv_spool</p>
<dd>&#8211; User spooler configuration file</dl>
<h2>See Also</h2>
<p><code>ctrans(1NCARG)</code>, <code>ictrans(1NCARG)</code> </p>
<p> Hardcopy: NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research </p>
<p> The use of this Software is governed by a License Agreement.</p>
