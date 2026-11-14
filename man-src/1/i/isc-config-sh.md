---
title: "isc-config-sh(1)"
name: "isc-config-sh"
section: "1"
letter: "i"
url: "/docs/linux/man/1-isc-config-sh/"
description: "isc-config.sh – Get information about the installed version of ISC BIND"
---

<p>isc-config.sh &#8211; Get information about the installed version of ISC BIND </p>
<h2>Synopsis</h2>
<dl>
<dt> <code>isc-config.sh</code> [<code>&#8211;cflags</code>] [<code>&#8211;exec-prefix</code>] [<code>&#8211;libs</code>] [<code>&#8211;prefix</code>] [<code>&#8211;version</code>] [libraries&#8230;]</dl>
<h2>Description</h2>
<p><code>isc-config.sh</code></p>
<dd>prints information related to the installed version of ISC BIND, such as the compiler and linker flags required to compile and link programs that use ISC BIND libraries. </p>
<p> The optional libraries are used to report specific details for compiling and linking for the listed libraries. The allowed choices are: <code>isc</code>, <code>isccc</code>, <code>isccfg</code>, <code>dns</code>, <code>lwres</code>, and <code>bind9</code>. Multiple libraries may be listed on the command line. (Some libraries require other libraries, so are implied.)</p>
<h2>Options</h2>
<p>&#8211;cflags</p>
<dl>
<dd>Prints the compiler command line options required to compile files that use ISC BIND. Use the <code>libraries</code> command line argument(s) to print additional specific flags to pass to the C compiler.</dl>
<p> &#8211;exec-prefix</p>
<dl>
<dd>Prints the directory prefix used in the ISC BIND installation for architecture dependent files to standard output.</dl>
<p> &#8211;libs</p>
<dl>
<dd>Prints the linker command line options used to link with the ISC BIND libraries. Use the <code>libraries</code> command line argument(s) to print additional specific flags.</dl>
<p> &#8211;prefix</p>
<dl>
<dd>Prints the directory prefix used in the ISC BIND installation for architecture independent files to standard output.</dl>
<p> &#8211;version</p>
<dl>
<dd>Prints the version of the installed ISC BIND suite.</dl>
<h2>Return Values</h2>
<p><code>isc-config.sh</code> returns an exit status of 1 if invoked with invalid arguments or no arguments at all. It returns 0 if information was successfully printed.</p>
<h2>Author</h2>
<p>Internet Systems Consortium</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009 Internet Systems Consortium, Inc. (&quot;ISC&quot;)</p>
