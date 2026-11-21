---

title: "rasqal-config(1)"
name: "rasqal-config"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rasqal-config/"
description: "rasqal-config – script to get information about the installed version of the RDF query library"
---

<p> rasqal-config &#8211; script to get information about the installed version of the RDF query library </p>
<h2>SYNOPSIS</h2>
<p> <code>rasqal-config</code> [&#8211;prefix<i>[=DIR]</i>] [&#8211;libs] [&#8211;libtool-libs] [&#8211;cflags] [&#8211;version] [&#8211;version-decimal] [&#8211;help]</p>
<h2>DESCRIPTION</h2>
<p> <i>rasqal-config</i> is a tool that is used to determine the compile and linker flags that should be used to compile and link programs that use the Rasqal RDF query library.</p>
<h2>OPTIONS</h2>
<p> <i>rasqal-config</i> accepts the following options:</p>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> Print the currently installed version of rasqal on the standard output.</dd>
<dt><code>&#8211;version-decimal</code></dt>
<dd> Print the currently installed version of rasqal as a decimal integer.</dd>
<dt><code>&#8211;libs</code></dt>
<dd> Print the linker flags that are necessary to link a program with Rasqal.</dd>
<dt><code>&#8211;libtool-libs</code></dt>
<dd> Print the path to the libtool file for rasqal.</dd>
<dt><code>&#8211;cflags</code></dt>
<dd> Print the compiler flags that are necessary to compile a program with the RDF query language.</dd>
<dt><code>&#8211;prefix=PREFIX</code></dt>
<dd> If specified, use PREFIX instead of the installation prefix that Rasqal was built with when computing the output for the &#8211;cflags and &#8211;libs options. This option must be specified before any &#8211;libs or &#8211;cflags options.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-librasqal/">librasqal</a>(3)</code></p>
<h2>AUTHOR</h2>
<p> Dave Beckett &#8211; <a rel="nofollow" href="http://www.dajobe.org/">http://www.dajobe.org/</a> </p>
