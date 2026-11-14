---
title: "netatalk-config(1)"
name: "netatalk-config"
section: "1"
letter: "n"
url: "/docs/linux/man/1-netatalk-config/"
description: "netatalk-config – script to get information about the installed version of netatalk"
---

<h2 class="name">NAME</h2>
<p> netatalk-config &#8211; script to get information about the installed version of netatalk </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>netatalk-config</code> [&#8211;prefix&nbsp;<wbr>[<i>=DIR</i>]] [&#8211;exec_prefix&nbsp;<wbr>[<i>=DIR</i>]] [&#8211;help] [&#8211;version] [&#8211;libs] [&#8211;libs-dirs] [&#8211;libs-names] [&#8211;cflags] [&#8211;macros]</dl>
<h2>DESCRIPTION</h2>
<p> <code>netatalk-config</code></p>
<dd>is a tool that is used to determine the compiler and linker flags that should be used to compile and link programs that use the <i>netatalk</i> run-time libraries.</p>
<h2>OPTIONS</h2>
<p> <code>netatalk-config</code> accepts the following options: </p>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help for this command and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the currently installed version of <i>netatalk</i> on the standard output.</dl>
<p> <code>&#8211;libs</code></p>
<dl>
<dt>
<dd> Print the linker flags that are necessary to link against the <i>netatalk</i> run-time libraries.</dl>
<p> <code>&#8211;libs-dirs</code></p>
<dl>
<dt>
<dd> Print only the -l/-R part of &#8211;libs.</dl>
<p> <code>&#8211;libs-names</code></p>
<dl>
<dt>
<dd> Print only the -l part of &#8211;libs.</dl>
<p> <code>&#8211;cflags</code></p>
<dl>
<dt>
<dd> Print the compiler flags that are necessary to compile a program linked against the <i>netatalk</i> run-time libraries.</dl>
<p> <code>&#8211;macros</code></p>
<dl>
<dt>
<dd> Print the <i>netatalk</i> m4 directory.</dl>
<p> <code>&#8211;prefix=PREFIX</code></p>
<dl>
<dt>
<dd> If specified, use PREFIX instead of the installation prefix that <i>netatalk</i> was built with when computing the output for the &#8211;cflags and &#8211;libs options. This option is also used for the exec prefix if &#8211;exec-prefix was not specified. This option must be specified before any &#8211;libs or &#8211;cflags options.</dl>
<p> <code>&#8211;exec\_prefix=PREFIX</code></p>
<dl>
<dt>
<dd> If specified, use PREFIX instead of the installation exec prefix that <i>netatalk</i> was built with when computing the output for the &#8211;cflags and &#8211;libs options. This option must be specified before any &#8211;libs or &#8211;cflags options.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1998 Owen Taylor </p>
<p> Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. </p>
<p> Man page adapted for <code>netatalk-config</code> by Sebastian Rittau in 2001. </p>
<h2>Index</h2>
