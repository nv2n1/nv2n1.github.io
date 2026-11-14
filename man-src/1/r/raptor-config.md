---
title: "raptor-config(1)"
name: "raptor-config"
section: "1"
letter: "r"
url: "/docs/linux/man/1-raptor-config/"
description: "raptor-config – script to get information about the installed version of Raptor"
---

<h2 class="name">NAME</h2>
<p> raptor-config &#8211; script to get information about the installed version of Raptor </p>
<h2>SYNOPSIS</h2>
<p> <code>raptor-config</code> [&#8211;cflags] [&#8211;options] [&#8211;help] [&#8211;libs] [&#8211;libtool-libs] [&#8211;private-libs] [&#8211;prefix<i>[=DIR]</i>] [&#8211;version-decimal] [&#8211;version]</p>
<h2>DESCRIPTION</h2>
<p> <i>raptor-config</i> is a tool that is used to determine the compile and linker flags that should be used to compile and link programs that use the Raptor RDF parser library.</p>
<h2>OPTIONS</h2>
<p> <i>raptor-config</i> accepts the following options:</p>
<dl>
<dt><code>&#8211;cflags</code></p>
<dd> Print the compiler flags that are necessary to compile a raptor program.</p>
<dt><code>&#8211;options</code></p>
<dd> Print raptor compiled options such as parsers and serializers available, the XML parser used (if any) and the WWW retrieval library used (if any).</p>
<dt><code>&#8211;help</code></p>
<dd> Print a help message summarising usage.</p>
<dt><code>&#8211;libs</code></p>
<dd> Print the linker flags that are necessary to link a raptor program. This excludes linker arguments used to build the raptor shared library.</p>
<dt><code>&#8211;libtool-libs</code></p>
<dd> Print the path to the libtool file for raptor.</p>
<dt><code>&#8211;private-libs</code></p>
<dd> Print the linker flags that are necessary to build the raptor shared library. This option is not usually needed because the raptor shared library has already been dynamically linked against these flags.</p>
<dt><code>&#8211;prefix=PREFIX</code></p>
<dd> If specified, use PREFIX instead of the installation prefix that raptor was built with when computing the output for the &#8211;cflags and &#8211;libs options. This option must be specified before any &#8211;libs or &#8211;cflags options.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the currently installed version of raptor on the standard output.</p>
<dt><code>&#8211;version-decimal</code></p>
<dd> Print the currently installed version of raptor as a decimal integer.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libraptor/">libraptor</a>(3)</code></p>
<h2>AUTHOR</h2>
<p> Dave Beckett &#8211; <a rel="nofollow" href="http://www.dajobe.org/">http://www.dajobe.org/</a> </p>
<h2>Index</h2>
