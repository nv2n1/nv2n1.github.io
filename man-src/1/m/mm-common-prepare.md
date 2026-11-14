---
title: "mm-common-prepare(1)"
name: "mm-common-prepare"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mm-common-prepare/"
description: "mm-common-prepare – Prepare a C++ binding module to use mm-common"
---

<h2>NAME</h2>
<p> mm-common-prepare &#8211; Prepare a C++ binding module to use mm-common</p>
<h2>SYNOPSIS</h2>
<p> <code>mm-common-prepare</code> [<i>OPTION</i>]&#8230; [<i>SOURCE-DIR</i>]</p>
<h2>DESCRIPTION</h2>
<p> Run <code>mm-common-prepare</code> to install the <i>mm-common</i> build support files into the source tree of a C++ binding module. The exact location where these files will be installed can be influenced through special macros in the <i>configure.ac</i> file.</p>
<dl>
<dt><code>AC_CONFIG_AUX_DIR(</code><i>[AUX-DIR]</i><code>)</code></p>
<dd> The Automake include files are placed into the <i>AUX-DIR</i> subdirectory of the top-level source directory. If <code>AC_CONFIG_AUX_DIR</code> is not specified, the files are placed at the top-level of the module&#8217;s source tree.</p>
<dt><code>MM_CONFIG_DOCTOOL_DIR(</code><i>[DOCTOOL-DIR]</i><code>)</code></p>
<dd> If the <code>MM_CONFIG_DOCTOOL_DIR</code> macro is called with an explicit <i>DOCTOOL-DIR</i> argument, the common utilities required for generating and installing the reference documentation of a C++ binding module will be installed into the named subdirectory. If <code>MM_CONFIG_DOCTOOL_DIR</code> is not used or does not specify a <i>DOCTOOL-DIR</i> argument, <code>mm-common-prepare</code> will not install the documentation utility files into the module&#8217;s source tree. Instead, it is assumed that the module depends on <i>glibmm</i> and can use the installed documentation utilities that come with it.</dl>
<p> If no <i>SOURCE-DIR</i> argument has been specified on the command line, the current working directory will be used.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;copy</code></p>
<dd> copy files instead of creating symbolic links to them</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> forcefully replace existing files or symbolic links</p>
<dt><code>&#8211;help</code></p>
<dd> display a help message and exit</p>
<dt><code>&#8211;version</code></p>
<dd> show version information and exit</dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 if OK, or 1 if an error occurred.</p>
<h2>FILES</h2>
<p> The build support files currently installed by <code>mm-common-prepare</code> are listed below.</p>
<dl>
<dt><code>Automake include files installed into </code><i>AUX-DIR</i><code>:</code></p>
<dd>
<dt>
<dd> <i>compile-binding.am</i></p>
<dt>
<dd> <i>dist-changelog.am</i></p>
<dt>
<dd> <i>doc-reference.am</i></p>
<dt>
<dd> <i>generate-binding.am</i></p>
<dt><code>Documentation utilities installed into </code><i>DOCTOOL-DIR</i><code>:</code></p>
<dd>
<dt>
<dd> <i>doc-install.pl</i></p>
<dt>
<dd> <i>doc-postprocess.pl</i></p>
<dt>
<dd> <i>doxygen.css</i></p>
<dt>
<dd> <i>tagfile-to-devhelp2.xsl</i></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-autoreconf/">autoreconf</a></code>(1) </p>
<p> <i>/usr/share/doc/mm-common/README</i> </p>
<p> <i>/usr/share/doc/mm-common/skeletonmm.tar.gz</i> </p>
<h2>Index</h2>
