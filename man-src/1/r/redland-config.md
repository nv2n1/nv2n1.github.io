---
title: "redland-config(1)"
name: "redland-config"
section: "1"
letter: "r"
url: "/docs/linux/man/1-redland-config/"
description: "redland-config – script to get information about the installed version of Redland"
---

<h2 class="name">NAME</h2>
<p> redland-config &#8211; script to get information about the installed version of Redland </p>
<h2>SYNOPSIS</h2>
<p> <code>redland-config</code> [&#8211;cflags] [&#8211;help] [&#8211;libs] [&#8211;libtool-libs] [&#8211;prefix<i>[=DIR]</i>] [&#8211;private-libs] [&#8211;version-decimal] [&#8211;version]</p>
<h2>DESCRIPTION</h2>
<p> <i>redland-config</i> is a tool that is used to determine the compile and linker flags that should be used to compile and link programs that use the Redland RDF library.</p>
<h2>OPTIONS</h2>
<p> <i>redland-config</i> accepts the following options:</p>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Print the currently installed version of redland on the standard output.</p>
<dt><code>&#8211;version-decimal</code></p>
<dd> Print the currently installed version of redland as a decimal integer.</p>
<dt><code>&#8211;libs</code></p>
<dd> Print the linker flags that are necessary to link a redland program. This excludes linker arguments used to build the librdf shared library.</p>
<dt><code>&#8211;libtool-libs</code></p>
<dd> Print the flags that are necessary to link a redland program with libtool.</p>
<dt><code>&#8211;private-libs</code></p>
<dd> Print the linker flags that are necessary to build the librdf shared library. This option is not usually needed because the librdf shared library has already been dynamically linked against these libs.</p>
<dt><code>&#8211;cflags</code></p>
<dd> Print the compiler flags that are necessary to compile a redland program.</p>
<dt><code>&#8211;prefix=PREFIX</code></p>
<dd> If specified, use PREFIX instead of the installation prefix that redland was built with when computing the output for the &#8211;cflags and &#8211;libs options. This option must be specified before any &#8211;libs or &#8211;cflags options.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-redland/">redland</a></code>(3),</p>
<h2>AUTHOR</h2>
<p> Dave Beckett &#8211; <a rel="nofollow" href="http://www.dajobe.org/">http://www.dajobe.org/</a> </p>
<h2>Index</h2>
